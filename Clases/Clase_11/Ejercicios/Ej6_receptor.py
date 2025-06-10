with open("/tmp/mi_fifo", "r") as fifo:
    for line in fifo:
        print(f"[RECEPTOR] Recibido: {line.strip()}")
