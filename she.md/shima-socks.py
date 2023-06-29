def f(a, b):
    return "".join(["R" if (i // a) % 2 == 0 else "W" for i in range(b)])


a, b = int(input()), int(input())
result = f(a, b)
print(result)
