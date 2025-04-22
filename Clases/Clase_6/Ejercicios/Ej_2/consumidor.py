# consumidor.py
import os
import time

fifo_path = '/tmp/buffer_fifo'

with open(fifo_path, 'r') as fifo:
    while True:
        line = fifo.readline().strip()
        if line:
            print(f"[{time.ctime()}] {line}")
        else:
            break
