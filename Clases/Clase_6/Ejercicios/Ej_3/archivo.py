# archivo.py
import os

fifo_path = '/tmp/fifo_archivo'
output_path = 'output.txt'

with open(fifo_path, 'r') as fifo, open(output_path, 'w') as file:
    while True:
        line = fifo.readline().strip()
        if line == 'exit':
            break
        file.write(line + '\n')
