# lector1.py
fifo_path = "canal_fifo"

with open(fifo_path, "r") as fifo:
    print("Lector 1 esperando...")
    linea = fifo.readline()
    print("Lector 1 leyó:", linea.strip())
