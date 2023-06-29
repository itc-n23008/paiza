def f(s):
    return "_".join(s)


n = int(input())
s = [input() for _ in range(n)]
result = f(s)
print(result)
