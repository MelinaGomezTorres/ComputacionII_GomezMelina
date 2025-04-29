import signal
import time

def handler(sig, frame):
    print("¡Hola!")

# Registrar el handler para SIGINT
signal.signal(signal.SIGINT, handler)

print("Esperando SIGINT... (Ctrl+C)")
while True:
    time.sleep(1)  # Mantiene el programa corriendo
