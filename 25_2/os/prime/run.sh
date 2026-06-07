#!/bin/bash
# 输出文件
OUTPUT="results_prime.csv"
# 初始化文件
echo "threads,run,time_sec" > $OUTPUT
# 参数
NUM=20000
echo "Start benchmark..."
# 线程数 1~8
for t in {1..8}
do
  echo "Testing threads = $t"
  # 每个线程跑 5 次
  for r in {1..5}
  do
    echo "  Run $r..."
    # 执行程序并抓取时间
    result=$(go run prime.go -num $NUM -n $t)
    # 提取时间（Time taken: xxx）
    time=$(echo "$result" | grep "Time taken" | awk '{print $NF}')
    # 去掉单位（s 或 ms 或 ns）
    # 转成秒（统一单位，方便画图）
    if [[ $time == *"ns" ]]; then
      time_sec=$(echo "$time" | sed 's/ns//' | awk '{printf "%.6f", $1/1000000000}')
    elif [[ $time == *"µs" ]]; then
      time_sec=$(echo "$time" | sed 's/µs//' | awk '{printf "%.6f", $1/1000000}')
    elif [[ $time == *"ms" ]]; then
      time_sec=$(echo "$time" | sed 's/ms//' | awk '{printf "%.6f", $1/1000}')
    elif [[ $time == *"s" ]]; then
      time_sec=$(echo "$time" | sed 's/s//' )
    else
      time_sec=$time
    fi
    # 写入 CSV
    echo "$t,$r,$time_sec" >> $OUTPUT
  done
done
echo "Done! Results saved to $OUTPUT"