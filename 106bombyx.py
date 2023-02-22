#!/usr/bin/python3

import sys
import math
from math import *
import my_help
from my_help import *

def check_arg():
    if len(sys.argv) != 1 and sys.argv[1] == "-h":
        print_info()
    try:
        len(sys.argv) == 4 or len(sys.argv) == 3
        n = int(sys.argv[1])
        n >= 0
        if (len(sys.argv) == 4):
            i0 = int(sys.argv[2])
            i1 = int(sys.argv[3])
            i0 >= 1 and i0 <= 100
            i1 >= 1 and i1 <= 100
        else:
            k = float(sys.argv[2])
            k >= 1 and k <= 4
    except:
        sys.exit(84)

def option_1():
    x = int(sys.argv[1])
    k = float(sys.argv[2])
    print(1, x)
    i = 2
    while (i <= 101):
        if (x <= 0 or x == 1000):
            xi = 0
        else:
            xi = k * x * (1000 - x) / 1000
        print(i, xi)
        i += 1

def option_2():
    x = int(sys.argv[1])
    i0 = int(sys.argv[2])
    i1 = int(sys.argv[3])
    print(1, x)
    i = 2
    while (i <= i0):
        if (x <= 0 or x == 1000):
            xi = 0
        else:
            xi = k * x * (1000 - x) / 1000
        print(i, xi)
        i += 1
    while (i <= i1):
        if (x <= 0 or x == 1000):
            xi = 0
        else:
            xi = k * x * (1000 - x) / 1000
        print(i, xi)
        i += 1

def main():
    check_arg()

    if (len(sys.argv) == 3):
        option_1()
    if (len(sys.argv) == 4):
        option_2()
main()
