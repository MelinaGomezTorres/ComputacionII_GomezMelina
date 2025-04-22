# usuario_a.py
import os
import threading
from datetime import datetime

fifo_write = '/tmp/chat_a'
fifo_read = '/tmp/chat_b'

def leer():
    with open(fifo_read, 'r') as fifo:
        while True:
            msg = fifo.readline().strip()
            if msg:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Usuario B: {msg}")
            if msg == '/exit':
                break

def escribir():
    with open(fifo_write, 'w') as fifo:
        while True:
            msg = input("Tú: ")
            fifo.write(msg + '\n')
            fifo.flush()
            if msg == '/exit':
                break

threading.Thread(target=leer).start()
escribir()
