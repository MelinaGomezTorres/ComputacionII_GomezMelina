#!/bin/bash
fifo="/tmp/mi_fifo"
[[ ! -p $fifo ]] && mkfifo $fifo

for i in {1..10}; do
    echo "Mensaje $i" > $fifo
    sleep 1
done
