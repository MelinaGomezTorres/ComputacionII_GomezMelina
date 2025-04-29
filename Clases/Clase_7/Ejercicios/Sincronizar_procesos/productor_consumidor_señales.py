import os
import signal
import time

# Manejador para el consumidor
def manejador(sig, frame):
    print("🍏 Consumidor ha recibido la señal para empezar.")
    # El consumidor hace su trabajo
    time.sleep(2)
    print("🍏 Consumidor ha terminado de procesar.")

# Registra el manejador para SIGUSR1
signal.signal(signal.SIGUSR1, manejador)

# Proceso productor
def productor(consumer_pid):
    print(f"🍅 Productor (PID: {os.getpid()}) está produciendo un producto...")
    time.sleep(3)  # Simula tiempo de producción
    print("🍅 Productor ha producido el producto. Enviando señal al consumidor.")
    os.kill(consumer_pid, signal.SIGUSR1)  # Envía la señal al consumidor

# Crear proceso hijo para el consumidor
pid = os.fork()

if pid == 0:
    # Proceso hijo (consumidor)
    print(f"🍏 Consumidor (PID: {os.getpid()}) está esperando una señal...")
    while True:
        time.sleep(1)  # Espera la señal
else:
    # Proceso padre (productor)
    consumer_pid = pid  # PID del consumidor
    productor(consumer_pid)
