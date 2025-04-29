import signal
import os
import time
import queue

# Cola para encolar las señales
cola = queue.Queue()

def manejador(sig, frame):
    print(f"Recibí la señal {sig}, añadiéndola a la cola.")
    cola.put(sig)

def procesar_trabajo():
    while True:
        if not cola.empty():
            sig = cola.get()
            print(f"Procesando trabajo para la señal {sig}")
            time.sleep(2)  # Simular procesamiento
        else:
            time.sleep(1)

# Registrar el handler para SIGUSR1
signal.signal(signal.SIGUSR1, manejador)

# Proceso productor que genera trabajos
def productor():
    while True:
        time.sleep(3)
        print("Generando trabajo...")
        os.kill(os.getpid(), signal.SIGUSR1)  # Enviar SIGUSR1 al propio proceso

# Ejecutar productor y procesar los trabajos
if __name__ == "__main__":
    # Crear un hilo para procesar la cola de trabajos
    import threading
    hilo = threading.Thread(target=procesar_trabajo)
    hilo.daemon = True  # Asegura que el hilo termine cuando termine el programa
    hilo.start()

    # Ejecutar el productor (esto genera señales SIGUSR1)
    productor()


