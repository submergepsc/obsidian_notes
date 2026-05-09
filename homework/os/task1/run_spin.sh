#!/bin/bash

M=10000000
REPEAT=5
OUTFILE="task31_spin_results.csv"

echo "program,threads,run,time_sec" > "$OUTFILE"

for n in 1 2 4 8 16; do
  for r in $(seq 1 $REPEAT); do
    echo "Running counter_spin, N=$n, run=$r"

    output=$(./counter_spin "$n" "$M")
    echo "$output"

    time=$(echo "$output" | grep -Eo 'time = [0-9]+\.[0-9]+' | grep -Eo '[0-9]+\.[0-9]+')

    echo "counter_spin,$n,$r,$time" >> "$OUTFILE"
  done
done

echo "Done. Results saved to $OUTFILE"

