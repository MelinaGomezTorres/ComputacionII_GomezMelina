# monitor.py
import os

fifo_path = '/tmp/temperatura'
log_path = 'log_temperatura.txt'

with open(fifo_path, 'r') as fifo, open(log_path, 'a') as log:
    for line in fifo:
        line = line.strip()
        print(f"Temperatura: {line}")
        log.write(line + '\n')
        temp = float(line.split('-')[-1])
        if temp > 28:
            print("⚠️  Alerta: temperatura alta!")
