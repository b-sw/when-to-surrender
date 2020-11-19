"""
    Name: script.py
    Purpose:

    @author

    Warsaw University of Technology
    Faculty of Electronics and Information Technology
"""
from main import *

ITERATIONS = 2

def main():
    data = []

    for _ in range(ITERATIONS-1):
        data.append(multi())

if __name__ == '__main__':
    main()