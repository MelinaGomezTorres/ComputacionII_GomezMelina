import os
import time

def hijo(id):
    time.sleep(id*2)  # Duermen distinto tiempo
    print(f"Hijo {id} PID {os.getpid()} termina.")
    os._exit(id)

if __name__ == "__main__":
    hijos = []
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            hijo(i+1)
        else:
            hijos.append(pid)

    print(f"Padre {os.getpid()} espera hijos...")

    orden_terminacion = []
    for _ in range(3):
        pid, status = os.waitpid(-1, 0)
        orden_terminacion.append((pid, status))
        print(f"Hijo con PID {pid} terminó con status {status}")

    print("Orden de terminación:", [pid for pid, _ in orden_terminacion])
