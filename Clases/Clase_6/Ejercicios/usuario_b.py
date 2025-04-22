# usuario_b.py
import threading

def leer():
    with open("chat_a_b", "r") as f:
        for linea in f:
            print("A:", linea.strip())

def escribir():
    while True:
        mensaje = input("B: ")
        with open("chat_b_a", "w") as f:
            f.write(mensaje + "\n")

threading.Thread(target=leer, daemon=True).start()
escribir()
