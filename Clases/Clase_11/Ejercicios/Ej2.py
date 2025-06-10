import os
import time

pid = os.fork()

if pid == 0:
    print(f"[HIJO] PID: {os.getpid()} terminó.")
    os._exit(0)
else:
    print(f"[PADRE] PID: {os.getpid()} no recogerá a {pid} por 10s.")
    time.sleep(10)
    os.waitpid(pid, 0)
