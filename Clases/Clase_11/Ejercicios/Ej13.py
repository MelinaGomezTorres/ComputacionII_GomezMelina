import os
import time

for _ in range(2):
    pid = os.fork()
    if pid == 0:
        print(f"[HIJO] PID: {os.getpid()} PPID: {os.getppid()}")
        time.sleep(10)
        os._exit(0)

time.sleep(15)
