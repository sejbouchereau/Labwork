from typing import Dict

stats: Dict[int, int] = {}


def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        resultat = fib(n - 1) + fib(n - 2)
        if n not in stats.keys():
            stats[n] = 1
        else:
            stats[n] += 1
        return resultat


print(fib(6))
print(stats)
