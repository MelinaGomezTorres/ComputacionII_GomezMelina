# lector_multi.py
import os

fifo_path = '/tmp/fifo_multi'

with open(fifo_path, 'r') as fifo:
    while True:
        line = fifo.readline().strip()
        if line:
            print(line)
