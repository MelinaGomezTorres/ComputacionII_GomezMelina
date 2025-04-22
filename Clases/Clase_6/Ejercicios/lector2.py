# lector2.py
fifo_path = "canal_fifo"

with open(fifo_path, "r") as fifo:
    print("Lector 2 esperando...")
    linea = fifo.readline()
    print("Lector 2 leyó:", linea.strip())
