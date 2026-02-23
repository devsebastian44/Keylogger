import time


class EducationalKeylogger:
    """
    Esta clase demuestra el concepto de captura de eventos
    sin interactuar realmente con las APIs de bajo nivel del sistema.
    """

    def __init__(self):
        self.is_running = False

    def run(self):
        self.is_running = True
        print("[Demo] Simulando captura de eventos de teclado...")
        print("[Demo] Presione Ctrl+C para detener.")

        # Simulación de eventos
        simulated_events = [
            "H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"
        ]

        try:
            for char in simulated_events:
                if not self.is_running:
                    break
                print(f"[EVENT] Tecla detectada: {char}")
                time.sleep(0.5)
            print("[Demo] Simulación completada con éxito.")
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        print("\n[*] Deteniendo demostración...")
        self.is_running = False
