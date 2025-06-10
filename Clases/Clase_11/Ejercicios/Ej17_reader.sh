#!/bin/bash
fifo="/tmp/mi_fifo"
[[ ! -p $fifo ]] && mkfifo $fifo

while true; do
    if read line < $fifo; then
        echo "Leído: $line"
    fi
done
