import signal
import threading
import time

salir = False

def handler(signum, frame):
    global salir
    print(f"Señal {signum} recibida.")
    salir = True

def tarea(nombre):
    while not salir:
        print(f"{nombre} trabajando...")
        time.sleep(1)
    print(f"{nombre} termina y sale.")

signal.signal(signal.SIGINT, handler)

hilo1 = threading.Thread(target=tarea, args=("Hilo 1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo 2",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
print("Programa finalizado.")
