#!/bin/bash
SIZE=2000
RUNS=5
echo "threads,run,time_sec" > results.csv
for t in {1..8}
do
  for r in $(seq 1 $RUNS)
  do  
    # 运行程序并提取时间
    output=$(go run matrix.go -s $SIZE -n $t)
    # 提取 Time taken 数值（单位秒）
    time=$(echo "$output" | grep "Time taken" | awk '{print $NF}' | sed 's/s//')
    echo "$t,$r,$time" >> results.csv
    echo "threads=$t run=$r time=$time"
  done
done