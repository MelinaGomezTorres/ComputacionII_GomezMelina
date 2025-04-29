import signal
import threading
import time
import queue

salir = False
eventos = queue.Queue()

def handler(signum, frame):
    global salir
    print(f"Señal {signum} recibida.")
    salir = True

def tarea(nombre):
    while not salir:
        eventos.put(f"{nombre} hizo algo.")
        time.sleep(1)
    eventos.put(f"{nombre} termina.")

signal.signal(signal.SIGINT, handler)

hilo1 = threading.Thread(target=tarea, args=("Hilo 1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo 2",))

hilo1.start()
hilo2.start()

# Mientras no se haya pedido salir o la cola tenga eventos
while not salir or not eventos.empty():
    try:
        evento = eventos.get(timeout=1)
        print("[LOG]:", evento)
    except queue.Empty:
        pass

hilo1.join()
hilo2.join()
print("Programa finalizado.")
