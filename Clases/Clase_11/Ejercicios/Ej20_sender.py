import os
import signal
import time
import sys

if len(sys.argv) != 2:
    print("Uso: python3 Ej20_sender.py [PID]")
    sys.exit(1)

pid = int(sys.argv[1])

for _ in range(5):
    os.kill(pid, signal.SIGUSR1)
    time.sleep(1)
    os.kill(pid, signal.SIGUSR2)
    time.sleep(1)
