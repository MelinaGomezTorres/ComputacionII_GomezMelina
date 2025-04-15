# Código usando fork y multiprocessing.Queue:

import os
import time
from multiprocessing import Queue

# Función del productor
def productor(q):
    for i in range(1, 6):
        print(f"[Productor] Enviando: {i}")
        q.put(i)  # Envia un número a la queue

# Función del consumidor
def consumidor(q):
    while True:
        valor = q.get()  # Obtiene un valor de la queue
        if valor == "FIN":  # Condición de parada
            break
        print(f"[Consumidor] Recibido: {valor}")

if __name__ == "__main__":
    q = Queue()  # Creamos la queue compartida
    
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
    q.put("FIN")  # Indicamos al consumidor que termine
    os.waitpid(pid_consumidor, 0)



# Código hecho solamente con multiprocessing:

'''
from multiprocessing import Process, Queue

# Función del productor
def productor(q):
    for i in range(1, 6):
        print(f"[Productor] Enviando: {i}")
        q.put(i)  # Envia un número a la queue

# Función del consumidor
def consumidor(q):
    while True:
        valor = q.get()  # Obtiene un valor de la queue
        if valor == "FIN":  # Condición de parada
            break
        print(f"[Consumidor] Recibido: {valor}")

if __name__ == "__main__":
    q = Queue()  # Creamos la queue compartida

    # Iniciamos los procesos
    p1 = Process(target=productor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))

    p1.start()  # Arrancamos el productor
    p2.start()  # Arrancamos el consumidor

    p1.join()   # El proceso principal espera que el productor termine
    q.put("FIN")  # Indicamos al consumidor que termine
    p2.join()   # El proceso principal espera que el consumidor termine
'''