def f(n, a):
    return sorted(a)[n // 2]


n = int(input())
a = [int(i) for i in input().split()]

result = f(n, a)
print(result)
