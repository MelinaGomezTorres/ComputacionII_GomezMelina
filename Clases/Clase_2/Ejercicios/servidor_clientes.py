import os
import time

# Función que simula la atención de un cliente
def handle_client(client_id):
    print(f"Atendiendo cliente {client_id} (PID: {os.getpid()})")
    time.sleep(2)  # Simula el tiempo que tarda en atender al cliente
    print(f"Cliente {client_id} atendido.")

# El servidor atiende 3 clientes en procesos separados
for client in range(3):
    pid = os.fork()  # Crear un nuevo proceso para cada cliente
    if pid == 0:  # Proceso hijo
        handle_client(client)
        os._exit(0)  # Termina el proceso hijo después de atender al cliente

# El proceso padre espera que los 3 procesos hijos terminen
for _ in range(3):  
    os.wait()

print("Todos los clientes fueron atendidos.")
