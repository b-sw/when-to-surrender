#!/bin/sh

mkdir graphs

python3 ./when-to-surrender/main.py F4 k-iter 3 7 15 25
python3 ./when-to-surrender/main.py F4 sd 0.9 0.7 0.5 0.3 
python3 ./when-to-surrender/main.py F4 best-worst 100 20 5 1 
python3 ./when-to-surrender/main.py F4 variance 0.1 0.01 0.005 0.001 

python3 ./when-to-surrender/main.py F5 k-iter 2 10 15 30 
python3 ./when-to-surrender/main.py F5 sd 0.7 0.3 0.2 0.01 
python3 ./when-to-surrender/main.py F5 best-worst 50 20 5 1 
python3 ./when-to-surrender/main.py F5 variance 100 1 0.1 0.05 

python3 ./when-to-surrender/main.py F6 k-iter 15 13 45 50 
python3 ./when-to-surrender/main.py F6 sd 0.7 0.2 0.1 0.01 
python3 ./when-to-surrender/main.py F6 best-worst 40 1 5 50 
python3 ./when-to-surrender/main.py F6 variance 1 0.2 0.1 0.15 
