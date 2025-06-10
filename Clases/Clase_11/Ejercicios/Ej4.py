import os
import time

pid = os.fork()

if pid == 0:
    time.sleep(5)  
    os.execlp("ls", "ls", "-l")
else:
    os.wait()
