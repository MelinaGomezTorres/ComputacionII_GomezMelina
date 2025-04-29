import signal
import threading
import time

# Variable global y lock
contador = 30
lock = threading.Lock()

# Flags para controlar la pausa y reanudación
pausado = False

def manejador(sig, frame):
    global pausado
    if sig == signal.SIGUSR1:
        pausado = True
        print("Contador pausado.")
    elif sig == signal.SIGUSR2:
        pausado = False
        print("Contador reanudado.")

def contar_regresivo():
    global contador
    while contador > 0:
        if pausado:
            time.sleep(1)
            continue
        with lock:
            print(f"Contando: {contador}")
            contador -= 1
        time.sleep(1)
    print("Cuenta regresiva finalizada.")

# Registrar los handlers
signal.signal(signal.SIGUSR1, manejador)
signal.signal(signal.SIGUSR2, manejador)

# Crear hilo para la cuenta regresiva
hilo = threading.Thread(target=contar_regresivo)
hilo.start()

# Esperar a que el hilo termine
hilo.join()