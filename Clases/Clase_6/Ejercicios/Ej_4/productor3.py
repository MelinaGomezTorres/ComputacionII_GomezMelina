# productor3.py
import os
import time

fifo_path = '/tmp/fifo_multi'

with open(fifo_path, 'w') as fifo:
    while True:
        fifo.write("Soy productor 3\n")
        time.sleep(1)
