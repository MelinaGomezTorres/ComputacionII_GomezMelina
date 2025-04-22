import os
import sys
import time

FIFO_1 = "/tmp/fifo1"
FIFO_2 = "/tmp/fifo2"

def enviar_mensaje():
    with open(FIFO_2, 'w') as fifo:
        while True:
            mensaje = input("Usuario 2, escribe un mensaje (o 'exit' para salir): ")
            if mensaje == 'exit':
                break
            fifo.write(mensaje + "\n")
            fifo.flush()

def recibir_mensaje():
    with open(FIFO_1, 'r') as fifo:
        while True:
            mensaje = fifo.readline()
            if mensaje:
                print(f"Usuario 1 dice: {mensaje.strip()}")
            time.sleep(0.1)  # Retardo mínimo para permitir la escritura sin bloquear

if __name__ == "__main__":
    # Ejecutar ambos en paralelo
    import threading

    # Crear hilos para leer y escribir
    hilo_recibir = threading.Thread(target=recibir_mensaje)
    hilo_enviar = threading.Thread(target=enviar_mensaje)

    hilo_recibir.start()
    hilo_enviar.start()

    hilo_enviar.join()
    hilo_recibir.join()

    print("Chat cerrado.")
