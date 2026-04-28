import pytest
from unittest.mock import patch
from src.core.engine import RealEngine
from src.core.examples import EducationalKeylogger


# Mocking Listener and Key from pynput
@pytest.fixture
def mock_pynput():
    with patch('src.core.engine.Listener') as mock_listener, \
         patch('src.core.engine.Key') as mock_key:
        yield mock_listener, mock_key


def test_engine_init():
    """Verifica que el motor se inicialice correctamente."""
    test_log = "tests/test.log"
    engine = RealEngine(output=test_log)
    assert engine.output_file == test_log


def test_engine_on_press(tmp_path):
    """Verifica que la pulsación de tecla se registre en el archivo."""
    d = tmp_path / "logs"
    d.mkdir()
    log_file = d / "test.log"

    engine = RealEngine(output=str(log_file))
    engine.on_press("A")

    with open(log_file, "r") as f:
        content = f.read()
        assert "A " in content


def test_engine_on_release_esc(mock_pynput):
    """Verifica que ESC detenga el motor."""
    _, mock_key = mock_pynput
    mock_key.esc = "ESC_KEY"

    engine = RealEngine()
    result = engine.on_release("ESC_KEY")
    assert result is False


@patch('src.core.engine.Listener')
def test_engine_start_calls_listener(mock_listener):
    """Verifica que engine.start() inicie el Listener."""
    engine = RealEngine()
    engine.start()
    assert mock_listener.called


def test_educational_keylogger():
    """Verifica el funcionamiento básico del modo educativo."""
    edu = EducationalKeylogger()
    assert edu.is_running is False

    # Mocking print to avoid spamming console during tests
    with patch('builtins.print'):
        edu.run()
        # En la implementación actual, run termina solo
        assert edu.is_running is True
