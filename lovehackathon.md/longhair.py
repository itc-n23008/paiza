def f(N):
    return "lucky" if N % 7 == 0 else "unlucky"


N = int(input())

result = f(N)
print(result)
