import signal
import time
import os
import queue

# Cola para registrar eventos de forma segura
eventos = queue.Queue()

def handler(sig, frame):
    eventos.put(f"Evento recibido: señal {sig}")

# Registrar el handler para SIGUSR1
signal.signal(signal.SIGUSR1, handler)

print(f"PID: {os.getpid()}")
print("Trabajando... (envía SIGUSR1 para registrar evento)")

try:
    while True:
        # Simula trabajo
        print("Procesando tarea...")
        time.sleep(2)

        # Procesar eventos pendientes
        while not eventos.empty():
            evento = eventos.get()
            print(f"[LOG]: {evento}")

except KeyboardInterrupt:
    print("\nTerminando programa.")
