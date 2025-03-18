import argparse

def main():
    parser = argparse.ArgumentParser(description="Procesa un archivo de entrada y genera un archivo de salida.")

    parser.add_argument("-i", "--input", required=True, help="Archivo de entrada")
    parser.add_argument("-o", "--output", required=True, help="Archivo de salida")

    args = parser.parse_args()

    print(f"Archivo de entrada: {args.input}")
    print(f"Archivo de salida: {args.output}")

if __name__ == "__main__":
    main()
