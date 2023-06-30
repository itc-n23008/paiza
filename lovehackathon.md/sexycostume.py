def f(m, n):
    return m - n if m > n else 0


m, n = map(int, input().split())
result = f(m, n)
print(result)
