import time
import random
import requests
from multiprocessing import Process, Queue

def worker(queue, result_queue):
    while not queue.empty():
        url = queue.get()
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        result_queue.put((url, time.time() - start_time, Process().pid))

def load_balancer(urls, num_workers):
    queue = Queue()
    result_queue = Queue()

    # Rellenar la cola de trabajo con las URLs
    for url in urls:
        queue.put(url)

    # Crear los trabajadores
    workers = []
    for _ in range(num_workers):
        p = Process(target=worker, args=(queue, result_queue))
        p.start()
        workers.append(p)

    # Esperar que todos los trabajadores terminen
    for p in workers:
        p.join()

    # Recoger y ordenar los resultados
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    results.sort(key=lambda x: x[1])  # Ordenar por tiempo de descarga

    # Mostrar los resultados
    for url, tiempo, pid in results:
        print(f"URL: {url}, Tiempo: {tiempo:.2f}s, PID: {pid}")

if __name__ == '__main__':
    urls = ["http://example.com", "http://example.org", "http://example.net"]  # Aquí pondrías URLs reales
    load_balancer(urls, num_workers=3)
