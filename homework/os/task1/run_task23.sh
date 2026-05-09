#!/bin/bash

M=10000000
REPEAT=5
OUTFILE="task23_results.csv"

PROGRAMS=(
  "counter_mutex"
  "counter_batched"
  "counter_atomic_relaxed"
  "counter_atomic_seqcst"
)

THREADS=(1 2 4 8 16)

echo "program,threads,run,time_sec" > "$OUTFILE"

for prog in "${PROGRAMS[@]}"; do
  for n in "${THREADS[@]}"; do
    for r in $(seq 1 $REPEAT); do
      echo "Running $prog, N=$n, run=$r"

      output=$(./"$prog" "$n" "$M")

      echo "$output"

      time=$(echo "$output" | grep -Eo '[0-9]+\.[0-9]+' | tail -n 1)

      echo "$prog,$n,$r,$time" >> "$OUTFILE"
    done
  done
done

echo "Done. Results saved to $OUTFILE"
