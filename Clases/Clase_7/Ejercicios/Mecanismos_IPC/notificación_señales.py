import os
import signal
import time

# Manejador de la señal SIGUSR1
def manejador_signals(signal_num, frame):
    print("¡Señal SIGUSR1 recibida!")

# Registrar el manejador
signal.signal(signal.SIGUSR1, manejador_signals)

# Crear un proceso hijo
pid = os.fork()

if pid == 0:  # Proceso hijo
    time.sleep(5)
    os.kill(os.getppid(), signal.SIGUSR1)  # Enviar señal SIGUSR1 al padre
    print("Proceso hijo ha enviado la señal SIGUSR1.")
else:  # Proceso padre
    print("Proceso principal esperando señal...")
    time.sleep(10)  # Esperar para recibir la señal
