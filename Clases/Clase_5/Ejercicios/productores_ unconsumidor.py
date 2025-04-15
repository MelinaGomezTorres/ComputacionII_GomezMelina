# Código usando fork y multiprocessing.Queue:

import os
import time
from multiprocessing import Queue

def productor(nombre, q):
    for i in range(3):
        mensaje = f"{nombre} produjo {i}"
        print(f"[{nombre}] Enviando: {mensaje}")
        q.put(mensaje)

def consumidor(q, total_mensajes):
    for _ in range(total_mensajes):
        dato = q.get()
        print(f"[Consumidor] Recibido: {dato}")

if __name__ == "__main__":
    q = Queue()

    pid_p1 = os.fork()
    if pid_p1 == 0:
        productor("P1", q)
        os._exit(0)

    pid_p2 = os.fork()
    if pid_p2 == 0:
        productor("P2", q)
        os._exit(0)

    # Esperar que los productores terminen antes de consumir
    os.waitpid(pid_p1, 0)
    os.waitpid(pid_p2, 0)

    pid_cons = os.fork()
    if pid_cons == 0:
        total = 3 + 3  # Total de mensajes esperados
        consumidor(q, total)
        os._exit(0)

    os.waitpid(pid_cons, 0)


# Código hecho solamente con multiprocessing:

'''from multiprocessing import Process, Queue

def productor(nombre, q):
    for i in range(3):
        mensaje = f"{nombre} produjo {i}"
        print(f"[{nombre}] Enviando: {mensaje}")
        q.put(mensaje)

def consumidor(q, total_mensajes):
    for _ in range(total_mensajes):
        dato = q.get()
        print(f"[Consumidor] Recibido: {dato}")

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=productor, args=("P1", q))
    p2 = Process(target=productor, args=("P2", q))
    
    total = 3 + 3  # Cada productor envía 3 mensajes
    p3 = Process(target=consumidor, args=(q, total))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
'''
