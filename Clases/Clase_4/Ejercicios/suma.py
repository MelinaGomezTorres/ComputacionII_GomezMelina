import os

def main():
    # Crear el pipe
    r_fd, w_fd = os.pipe()

    pid = os.fork()

    if pid > 0:
        # Proceso padre
        os.close(r_fd)  # Cerramos el descriptor de lectura
        numbers = [1, 2, 3, 4, 5]
        # Convertimos la lista a string para enviarla
        message = ','.join(map(str, numbers))
        os.write(w_fd, message.encode())
        os.close(w_fd)  # Cerramos el descriptor de escritura
        os.wait()  # Esperamos a que el hijo termine
    else:
        # Proceso hijo
        os.close(w_fd)  # Cerramos el descriptor de escritura
        read_data = os.read(r_fd, 1024).decode()
        os.close(r_fd)  # Cerramos el descriptor de lectura

        # Procesamos los datos recibidos
        numbers = list(map(int, read_data.split(',')))
        print(f"Hijo: números recibidos = {numbers}")
        print(f"Hijo: la suma es = {sum(numbers)}")


if __name__ == "__main__":
    main()
