# escritor.py
import os
import time

fifo_path = "canal_fifo"

with open(fifo_path, "w") as fifo:
    print("Escribiendo en el FIFO...")
    fifo.write("Hola desde el escritor\n")
    print("Mensaje enviado.")
