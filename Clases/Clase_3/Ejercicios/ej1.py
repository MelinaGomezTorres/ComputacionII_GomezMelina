import os
import time
import sys

def main():
    pid1 = os.fork()
    
    if pid1 == 0:
        # Primer hijo
        time.sleep(2)  # Se duerme 2 segundos
        print(f"Soy el hijo 1, mi PID es {os.getpid()}, y el PID de mi padre es {os.getppid()}")
        sys.exit(0)
    
    pid2 = os.fork()
    
    if pid2 == 0:
        # Segundo hijo
        time.sleep(3)  # Se duerme 3 segundos
        print(f"Soy el hijo 2, mi PID es {os.getpid()}, y el PID de mi padre es {os.getppid()}")
        sys.exit(0)

    # Proceso padre
    time.sleep(0)  # No espera a los hijos, termina antes
    print(f"Soy el padre, mi PID es {os.getpid()}, y estoy terminando")
    sys.exit(0)

if __name__ == "__main__":
    main()

"""
Aquí el que termina primero es el padre, ya que no tiene retraso.
Luego le sigue el hijo 1 después de 2 segundos y el hijo 2 después de 3 segundos.

Los hijos quedan como huérfanos porque el padre termina antes que ellos.
El sistema operativo asigna el proceso init (PID 1) como su nuevo padre, 
por lo que el PID del padre cambia a 1.

Puede haber procesos huérfanos, pero nunca quedan sin supervisión; 
el sistema siempre los reasigna.

Si el hijo 1 terminara antes que el padre, no quedaría huérfano.
Sin embargo, si el hijo 2 tiene un retraso mayor que el padre, sí quedará huérfano.

Documentación oficial: https://docs.python.org/3/library/os.html

¿Qué cambia con wait()?
- El padre esperará a que los hijos terminen antes de salir.
- Los hijos mantendrán su PPID original porque el padre seguirá vivo hasta el final.
- El orden de las impresiones será predecible:
  - Hijo 1 imprimirá su mensaje después de 2 segundos.
  - Hijo 2 imprimirá su mensaje después de 3 segundos.
  - El padre imprimirá su mensaje al final, después de que ambos hijos terminen.

Sin wait(), el padre podría terminar antes que los hijos, haciéndolos huérfanos.
Con wait(), el padre espera a los hijos antes de finalizar.
"""




