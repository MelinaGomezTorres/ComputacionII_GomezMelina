# escritor_condicional.py
import os
import time

fifo_path = '/tmp/fifo_condicional'

with open(fifo_path, 'w') as fifo:
    time.sleep(2)  # Simula una espera antes de escribir
    fifo.write('Mensaje después de espera\n')
