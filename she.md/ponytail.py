def f(n):
    return "\n".join([str(i) if i != 0 else "0!!" for i in range(n + 1)[::-1]])


n = int(input())
result = f(n)
print(result)
