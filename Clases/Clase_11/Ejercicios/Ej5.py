import os

r, w = os.pipe()

pid = os.fork()

if pid == 0:
    os.close(r)
    msg = b"Hola padre desde el hijo!"
    os.write(w, msg)
    os.close(w)
    os._exit(0)
else:
    os.close(w)
    mensaje = os.read(r, 1024)
    print(f"[PADRE] Recibido: {mensaje.decode()}")
    os.wait()
