import os
import signal
import time

# Contador de señales SIGINT
__contador_SIGINT__ = 0

def manejador_SIGINT(sig, frame):
    global __contador_SIGINT__
    __contador_SIGINT__ += 1
    print(f"🛑 SIGINT recibido #{__contador_SIGINT__}")
    
    # Si el contador llega a 3, terminamos el proceso
    if __contador_SIGINT__ >= 3:
        print("💥 Recibí 3 SIGINT. Terminando proceso hijo.")
        exit(0)

# Crear un proceso hijo
pid = os.fork()

if pid == 0:
    # Proceso hijo
    signal.signal(signal.SIGINT, manejador_SIGINT)  # Registramos el manejador en el hijo
    print(f"Proceso hijo (PID: {os.getpid()}) esperando SIGINT...")
    while True:
        time.sleep(1)
else:
    # Proceso padre
    print(f"Proceso padre (PID: {os.getpid()}) enviando SIGINT al hijo (PID: {pid})...")
    time.sleep(1)  # Esperamos un poco para que el hijo se ponga en espera

    # Enviar SIGINT al hijo 3 veces
    for _ in range(3):
        os.kill(pid, signal.SIGINT)
        time.sleep(1)  # Esperamos 1 segundo entre señales

    print("Proceso padre terminó de enviar SIGINT.")
