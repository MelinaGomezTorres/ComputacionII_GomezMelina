import hashlib
import json

def calcular_hash(prev_hash, datos, timestamp):
    bloque_str = prev_hash + json.dumps(datos, sort_keys=True) + timestamp
    return hashlib.sha256(bloque_str.encode()).hexdigest()

def verificar_cadena():
    try:
        with open("blockchain.json", "r") as f:
            cadena = json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo blockchain.json")
        return

    bloques_invalidos = 0
    alertas = 0
    total = len(cadena)

    suma_f = suma_p = suma_o = 0

    for i, bloque in enumerate(cadena):
        timestamp = bloque["timestamp"]
        datos = bloque["datos"]
        hash_prev = bloque["prev_hash"]
        hash_esp = calcular_hash(hash_prev, datos, timestamp)
        if hash_esp != bloque["hash"]:
            print(f"[!] Bloque #{i + 1} CORRUPTO")
            bloques_invalidos += 1

        if bloque["alerta"]:
            alertas += 1

        suma_f += datos["frecuencia"]["media"]
        suma_p += datos["presion"]["media"]
        suma_o += datos["oxigeno"]["media"]

    prom_f = round(suma_f / total, 2)
    prom_p = round(suma_p / total, 2)
    prom_o = round(suma_o / total, 2)

    with open("reporte.txt", "w") as r:
        r.write(f"Cantidad total de bloques: {total}\n")
        r.write(f"Bloques con alertas: {alertas}\n")
        r.write(f"Bloques corruptos: {bloques_invalidos}\n")
        r.write(f"Promedio Frecuencia: {prom_f}\n")
        r.write(f"Promedio Presion: {prom_p}\n")
        r.write(f"Promedio Oxigeno: {prom_o}\n")

    print("[✓] Verificación completa. Ver reporte.txt.")

if __name__ == "__main__":
    verificar_cadena()
