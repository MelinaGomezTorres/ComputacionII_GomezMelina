import os
import signal
import time

def manejador(sig, frame):
    print(f"🛑 Recibí la señal {sig}.")

# Registra el manejador para SIGTERM
signal.signal(signal.SIGTERM, manejador)

# Simula un proceso en espera
print(f"PID: {os.getpid()}. Esperando SIGTERM...")

# Este proceso se quedará esperando la señal SIGTERM
while True:
    time.sleep(1)
