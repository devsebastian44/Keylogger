from unittest.mock import patch
from src.core.engine import RealEngine


def test_engine_init():
    """Verifica que el motor se inicialice correctamente."""
    engine = RealEngine(output="tests/test.log")
    assert engine.output_file == "tests/test.log"


@patch('src.core.engine.Listener')
def test_engine_start_mock(mock_listener):
    """Verifica que el motor llame al listener de pynput."""
    engine = RealEngine()
    engine.start()
    assert mock_listener.called


def test_educational_mode():
    """Verifica que el modo educativo no falle."""
    from src.core.examples import EducationalKeylogger
    edu = EducationalKeylogger()
    assert not edu.is_running
    # No ejecutamos .run() para evitar bloqueos en CI
