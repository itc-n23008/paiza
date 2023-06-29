def f(p):
    return "yes" if p.count("yes") > p.count("no") else "no"


p = [input() for _ in range(5)]
result = f(p)
print(result)
