# escritor.py
import os
import time

fifo_path = '/tmp/test_fifo'

with open(fifo_path, 'w') as fifo:
    time.sleep(2)  # Simula una espera antes de escribir
    fifo.write('Hola desde el escritor\n')
