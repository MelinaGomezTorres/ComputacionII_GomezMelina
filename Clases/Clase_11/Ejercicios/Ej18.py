import os

r, w = os.pipe()

pid = os.fork()

if pid == 0:  # hijo
    os.close(w)
    r = os.fdopen(r)
    print("Hijo lee:", r.readline())
else:
    os.close(r)
    w = os.fdopen(w, 'w')
    w.write("Mensaje desde padre\n")
    w.flush()
    os.wait()
