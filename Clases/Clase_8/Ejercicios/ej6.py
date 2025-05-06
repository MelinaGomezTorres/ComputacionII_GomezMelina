import time
import multiprocessing

def actualizar(cronometro):
    while True:
        time.sleep(1)
        with cronometro.get_lock():
            cronometro.value = time.time()

def verificar(cronometro):
    last_time = None
    while True:
        time.sleep(0.5)
        with cronometro.get_lock():
            current_time = cronometro.value
            if last_time is not None and current_time - last_time > 1:
                print(f"Incoherencia detectada: Salto de más de 1 segundo.")
            last_time = current_time

if __name__ == '__main__':
    cronometro = multiprocessing.Value('d', time.time())  # 'd' tipo de dato double
    procesos = []
    
    # Iniciar 3 procesos que actualizan el cronómetro
    for _ in range(3):
        p = multiprocessing.Process(target=actualizar, args=(cronometro,))
        p.start()
        procesos.append(p)

    # Iniciar el proceso que verifica el cronómetro
    p_verificar = multiprocessing.Process(target=verificar, args=(cronometro,))
    p_verificar.start()

    # Esperar que los procesos terminen (no se va a hacer porque es un ejemplo infinito)
    for p in procesos:
        p.join()
    p_verificar.join()
