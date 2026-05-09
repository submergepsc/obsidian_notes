#!/bin/bash

echo "N,run,time" > mutex_results.csv

for n in 1 2 4 8
do
    for r in 1 2 3 4 5
    do
        output=$(./counter_mutex $n 10000000)
        time=$(echo "$output" | awk -F'time = ' '{print $2}')
        echo "$n,$r,$time" >> mutex_results.csv
        echo "N=$n run=$r time=$time"
    done
done
