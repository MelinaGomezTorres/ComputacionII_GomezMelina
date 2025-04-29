import signal
import time

def manejar_sigint(sig, frame):
    print("¡Recibí SIGINT (Ctrl+C)!")

# Ignorar SIGINT por 5 segundos
def ignorar_sigint():
    print("Ignorando SIGINT por 5 segundos...")
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    time.sleep(5)
    signal.signal(signal.SIGINT, manejar_sigint)
    print("Ya no se ignoran las señales.")

# Registrar el handler para SIGINT
signal.signal(signal.SIGINT, manejar_sigint)

# Ignorar SIGINT temporalmente
ignorar_sigint()

# Mantener el programa en ejecución
while True:
    time.sleep(1)
