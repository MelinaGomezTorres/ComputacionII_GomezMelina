import os
import time

pid = os.fork()

if pid == 0:
    time.sleep(10)
    print(f"[HIJO] Mi nuevo PPID es {os.getppid()}")
else:
    print(f"[PADRE] Finaliza. PID: {os.getpid()}")
    os._exit(0)
