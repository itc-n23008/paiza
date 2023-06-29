def f(x, y):
    list = [str(i) for i in sorted([int(i) for i in y if i not in x])]
    return " ".join(list) if len(list) != 0 else None


n, m1 = int(input()), int(input())
x = list(map(int, input().split()))
m2 = int(input())
y = list(map(int, input().split()))
result = f(x, y)
print(result)
