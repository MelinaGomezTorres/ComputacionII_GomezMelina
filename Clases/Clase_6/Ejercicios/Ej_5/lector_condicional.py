# lector_condicional.py
import os
import time

fifo_path = '/tmp/fifo_condicional'

attempts = 0
while attempts < 5:
    try:
        with open(fifo_path, 'r') as fifo:
            data = fifo.read()
            print(f"Recibido: {data}")
            break
    except BlockingIOError:
        print("FIFO vacío, reintentando...")
        attempts += 1
        time.sleep(1)
if attempts == 5:
    print("No se pudo leer del FIFO después de 5 intentos.")
