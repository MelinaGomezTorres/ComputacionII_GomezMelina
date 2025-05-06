import time
import multiprocessing

def enviar_datos(pipe, data):
    for num in data:
        pipe.send(num)
    pipe.send(None)  # Fin de la transmisión

def recibir_datos(pipe):
    data = []
    while True:
        num = pipe.recv()
        if num is None:
            break
        data.append(num)
    return data

if __name__ == '__main__':
    data = list(range(1000000))
    
    # Método 1: Pipe
    pipe = multiprocessing.Pipe()
    start = time.time()
    p1 = multiprocessing.Process(target=enviar_datos, args=(pipe[0], data))
    p2 = multiprocessing.Process(target=recibir_datos, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Tiempo con Pipe: {time.time() - start:.4f} segundos")
    
    # Métodos adicionales como Queue y Manager().list seguirían la misma estructura
