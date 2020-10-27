#!/bin/bash
python3 tarea4.py>>resultados.txt
for ((i=0;i<30;i++))
do
    python3 tarea4.py>>resultados.txt
done
