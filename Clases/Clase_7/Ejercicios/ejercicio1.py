import signal
import atexit
import time

def despedida(sig, frame):
    print(f"Recibí la señal {sig}, cerrando el programa.")

def limpieza():
    print("Ejecutando limpieza final...")

# Registrar la limpieza al final
atexit.register(limpieza)

# Registrar el handler para SIGTERM
signal.signal(signal.SIGTERM, despedida)

print("El proceso está corriendo... Envia SIGTERM para terminarlo.")

# Mantener el programa corriendo
time.sleep(30)
