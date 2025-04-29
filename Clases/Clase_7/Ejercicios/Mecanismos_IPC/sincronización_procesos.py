import multiprocessing

# Recurso compartido
contador = multiprocessing.Value('i', 0)

# Semáforo
semaforo = multiprocessing.Semaphore(1)

# Función que incrementa el contador
def incrementar():
    for _ in range(1000):
        semaforo.acquire()  # Adquirir semáforo
        contador.value += 1
        semaforo.release()  # Liberar semáforo

# Crear procesos
proceso1 = multiprocessing.Process(target=incrementar)
proceso2 = multiprocessing.Process(target=incrementar)

# Iniciar procesos
proceso1.start()
proceso2.start()

# Esperar a que ambos procesos terminen
proceso1.join()
proceso2.join()

# Imprimir resultado final
print(f"Valor final del contador: {contador.value}")
