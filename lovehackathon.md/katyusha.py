def f(n, p, m, q):
    return n * p + (n // m + (n % m > 0)) * q


n, p = map(int, input().split())
m, q = map(int, input().split())
result = f(n, p, m, q)
print(result)
