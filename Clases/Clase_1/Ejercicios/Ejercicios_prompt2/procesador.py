import argparse

def procesar_archivo(archivo_entrada, archivo_salida, mayusculas=False):
    """
    Procesa un archivo de entrada y guarda el resultado en un archivo de salida.

    Args:
        archivo_entrada (str): Ruta al archivo de entrada.
        archivo_salida (str): Ruta al archivo de salida.
        mayusculas (bool, opcional): Si es True, convierte el texto a mayúsculas.
    """
    try:
        with open(archivo_entrada, 'r') as f_entrada:
            texto = f_entrada.read()

        if mayusculas:
            texto = texto.upper()

        with open(archivo_salida, 'w') as f_salida:
            f_salida.write(texto)

        print(f"Archivo procesado correctamente. Resultado guardado en '{archivo_salida}'.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesa un archivo de texto.")
    parser.add_argument("-i", "--input", required=True, help="Archivo de entrada")
    parser.add_argument("-o", "--output", required=True, help="Archivo de salida")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Convierte el texto a mayúsculas")

    args = parser.parse_args()

    procesar_archivo(args.input, args.output, args.uppercase)
