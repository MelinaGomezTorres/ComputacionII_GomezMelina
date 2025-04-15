# Código usando fork y multiprocessing.Queue:

import os
import time
from multiprocessing import Queue

def productor(q):
    for i in range(10):
        print(f"[Productor] Enviando: {i}")
        q.put(i)
    for _ in range(3):  # 3 consumidores → enviamos 3 "FIN"
        q.put("FIN")

def consumidor(nombre, q):
    while True:
        dato = q.get()
        if dato == "FIN":
            print(f"[{nombre}] Finaliza")
            break
        print(f"[{nombre}] Procesando: {dato}")
        time.sleep(0.5)

if __name__ == "__main__":
    q = Queue()

    pid_prod = os.fork()
    if pid_prod == 0:
        productor(q)
        os._exit(0)

    pid_c1 = os.fork()
    if pid_c1 == 0:
        consumidor("C1", q)
        os._exit(0)

    pid_c2 = os.fork()
    if pid_c2 == 0:
        consumidor("C2", q)
        os._exit(0)

    pid_c3 = os.fork()
    if pid_c3 == 0:
        consumidor("C3", q)
        os._exit(0)

    # Esperamos a que todos terminen
    os.waitpid(pid_prod, 0)
    os.waitpid(pid_c1, 0)
    os.waitpid(pid_c2, 0)
    os.waitpid(pid_c3, 0)


# Código hecho solamente con multiprocessing:

'''from multiprocessing import Process, Queue
import time

def productor(q):
    for i in range(10):
        print(f"[Productor] Enviando: {i}")
        q.put(i)
    for _ in range(3):  # 3 consumidores → enviamos 3 "FIN"
        q.put("FIN")

def consumidor(nombre, q):
    while True:
        dato = q.get()
        if dato == "FIN":
            print(f"[{nombre}] Finaliza")
            break
        print(f"[{nombre}] Procesando: {dato}")
        time.sleep(0.5)

if __name__ == "__main__":
    q = Queue()

    prod = Process(target=productor, args=(q,))
    cons1 = Process(target=consumidor, args=("C1", q))
    cons2 = Process(target=consumidor, args=("C2", q))
    cons3 = Process(target=consumidor, args=("C3", q))

    prod.start()
    cons1.start()
    cons2.start()
    cons3.start()

    prod.join()
    cons1.join()
    cons2.join()
    cons3.join()
'''