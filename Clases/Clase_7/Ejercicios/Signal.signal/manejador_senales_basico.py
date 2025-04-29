import signal
import os
import time

def manejador(sig, frame):
    if sig == signal.SIGINT:
        print("🔴 SIGINT recibido (Ctrl+C)")
    elif sig == signal.SIGTERM:
        print("⚫ SIGTERM recibido (kill)")
    elif sig == signal.SIGHUP:
        print("🟡 SIGHUP recibido (terminal cerrada o kill -HUP)")

signal.signal(signal.SIGINT, manejador)
signal.signal(signal.SIGTERM, manejador)
signal.signal(signal.SIGHUP, manejador)

print(f"PID: {os.getpid()}")
print("Esperando señales...")

while True:
    time.sleep(1)
