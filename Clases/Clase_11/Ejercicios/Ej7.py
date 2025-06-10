from multiprocessing import Process, Lock
from datetime import datetime
import os

def escribir_log(lock):
    with lock:
        with open("log.txt", "a") as f:
            f.write(f"PID: {os.getpid()} - {datetime.now()}\n")

if __name__ == "__main__":
    lock = Lock()
    procesos = [Process(target=escribir_log, args=(lock,)) for _ in range(4)]

    for p in procesos: p.start()
    for p in procesos: p.join()
