import signal
import os
import time

def handler_usr1(signum, frame):
    print("Recibida SIGUSR1")

def handler_usr2(signum, frame):
    print("Recibida SIGUSR2")

signal.signal(signal.SIGUSR1, handler_usr1)
signal.signal(signal.SIGUSR2, handler_usr2)

print(f"Esperando señales... PID: {os.getpid()}")

while True:
    signal.pause()
