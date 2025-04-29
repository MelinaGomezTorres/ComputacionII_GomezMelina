import signal
import os
import time

def manejador_SIGALRM(sig, frame):
    print("⏰ Señal SIGALRM recibida")

def manejador_SIGHUP(sig, frame):
    print("🔄 Señal SIGHUP recibida")

# Registramos los manejadores
signal.signal(signal.SIGALRM, manejador_SIGALRM)
signal.signal(signal.SIGHUP, manejador_SIGHUP)

print(f"PID del proceso: {os.getpid()}")
print("Esperando señales...")

# Enviará SIGALRM en 5 segundos
signal.alarm(5)

# Esperamos señales
while True:
    time.sleep(1)
