def check_divisibility(n, m):
    return "ok" if m % n == 0 else "ng"

n, m = map(int, input().split())

answer = check_divisibility(n, m)
print(answer)

