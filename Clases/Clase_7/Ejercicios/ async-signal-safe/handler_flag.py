import os
import signal
import time

# Bandera de interrupción
interrumpir = False

def handler(sig, frame):
    global interrumpir
    interrumpir = True

# Registrar handler para SIGUSR1
signal.signal(signal.SIGUSR1, handler)

print(f"PID: {os.getpid()}")
print("Simulando tarea larga... (envía SIGUSR1 para interrumpir)")

for i in range(1, 101):
    if interrumpir:
        print("\nTarea interrumpida.")
        break
    print(f"Trabajando... paso {i}")
    time.sleep(0.5)

print("Proceso finalizado.")

