# enviar.py
import os

fifo_path = '/tmp/fifo_archivo'

with open(fifo_path, 'w') as fifo:
    while True:
        line = input("Escribe algo (escribe 'exit' para salir): ")
        fifo.write(line + '\n')
        if line == 'exit':
            break
