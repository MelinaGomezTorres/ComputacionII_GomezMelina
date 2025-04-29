import signal
import os
import time

# 1. Definimos un manejador que se ejecuta cuando llega una señal
def manejador(sig, frame):
    print(f"📢 Señal recibida: {sig}. ¡No me cerrás tan fácil!")

# 2. Asociamos el manejador a la señal SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, manejador)

# 3. Mostramos el PID del proceso para pruebas
print(f"PID del proceso: {os.getpid()}")
print("🕓 Esperando señal... (Presioná Ctrl+C para enviar SIGINT)")

# 4. Bucle infinito para que el programa siga corriendo
while True:
    time.sleep(1)
