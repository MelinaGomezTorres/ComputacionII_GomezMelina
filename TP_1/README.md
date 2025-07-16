# Sistema Concurrente de Análisis Biométrico con Blockchain Local

## Ejecución

1. Ejecutar el sistema principal:

```
python3 main.py
```

2. Verificar la cadena y generar el reporte:

```
python3 verificar_cadena.py
```

## Archivos

- `main.py`: Generación, análisis, verificación y escritura de bloques.
- `verificar_cadena.py`: Verifica integridad de la cadena y genera reporte.
- `blockchain.json`: Se crea automáticamente, al ejecutar main.py.
- `reporte.txt`: Se crea al verificar la cadena.

## Requisitos

- Python ≥ 3.9
- Módulos estándar: `multiprocessing`, `hashlib`, `json`, `random`, `datetime`, `time`, `collections`

## ¿Por qué está hecho así el código? (Explicación personal)

El objetivo fue simular un sistema que recibe señales biométricas en tiempo real, generando una muestra por segundo con frecuencia cardíaca, presión arterial y oxígeno. El enfoque del trabajo fue pensar cómo funcionaría un sistema real que necesita procesar estos datos rápido y de forma segura. Por eso, el programa está dividido en procesos: cada uno tiene una tarea clara y trabaja en paralelo con los otros, aprovechando mejor los recursos del sistema.

Usé `multiprocessing` porque permite dividir el trabajo en procesos reales (no solo hilos), evitando cuellos de botella si una señal tarda más en procesarse que otra. Así, los cálculos de frecuencia, presión y oxígeno se hacen al mismo tiempo, simulando el comportamiento de sensores en tiempo real.

La comunicación entre procesos se resolvió con `Pipe` y `Queue`: `Pipe` para enviar datos desde el proceso principal a los analizadores, y `Queue` para que estos manden los resultados al verificador sin depender del orden.

Cada proceso mantiene una ventana de los últimos 30 valores para calcular promedios y desviaciones más estables, como se hace en medicina, y no depender de un solo dato puntual.

El verificador decide si los valores están dentro de lo normal y guarda todo en bloques tipo blockchain, donde cada bloque resume los datos del momento y se encadena con el anterior mediante un hash. Así, si alguien modifica un dato, se rompe la cadena y se detecta.

Por último, un script (`verificar_cadena.py`) revisa la cadena y genera un resumen con estadísticas. Con eso se completa el ciclo del sistema: generar, procesar, validar, guardar y reportar.
