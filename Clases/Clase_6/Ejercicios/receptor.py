# receptor.py
fifo_path = "chat_fifo"

print("Chat Receptor (esperando mensajes...)")
while True:
    with open(fifo_path, "r") as fifo:
        for linea in fifo:
            print(">>", linea.strip())
