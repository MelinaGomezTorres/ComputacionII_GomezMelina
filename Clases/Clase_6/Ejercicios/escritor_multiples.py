# escritor_multiples.py
import time

fifo_path = "canal_fifo"

with open(fifo_path, "w") as fifo:
    print("Escribiendo 3 líneas...")
    for i in range(3):
        mensaje = f"Mensaje {i+1}\n"
        fifo.write(mensaje)
        fifo.flush()
        print("Enviado:", mensaje.strip())
        time.sleep(1)
