def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        # return fib(n - 1) + fib(n - 2)
        return fib(n - 2) + fib(n - 1)


print(fib(6))
