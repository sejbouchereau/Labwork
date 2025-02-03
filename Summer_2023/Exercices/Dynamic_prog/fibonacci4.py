# -*- coding: latin-1 -*-
from typing import Dict, List

stats: Dict[int, int] = {}


def fib_mem(n: int) -> int:
    mem: List[int] = [0] * (n + 1)  # permet de créer un tableau contenant n+1 zéro
    return fib_mem_c(n, mem)


def fib_mem_c(n: int, mem: List[int]) -> int:
    if mem[n] > 0:
        return mem[n]
    elif n < 2:
        mem[n] = n
        return n
    else:
        mem[n] = fib_mem_c(n - 1, mem) + fib_mem_c(n - 2, mem)
        if n not in stats.keys():
            stats[n] = 1
        else:
            stats[n] += 1
        return mem[n]


print(fib_mem(6))
print(stats)
