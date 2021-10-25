#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = tuple(map(int, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
        # Найти искомую сумму.
    s = 1
    f = 0
    for item in A:
        if item < 0:
            s *= item
        if item > 0:
            f += item
    print(s,f)
