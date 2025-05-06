from multiprocessing import Pool

# Función que calcula el cuadrado de un número
def calcular_cuadrado(n):
    return n ** 2

if __name__ == "__main__":
    # Lista de números del 1 al 10
    numeros = list(range(1, 11))

    # Crea un Pool con 4 procesos
    with Pool(4) as pool:
        # Distribuye la tarea entre los procesos del Pool
        resultados = pool.map(calcular_cuadrado, numeros)

    # Muestra los resultados
    print(f"Los cuadrados de los números son: {resultados}")
