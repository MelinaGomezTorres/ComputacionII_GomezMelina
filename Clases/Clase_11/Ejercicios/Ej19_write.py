import multiprocessing
import time
import os

def escribir():
    with open("concurrente.txt", "a") as f:
        for _ in range(5):
            f.write(f"PID {os.getpid()} escribe\n")
            time.sleep(0.1)

if __name__ == "__main__":
    procesos = [multiprocessing.Process(target=escribir) for _ in range(5)]
    for p in procesos: p.start()
    for p in procesos: p.join()
