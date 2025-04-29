import os
import signal
import time
import multiprocessing

# Manejador de la señal para los consumidores
def manejar_senal_producto(sig, frame):
    print(f"Consumidor {os.getpid()}: Producto listo, procesando...")

# Proceso productor
def proceso_productor(consumidores):
    print("Productor: Generando el producto...")
    time.sleep(2)  # Simulando la generación de un producto
    print("Productor: Producto listo, notificando a los consumidores...")
    for pid in consumidores:
        os.kill(pid, signal.SIGUSR1)  # Notificar a cada consumidor

# Proceso consumidor
def proceso_consumidor():
    print(f"Consumidor {os.getpid()}: Esperando el producto...")
    signal.signal(signal.SIGUSR1, manejar_senal_producto)  # El consumidor espera la señal SIGUSR1
    signal.pause()  # Pausa hasta que reciba la señal
    print(f"Consumidor {os.getpid()}: Producto procesado.")

# Main
if __name__ == "__main__":
    # Usar Manager para compartir la lista de consumidores entre procesos
    with multiprocessing.Manager() as manager:
        consumidores = manager.list()  # Lista compartida entre procesos

        # Crear 3 consumidores
        for _ in range(3):
            pid = os.fork()
            if pid == 0:  # Proceso hijo (consumidor)
                proceso_consumidor()
                exit()  # Terminar el proceso hijo después de ejecutar el consumidor
            else:
                consumidores.append(pid)  # Agregar el PID del consumidor a la lista

        # Proceso padre (productor)
        proceso_productor(consumidores)
