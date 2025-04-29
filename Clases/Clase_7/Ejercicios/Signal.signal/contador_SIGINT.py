import signal
import os
import time

__contador__ = 0  # Global para contar SIGINT

def manejador_SIGINT(sig, frame):
    global __contador__
    __contador__ += 1
    print(f"🛑 SIGINT #{__contador__} recibido")
    if __contador__ >= 3:
        print("💥 Recibí 3 SIGINT. Terminando...")
        exit(0)

signal.signal(signal.SIGINT, manejador_SIGINT)

print(f"PID: {os.getpid()}")
print("Presioná Ctrl+C tres veces para terminar")

while True:
    time.sleep(1)
