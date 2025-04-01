import os
import sys

def crear_hijo(n):
    pid = os.fork()
    
    if pid == 0:  # Código del hijo
        print(f"Hijo {n}: PID = {os.getpid()} (Hijo de {os.getppid()})")
        if n < 5:  # Solo los primeros 4 hijos crean otro hijo
            crear_hijo(n + 1)
        sys.exit(0)
    else:
        os.waitpid(pid, 0)  # Esperar a que el hijo termine antes de seguir

def main():
    print(f"Proceso padre PID = {os.getpid()}")
    crear_hijo(1)  # Inicia la creación de hijos en cascada
    print("Todos los hijos han terminado.")

if __name__ == "__main__":
    main()

"""
¿Cómo funciona?
El proceso padre inicializa la cadena de procesos y muestra su PID.

Cada hijo se crea con os.fork() y solo los primeros 4 hijos crean otro hijo.

Cada hijo imprime su propio PID y el PID de su padre.

Cada padre espera a su hijo antes de terminar (os.waitpid(pid, 0)) para evitar procesos zombis.

El último hijo no genera más hijos y termina inmediatamente.
"""



