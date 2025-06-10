import argparse
import os
import time
import random

parser = argparse.ArgumentParser(description="Crea procesos hijos.")
parser.add_argument("--num", type=int, required=True, help="Cantidad de procesos hijos a crear")
parser.add_argument("--verbose", action="store_true", help="Activar mensajes detallados")
args = parser.parse_args()

if args.verbose:
    print(f"[PADRE] PID: {os.getpid()}")

children = []

for i in range(args.num):
    pid = os.fork()
    if pid == 0:
        # Hijo
        t = random.randint(1, 5)
        if args.verbose:
            print(f"[HIJO {os.getpid()}] Dormirá {t} segundos")
        time.sleep(t)
        os._exit(0)
    else:
        children.append(pid)

# Esperar a que todos los hijos terminen
for pid in children:
    os.waitpid(pid, 0)

print("\nJerarquía de procesos:")
os.system(f"pstree -p {os.getpid()}")
