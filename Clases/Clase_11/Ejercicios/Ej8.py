from multiprocessing import Process, Value, Lock

def incrementar(contador, lock=None):
    for _ in range(100000):
        if lock:
            with lock:
                contador.value += 1
        else:
            contador.value += 1

def correr_sin_lock():
    c = Value('i', 0)
    p1 = Process(target=incrementar, args=(c,))
    p2 = Process(target=incrementar, args=(c,))
    p1.start(); p2.start()
    p1.join(); p2.join()
    print("Sin Lock:", c.value)

def correr_con_lock():
    c = Value('i', 0)
    lock = Lock()
    p1 = Process(target=incrementar, args=(c, lock))
    p2 = Process(target=incrementar, args=(c, lock))
    p1.start(); p2.start()
    p1.join(); p2.join()
    print("Con Lock:", c.value)

if __name__ == "__main__":
    correr_sin_lock()
    correr_con_lock()
