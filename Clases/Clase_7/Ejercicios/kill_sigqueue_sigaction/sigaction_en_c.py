import os
import signal
import time

# Función para manejar SIGTERM
def manejador(sig, frame):
    print(f"🛑 El proceso hijo (PID: {os.getpid()}) recibió la señal SIGTERM y terminará.")

# Registrar el manejador para SIGTERM
signal.signal(signal.SIGTERM, manejador)

# Crear un proceso hijo
pid = os.fork()

if pid == 0:
    # Este es el proceso hijo
    print(f"👶 Proceso hijo iniciado (PID: {os.getpid()}). Durmiendo durante 10 segundos...")
    time.sleep(10)  # El hijo duerme 10 segundos antes de terminar
    print("😴 Proceso hijo terminó sin recibir señales.")
else:
    # Este es el proceso padre
    print(f"👨‍👩‍👧 Proceso padre (PID: {os.getpid()}) enviando SIGTERM al hijo (PID: {pid})...")
    time.sleep(3)  # El padre espera 3 segundos
    os.kill(pid, signal.SIGTERM)  # Enviar SIGTERM al hijo
    print("🛑 Se envió SIGTERM al hijo. Esperando que termine...")
    
    # Espera hasta que el hijo termine
    os.waitpid(pid, 0)  # El proceso padre espera que el hijo termine
    print("✅ El hijo ha terminado. El proceso padre también finalizará.")

