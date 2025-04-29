import signal
import threading
import time
import queue
import os

salir = False
clientes = []

def handler(signum, frame):
    global salir
    print(f"⚠️ Señal {signum} recibida. Iniciando limpieza...")
    salir = True

def cliente(id, eventos):
    while not salir:
        eventos.put(f"Cliente {id} activo.")
        time.sleep(1)
    eventos.put(f"Cliente {id} desconectado limpiamente.")

signal.signal(signal.SIGTERM, handler)

eventos = queue.Queue()

# Lanzar múltiples clientes simulados
for i in range(3):
    t = threading.Thread(target=cliente, args=(i + 1, eventos))
    t.start()
    clientes.append(t)

print(f"Servidor ejecutándose... PID: {os.getpid()}")
print("Envia SIGTERM con: kill -TERM <PID>")

# Proceso principal recolecta eventos
while not salir or not eventos.empty():
    try:
        msg = eventos.get(timeout=1)
        print("[LOG]:", msg)
    except queue.Empty:
        pass

# Esperar limpieza
for c in clientes:
    c.join()

print("✅ Servidor finalizado correctamente.")
