import signal
import os
import time

def handler(sig, frame):
    print(f"Recibida señal: {sig}")

signal.signal(signal.SIGUSR1, handler)

print(f"Esperando señal... PID: {os.getpid()}")

while True:
    time.sleep(1)
