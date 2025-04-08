import os

def main():

    # Creamos dos pipes: uno para padre->hijo y otro para hijo->padre
    padre_a_hijo_r, padre_a_hijo_w = os.pipe()
    hijo_a_padre_r, hijo_a_padre_w = os.pipe()

    pid = os.fork()

    if pid > 0:
        # Proceso padre
        os.close(padre_a_hijo_r)  # Cerramos lectura del primer pipe
        os.close(hijo_a_padre_w)  # Cerramos escritura del segundo pipe

        mensaje = "Hola hijo, ¿cuánto es 7 + 3?"
        os.write(padre_a_hijo_w, mensaje.encode())
        os.close(padre_a_hijo_w)  # Cerramos escritura después de enviar

        # Esperamos la respuesta del hijo
        respuesta = os.read(hijo_a_padre_r, 1024).decode()
        print(f"Padre recibió: {respuesta}")
        os.close(hijo_a_padre_r)  # Cerramos lectura

        os.wait()  # Esperamos al hijo

    else:
        # Proceso hijo
        os.close(padre_a_hijo_w)  # Cerramos escritura del primer pipe
        os.close(hijo_a_padre_r)  # Cerramos lectura del segundo pipe

        pregunta = os.read(padre_a_hijo_r, 1024).decode()
        print(f"Hijo recibió: {pregunta}")
        os.close(padre_a_hijo_r)  # Cerramos lectura

        # Procesamos y respondemos
        respuesta = "La respuesta es 10"
        os.write(hijo_a_padre_w, respuesta.encode())
        os.close(hijo_a_padre_w)  # Cerramos escritura


if __name__ == "__main__":
    main()
