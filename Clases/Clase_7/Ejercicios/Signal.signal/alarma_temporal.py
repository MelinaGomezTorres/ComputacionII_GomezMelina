import signal
import time

def manejador_alarma(sig, frame):
    print("⏰ Tiempo límite excedido. Terminando...")
    exit(1)

signal.signal(signal.SIGALRM, manejador_alarma)
signal.alarm(5)  # 5 segundos de tiempo límite

print("🕒 Tenés 5 segundos para completar la tarea...")
try:
    # Simulamos una tarea larga
    time.sleep(10)
except:
    pass

print("✅ Tarea completada a tiempo")
