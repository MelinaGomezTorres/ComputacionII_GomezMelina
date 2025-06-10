from multiprocessing import Process, Semaphore
import time, os, random

def zona_critica(sem):
    with sem:
        print(f"PID {os.getpid()} entra")
        time.sleep(random.randint(1, 3))
        print(f"PID {os.getpid()} sale")

if __name__ == "__main__":
    sem = Semaphore(3)
    procesos = [Process(target=zona_critica, args=(sem,)) for _ in range(10)]

    for p in procesos: p.start()
    for p in procesos: p.join()
