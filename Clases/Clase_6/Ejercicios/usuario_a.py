# usuario_a.py
import threading

def leer():
    with open("chat_b_a", "r") as f:
        for linea in f:
            print("B:", linea.strip())

def escribir():
    while True:
        mensaje = input("A: ")
        with open("chat_a_b", "w") as f:
            f.write(mensaje + "\n")

threading.Thread(target=leer, daemon=True).start()
escribir()
