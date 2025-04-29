import signal
import os
import time

def manejador(sig, frame):
    print(f"📢 Recibí SIGTERM (señal {sig}) desde otro proceso. ¡Sigo vivo!")

# Registramos el manejador para SIGTERM
signal.signal(signal.SIGTERM, manejador)

print(f"📛 PID del proceso: {os.getpid()}")
print("Esperando SIGTERM desde otra terminal...")

while True:
    time.sleep(1)


