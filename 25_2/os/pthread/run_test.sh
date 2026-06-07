#!/usr/bin/env bash
PROGRAM="./mp"         # 你的可执行文件名
SIZE=2000              # 矩阵大小
REPEAT=5               # 每个线程跑几次
OUTFILE="results.csv"  # 输出结果文件
# 先检查程序是否存在
if [ ! -x "$PROGRAM" ]; then
    echo "错误：找不到可执行文件 $PROGRAM"
    echo "请先编译，例如：gcc matrix_mul_pthread.c -lpthread -o mp"
    exit 1
fi
# 写入 CSV 表头
echo "threads,run,time_sec" > "$OUTFILE"
# 线程数 1 到 8
for threads in $(seq 1 8); do
    echo "========== 线程数: $threads =========="
    # 每个线程数跑 5 次
    for run in $(seq 1 $REPEAT); do
        echo "运行中: threads=$threads, run=$run"
        # 执行程序并抓取输出
        output=$($PROGRAM $SIZE $threads)
        # 从输出中提取最后的时间数字
        # 例如匹配：Execution time:43.286 sec
        time_sec=$(echo "$output" | grep "Execution time" | sed -E 's/.*Execution time:[[:space:]]*([0-9.]+)[[:space:]]*sec.*/\1/')
        # 如果没提取到，报错并打印原输出
        if [ -z "$time_sec" ]; then
            echo "提取运行时间失败，原始输出如下："
            echo "$output"
            exit 1
        fi
        echo "$threads,$run,$time_sec" >> "$OUTFILE"
    done
done
echo "全部完成，结果已保存到 $OUTFILE"