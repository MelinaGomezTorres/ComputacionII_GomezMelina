# emisor.py
fifo_path = "chat_fifo"

print("Chat Emisor (CTRL+C para salir)")
while True:
    mensaje = input("Tú: ")
    with open(fifo_path, "w") as fifo:
        fifo.write(mensaje + "\n")
