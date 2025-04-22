# lector.py
fifo_path = "canal_fifo"

with open(fifo_path, "r") as fifo:
    print("Esperando mensaje...")
    mensaje = fifo.readline()
    print("Mensaje recibido:", mensaje)
