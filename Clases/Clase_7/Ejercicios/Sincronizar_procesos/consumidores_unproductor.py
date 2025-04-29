import os
import signal
import time
from multiprocessing import Process, Manager

# Manejador de la señal en consumidores
def manejar_senal_producto(sig, frame):
    print(f"[{os.getpid()}] Señal recibida: producto listo.")

# Función que ejecuta cada consumidor
def consumidor():
    signal.signal(signal.SIGUSR1, manejar_senal_producto)
    print(f"Consumidor {os.getpid()} esperando señal...")
    signal.pause()
    print(f"Consumidor {os.getpid()} terminó de procesar el producto.")

# Función que ejecuta el productor
def productor(consumidores):
    print(f"Productor {os.getpid()} generando producto...")
    time.sleep(2)
    print("Producto generado. Enviando señales...")
    for pid in consumidores:
        os.kill(pid, signal.SIGUSR1)
    print("Señales enviadas.")

if __name__ == "__main__":
    with Manager() as manager:
        consumidores = manager.list()
        procesos = []

        # Crear y lanzar 3 procesos consumidores
        for _ in range(3):
            proceso = Process(target=consumidor)
            proceso.start()
            consumidores.append(proceso.pid)
            procesos.append(proceso)

        time.sleep(1)  # Dar tiempo a los consumidores a registrarse

        # Crear y lanzar el proceso productor
        productor(consumidores)

        # Esperar que los consumidores terminen
        for proceso in procesos:
            proceso.join()



