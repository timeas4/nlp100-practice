from functools import cache
N = int(input())
@cache
def f(N):
    if N == 0:
        return 1

    return f(int(N/2))+f(int(N/3))+f(int(N/5))
print(f(N))