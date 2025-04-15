# Código usando fork y multiprocessing.Queue:

import os
import time
from multiprocessing import Queue

def productor(q):
    for i in range(5):
        print(f"[Productor] Enviando: {i}")
        q.put(i)  # Poner datos en la queue

def consumidor(q):
    for _ in range(5):
        valor = q.get()  # Tomar datos de la queue
        print(f"[Consumidor] Recibido: {valor}")

if __name__ == "__main__":
    q = Queue()
    
    pid_productor = os.fork()
    
    if pid_productor == 0:
        # Proceso hijo (Productor)
        productor(q)
        os._exit(0)
    
    pid_consumidor = os.fork()
    
    if pid_consumidor == 0:
        # Proceso hijo (Consumidor)
        consumidor(q)
        os._exit(0)
    
    # Esperar que ambos procesos terminen
    os.waitpid(pid_productor, 0)
    os.waitpid(pid_consumidor, 0)



# Código hecho solamente con multiprocessing:

'''
from multiprocessing import Process, Queue

def productor(q):
    for i in range(5):
        print(f"[Productor] Enviando: {i}")
        q.put(i)  # Poner datos en la queue

def consumidor(q):
    for _ in range(5):
        valor = q.get()  # Tomar datos de la queue
        print(f"[Consumidor] Recibido: {valor}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=productor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
'''

