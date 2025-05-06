import random
import time
import multiprocessing

def cajero(balance, lock):
    retries = 0
    while retries < 5:
        with lock:
            # Simulamos una operación de retiro o depósito
            operacion = random.choice(['retiro', 'depósito'])
            monto = random.randint(1, 100)
            if operacion == 'retiro' and balance.value >= monto:
                balance.value -= monto
                print(f"Cajero {multiprocessing.current_process().pid} realizó un {operacion} de {monto}. Balance: {balance.value}")
            elif operacion == 'depósito':
                balance.value += monto
                print(f"Cajero {multiprocessing.current_process().pid} realizó un {operacion} de {monto}. Balance: {balance.value}")
        retries += 1
        time.sleep(2**retries)  # Back-off exponencial

if __name__ == '__main__':
    balance = multiprocessing.Value('d', 1000.0)  # Balance inicial de 1000
    lock = multiprocessing.Lock()
    procesos = []
    for _ in range(5):
        p = multiprocessing.Process(target=cajero, args=(balance, lock))
        p.start()
        procesos.append(p)
    
    for p in procesos:
        p.join()

    print("Simulación terminada.")
