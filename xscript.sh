#!/bin/sh

mkdir output
mkdir graphs

taskset -c 0 python3 ./when-to-surrender/main.py F4 k-iter 100 150 200 715 f4-k-iter > output/f4-k-iter.txt &
taskset -c 1 python3 ./when-to-surrender/main.py F4 sd 0.15 0.14 0.13 0.12 f4-sd > output/f4-sd.txt &
taskset -c 2 python3 ./when-to-surrender/main.py F4 best-worst 0.125 0.1 0.075 0.05 f4-best-worst > output/f4-best-worst.txt &
taskset -c 3 python3 ./when-to-surrender/main.py F4 variance 0.00055 0.00045 0.0004 0.00035 f4-variance > output/f4-variance.txt & 

taskset -c 4 python3 ./when-to-surrender/main.py F5 k-iter 150 300 450 715 f5-k-iter > output/f5-k-iter.txt &
taskset -c 5 python3 ./when-to-surrender/main.py F5 sd 0.017 0.015 0.013 0.012 f5-sd > output/f5-sd.txt &
taskset -c 6 python3 ./when-to-surrender/main.py F5 best-worst 1.0 0.9 0.8 0.7 f5-best-worst > output/f5-best-worst.txt &
taskset -c 7 python3 ./when-to-surrender/main.py F5 variance 0.15 0.1 0.075 0.05  f5-variance > output/f5-variance.txt &

taskset -c 0 python3 ./when-to-surrender/main.py F6 k-iter 50 75 100 715 f6-k-iter > output/f6-k-iter.txt &
taskset -c 1 python3 ./when-to-surrender/main.py F6 sd 0.25 0.2 0.175 0.1 f6-sd > output/f6-sd.txt &
taskset -c 2 python3 ./when-to-surrender/main.py F6 best-worst 2.0 1.75 1.5 1.0 f6-best-worst > output/f6-best-worst.txt &
taskset -c 3 python3 ./when-to-surrender/main.py F6 variance 0.8 0.5 0.3 0.1 f6-variance > output/f6-variance.txt &
