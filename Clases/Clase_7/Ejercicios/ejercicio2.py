import os
import signal
import time
import random

def manejador(sig, frame):
    print(f"Se recibió la señal {sig} de un hijo con PID: {os.getpid()}")

# Crear tres procesos hijos
def crear_hijo():
    hijo_pid = os.fork()
    if hijo_pid == 0:
        time.sleep(random.randint(1, 3))
        if random.choice([True, False]):
            os.kill(os.getppid(), signal.SIGUSR1)
        else:
            os.kill(os.getppid(), signal.SIGUSR2)
        os.kill(os.getppid(), signal.SIGTERM)
        os._exit(0)

# Registrar el handler
signal.signal(signal.SIGUSR1, manejador)
signal.signal(signal.SIGUSR2, manejador)
signal.signal(signal.SIGTERM, manejador)

# Crear hijos
for _ in range(3):
    crear_hijo()

# Mantener proceso principal en espera
time.sleep(10)
