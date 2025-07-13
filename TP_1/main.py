# main.py
import multiprocessing as mp
import hashlib
import json
import random
import time
from datetime import datetime
from collections import deque

# ------------------------------
# Utilidades
# ------------------------------
def generar_dato():
    return {
        "timestamp": datetime.now().isoformat(timespec='seconds'),
        "frecuencia": random.randint(60, 180),
        "presion": [random.randint(110, 180), random.randint(70, 110)],
        "oxigeno": random.randint(90, 100)
    }

def calcular_hash(prev_hash, datos, timestamp):
    bloque_str = prev_hash + json.dumps(datos, sort_keys=True) + timestamp
    return hashlib.sha256(bloque_str.encode()).hexdigest()

# ------------------------------
# Procesos Analizadores
# ------------------------------
def analizador(tipo, pipe, queue):
    ventana = deque(maxlen=30)
    while True:
        try:
            dato = pipe.recv()
            if dato == 'FIN':
                break
            timestamp = dato['timestamp']
            if tipo == 'frecuencia':
                valor = dato['frecuencia']
            elif tipo == 'presion':
                valor = dato['presion'][0]  # sistólica
            elif tipo == 'oxigeno':
                valor = dato['oxigeno']
            else:
                continue  # tipo inválido
            ventana.append(valor)
            media = sum(ventana) / len(ventana)
            desv = (sum((x - media)**2 for x in ventana) / len(ventana)) ** 0.5
            queue.put({
                "tipo": tipo,
                "timestamp": timestamp,
                "media": round(media, 2),
                "desv": round(desv, 2)
            })
        except EOFError:
            break

# ------------------------------
# Proceso Verificador
# ------------------------------
def verificador(q_f, q_p, q_o, lock):
    cadena = []
    hash_anterior = '0' * 64
    with open("blockchain.json", "w") as f:
        f.write("[]")
    for _ in range(60):
        r_f = q_f.get()
        r_p = q_p.get()
        r_o = q_o.get()

        timestamp = r_f['timestamp']
        datos = {
            "frecuencia": {"media": r_f['media'], "desv": r_f['desv']},
            "presion": {"media": r_p['media'], "desv": r_p['desv']},
            "oxigeno": {"media": r_o['media'], "desv": r_o['desv']},
        }

        alerta = (r_f['media'] >= 200 or r_o['media'] < 90 or r_o['media'] > 100 or r_p['media'] >= 200)
        nuevo_bloque = {
            "timestamp": timestamp,
            "datos": datos,
            "alerta": alerta,
            "prev_hash": hash_anterior
        }
        hash_actual = calcular_hash(hash_anterior, datos, timestamp)
        nuevo_bloque["hash"] = hash_actual
        hash_anterior = hash_actual

        with lock:
            cadena.append(nuevo_bloque)
            with open("blockchain.json", "w") as f:
                json.dump(cadena, f, indent=2)

        print(f"Bloque #{len(cadena)} - Hash: {hash_actual[:10]}... Alerta: {alerta}")
        time.sleep(1)

# ------------------------------
# Proceso Principal
# ------------------------------
def main():
    # Pipes y Queues
    p_fq, c_fq = mp.Pipe()
    p_pq, c_pq = mp.Pipe()
    p_oq, c_oq = mp.Pipe()

    q_f = mp.Queue()
    q_p = mp.Queue()
    q_o = mp.Queue()

    lock = mp.Lock()

    # Procesos
    a_f = mp.Process(target=analizador, args=('frecuencia', c_fq, q_f))
    a_p = mp.Process(target=analizador, args=('presion', c_pq, q_p))
    a_o = mp.Process(target=analizador, args=('oxigeno', c_oq, q_o))
    verif = mp.Process(target=verificador, args=(q_f, q_p, q_o, lock))

    a_f.start()
    a_p.start()
    a_o.start()
    verif.start()

    for _ in range(60):
        dato = generar_dato()
        p_fq.send(dato)
        p_pq.send(dato)
        p_oq.send(dato)
        time.sleep(1)

    p_fq.send('FIN')
    p_pq.send('FIN')
    p_oq.send('FIN')

    p_fq.close()
    p_pq.close()
    p_oq.close()

    a_f.join()
    a_p.join()
    a_o.join()
    verif.join()

if __name__ == "__main__":
    main()
