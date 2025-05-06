import math
import multiprocessing

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def calcular_primos(rango, lock):
    primos = []
    for num in rango:
        if es_primo(num):
            primos.append(num)
    with lock:
        with open("primos.txt", "a") as f:
            for primo in primos:
                f.write(f"{primo}\n")

def dividir_rango(start, end, num_procesos):
    step = (end - start) // num_procesos
    ranges = [(start + i*step, start + (i+1)*step) for i in range(num_procesos)]
    ranges[-1] = (ranges[-1][0], end)
    return ranges

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    num_procesos = 8
    start, end = 1, 100000  # Ajustar rango para calcular primos
    ranges = dividir_rango(start, end, num_procesos)

    procesos = []
    for rango in ranges:
        p = multiprocessing.Process(target=calcular_primos, args=(range(rango[0], rango[1]), lock))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    print("Cálculo de primos terminado.")
