import os
import sys

def main():
    p2c_r, p2c_w = os.pipe()  # Padre a hijo
    c2p_r, c2p_w = os.pipe()  # Hijo a padre

    pid = os.fork()

    if pid > 0:
        # Proceso padre
        os.close(p2c_r)
        os.close(c2p_w)

        while True:
            operation = input("Ingrese una operación matemática (o 'salir' para terminar): ")
            os.write(p2c_w, (operation + "\n").encode())

            if operation.lower() == "salir":
                break

            response = os.read(c2p_r, 1024).decode()
            print(f"Padre recibió:\n{response}")

        os.close(p2c_w)
        os.close(c2p_r)
        os.waitpid(pid, 0)

    else:
        # Proceso hijo
        os.close(p2c_w)
        os.close(c2p_r)

        while True:
            operation = b""
            while not operation.endswith(b"\n"):
                chunk = os.read(p2c_r, 1)
                if not chunk:
                    break  # EOF
                operation += chunk

            operation = operation.decode().strip()

            if operation.lower() == "salir" or not operation:
                break

            try:
                result = str(eval(operation))
                status = "Operación completada correctamente"
            except Exception as e:
                result = f"Error: {e}"
                status = "Operación fallida"

            full_response = f"Resultado: {result}\nEstado: {status}"
            os.write(c2p_w, full_response.encode())

        os.close(p2c_r)
        os.close(c2p_w)
        sys.exit(0)


if __name__ == "__main__":
    main()
