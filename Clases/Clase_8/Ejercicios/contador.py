from multiprocessing import Process, Value, Lock
import time

def incrementar(valor, lock):
    for _ in range(10):
        time.sleep(0.01)
        with lock:  # Adquirimos el Lock para acceder de forma exclusiva al valor
            valor.value += 1

if __name__ == "__main__":
    contador = Value('i', 0)  # 'i' es para enteros
    lock = Lock()  # Creamos un Lock
    procesos = []

    # Crea 4 procesos para incrementar el valor
    for _ in range(4):
        p = Process(target=incrementar, args=(contador, lock))
        p.start()
        procesos.append(p)

    # Espera a que todos los procesos terminen
    for p in procesos:
        p.join()

    # Muestra el resultado
    print(f"Valor final del contador: {contador.value}")
