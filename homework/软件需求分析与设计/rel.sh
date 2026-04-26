#!/bin/bash

# 检查是否提供了文件路径
if [ $# -eq 0 ]; then
  echo "用法: $0 文件路径"
  exit 1
fi

# 文件路径
file=$1

# 检查文件是否存在
if [ ! -f "$file" ]; then
  echo "文件不存在: $file"
  exit 1
fi

# 删除所有空行
sed -i '/^$/d' "$file"

echo "已删除文件中的所有空行: $file"
