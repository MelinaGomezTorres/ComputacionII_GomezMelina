# lector.py
import os

fifo_path = '/tmp/test_fifo'

with open(fifo_path, 'r') as fifo:
    data = fifo.read()
    print(f"Recibido: {data}")
