import os
import signal
import time

def hijo():
    print(f"👶 Hijo ejecutándose (PID {os.getpid()})")
    try:
        time.sleep(10)
    except:
        pass
    print("👶 Hijo finalizó")

def padre(pid_hijo):
    print(f"👨 Padre enviará SIGTERM a PID {pid_hijo} en 3 segundos")
    time.sleep(3)
    os.kill(pid_hijo, signal.SIGTERM)  # Envía SIGTERM
    _, status = os.wait()  # Espera que el hijo termine
    print(f"👨 Hijo {pid_hijo} terminado con estado {status}")

pid = os.fork()

if pid == 0:
    # Hijo maneja SIGTERM y termina limpiamente
    signal.signal(signal.SIGTERM, lambda sig, frame: exit(0))
    hijo()
else:
    padre(pid)
