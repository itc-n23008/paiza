def f(s, t):
    for i in s:
        if i in t:
            t = t.replace(i, "", 1)
    return len(t)


n, m = map(int, input().split())
s = input()
t = input()
result = f(s, t)
print(result)
