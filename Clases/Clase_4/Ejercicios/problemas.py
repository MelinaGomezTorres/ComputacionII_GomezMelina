import os
import time

def main():
    # Variable compartida antes del fork
    message = "Mensaje inicial"

    pid = os.fork()

    if pid == 0:
        # Proceso hijo
        print(f"Hijo: PID {os.getpid()} - Padre PID {os.getppid()}")
        time.sleep(1)  # Espera para que el padre modifique el mensaje
        print(f"Hijo lee el mensaje: {message}")
        message = "Mensaje modificado por el hijo"
        print(f"Hijo cambia el mensaje a: {message}")
    else:
        # Proceso padre
        print(f"Padre: PID {os.getpid()} - Hijo PID {pid}")
        message = "Mensaje modificado por el padre"
        print(f"Padre cambia el mensaje a: {message}")
        time.sleep(2)  # Espera para que el hijo termine
        print(f"Padre lee el mensaje: {message}")

if __name__ == "__main__":
    main()

'''
Problemas:

Memoria no compartida: aunque message está antes del fork(), los cambios en el hijo no afectan al padre y viceversa.

Condiciones de carrera: si no pones sleep(), el orden de ejecución puede ser caótico.

Comunicación limitada: no hay un canal real de comunicación, solo variables locales que no se sincronizan.
'''
