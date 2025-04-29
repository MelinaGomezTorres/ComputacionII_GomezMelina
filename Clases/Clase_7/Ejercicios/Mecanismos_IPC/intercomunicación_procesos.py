import os

# Crear una pipe
pipe_lee, pipe_escribe = os.pipe()

pid = os.fork()

if pid == 0:  # Proceso hijo
    os.close(pipe_escribe)  # Cerrar la escritura
    mensaje = os.read(pipe_lee, 1024).decode()  # Leer mensaje del padre
    print(f"Proceso hijo recibió el mensaje: {mensaje}")
    mensaje_modificado = mensaje.upper()  # Modificar el mensaje
    print(f"Proceso hijo devuelve el mensaje modificado: {mensaje_modificado}")
    os.write(pipe_lee, mensaje_modificado.encode())  # Enviar respuesta al padre
else:  # Proceso padre
    os.close(pipe_lee)  # Cerrar la lectura
    mensaje = "¡Hola desde el padre!"
    os.write(pipe_escribe, mensaje.encode())  # Enviar mensaje al hijo
    os.close(pipe_escribe)
    
    os.wait()  # Esperar que termine el hijo
    
    pipe_lee, pipe_escribe = os.pipe()  # Crear una nueva pipe para leer la respuesta
    respuesta = os.read(pipe_lee, 1024).decode()
    print(f"Proceso padre recibió la respuesta: {respuesta}")
