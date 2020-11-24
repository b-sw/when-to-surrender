#!/bin/sh

#taskset -c 0 python3 ./when-to-surrender/main.py F4 k-iter 3 7 15 25 > output/f4-k-iter.txt &
#taskset -c 1 python3 ./when-to-surrender/main.py F4 k-iter 35 100 200 715 > output/f4-k-iter2.txt &
#taskset -c 2 python3 ./when-to-surrender/main.py F4 sd 0.9 0.5 0.4 0.2 > output/f4-sd.txt &
#taskset -c 3 python3 ./when-to-surrender/main.py F4 sd 0.18 0.15 0.12 0.1 > output/f4-sd2.txt &
#taskset -c 4 python3 ./when-to-surrender/main.py F4 best-worst 20 5 1 0.3 > output/f4-best-worst.txt &
#taskset -c 5 python3 ./when-to-surrender/main.py F4 best-worst 0.1 0.05 0.01 0.005 > output/f4-best-worst2.txt &
#taskset -c 6 python3 ./when-to-surrender/main.py F4 variance 0.1 0.01 0.008 0.005 > output/f4-variance.txt & 
#taskset -c 7 python3 ./when-to-surrender/main.py F4 variance 0.003 0.002 0.001 0.0005 > output/f4-variance2.txt & 

#taskset -c 0 python3 ./when-to-surrender/main.py F5 k-iter 2 10 15 60 > output/f5-k-iter.txt &
#taskset -c 1 python3 ./when-to-surrender/main.py F5 k-iter 150 200 300 715 > output/f5-k-iter2.txt &
#taskset -c 2 python3 ./when-to-surrender/main.py F5 sd 0.7 0.2 0.1 0.05 > output/f5-sd.txt &
#taskset -c 3 python3 ./when-to-surrender/main.py F5 sd 0.03 0.02 0.015 0.01 > output/f5-sd2.txt &
#taskset -c 4 python3 ./when-to-surrender/main.py F5 best-worst 50 20 5 2.5 > output/f5-best-worst.txt &
#taskset -c 5 python3 ./when-to-surrender/main.py F5 best-worst 1.5 1 0.75 0.5 > output/f5-best-worst2.txt &
#taskset -c 6 python3 ./when-to-surrender/main.py F5 variance 100 1 0.5 0.3 > output/f5-variance.txt &
#taskset -c 7 python3 ./when-to-surrender/main.py F5 variance 0.2 0.1 0.075 0.05 > output/f5-variance2.txt &

#taskset -c 0 python3 ./when-to-surrender/main.py F6 k-iter 13 15 25 50 > output/f6-k-iter.txt &
#taskset -c 1 python3 ./when-to-surrender/main.py F6 k-iter 75 100 250 715 > output/f6-k-iter2.txt &
#taskset -c 2 python3 ./when-to-surrender/main.py F6 sd 0.7 0.6 0.5 0.3 > output/f6-sd.txt &
#taskset -c 3 python3 ./when-to-surrender/main.py F6 sd 0.2 0.1 0.05 0.01 > output/f6-sd2.txt &
#taskset -c 4 python3 ./when-to-surrender/main.py F6 best-worst 50 10 5 3 > output/f6-best-worst.txt &
#taskset -c 5 python3 ./when-to-surrender/main.py F6 best-worst 2 1.75 1.5 1 > output/f6-best-worst2.txt &
#taskset -c 6 python3 ./when-to-surrender/main.py F6 variance 1 0.8 0.5 0.2 > output/f6-variance.txt &
#taskset -c 7 python3 ./when-to-surrender/main.py F6 variance 0.175 0.15 0.125 0.1 > output/f6-variance2.txt &
