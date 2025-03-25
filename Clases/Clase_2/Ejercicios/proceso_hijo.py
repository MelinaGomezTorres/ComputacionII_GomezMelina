import os

# Crear 3 procesos hijos
for _ in range(3):
    pid = os.fork()
    if pid == 0:  # Proceso hijo
        print(f"Hijo: PID {os.getpid()}, Padre: {os.getppid()}")
        os._exit(0)

# El padre espera a los 3 procesos hijos
for _ in range(3):
    os.wait()
