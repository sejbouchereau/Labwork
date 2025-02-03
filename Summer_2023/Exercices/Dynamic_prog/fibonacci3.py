# -*- coding: latin-1 -*-
def fib_mem(n):
    mem = [0] * (n + 1)  # permet de créer un tableau contenant n+1 zéro
    return fib_mem_c(n, mem)


def fib_mem_c(n, pos):
    if n == 0 or n == 1:
        pos[n] = n
        return n
    elif pos[n] > 0:
        return pos[n]
    else:
        pos[n] = fib_mem_c(n - 1, pos) + fib_mem_c(n - 2, pos)
    return pos[n]


print(fib_mem(9))
