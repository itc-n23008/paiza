def f(c, p):
    return 1 if c[0] / p[0] > c[1] / p[1] else 2


c, p = zip(*(map(int, input().split()) for _ in range(2)))
result = f(c, p)
print(result)
