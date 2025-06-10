#!/bin/bash

declare -A estados
echo "PID  PPID  Nombre          Estado"
for pid in /proc/[0-9]*; do
    p=${pid##*/}
    if [[ -r $pid/status ]]; then
        nombre=$(grep "^Name:" $pid/status | awk '{print $2}')
        ppid=$(grep "^PPid:" $pid/status | awk '{print $2}')
        estado=$(grep "^State:" $pid/status | awk '{print $2}')
        echo "$p  $ppid  $nombre  $estado"
        estados["$estado"]=$(( ${estados["$estado"]} + 1 ))
    fi
done

echo -e "\nResumen de estados:"
for e in "${!estados[@]}"; do
    echo "$e : ${estados[$e]}"
done
