#!/usr/bin/python3
import time

from matrix_fill.methods import matrix_fill_spiral

if __name__ == '__main__':
    number = 100
    st = time.time()
    for _ in range(100):
        matrix_fill_spiral(number)
    et = time.time()
    print(et - st)
