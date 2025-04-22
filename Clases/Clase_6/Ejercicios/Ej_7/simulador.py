# simulador.py
import os
import time
import random
from datetime import datetime

fifo_path = '/tmp/temperatura'

with open(fifo_path, 'w') as fifo:
    while True:
        temp = round(random.uniform(20, 30), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fifo.write(f"{timestamp} - {temp}\n")
        fifo.flush()
        time.sleep(1)
