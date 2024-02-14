from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < -2 and n % 2 == 0:
        n = -n
        return -(fib(n//2+1)*fib(n-n//2) + fib(n//2)*fib(n-n//2-1))
    elif n < -2 and n % 2 == 1:
        n = -n
        return fib(n//2+1)*fib(n-n//2) + fib(n//2)*fib(n-n//2-1)
    elif -3 < n < 0: return [-1,1][n]
    elif -1 < n < 3: return [0,1,1][n]
    elif n > 2: return fib(n//2+1)*fib(n-n//2) + fib(n//2)*fib(n-n//2-1)
