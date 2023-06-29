def count_required_changes(n, m, s, t):
    counter = {}
    for c in s:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    for c in t:
        if c not in counter:
            counter[c] = -1
        else:
            counter[c] -= 1

    answer = sum(-1 * i for i in counter.values() if i < 0)
    return answer

n, m = map(int, input().split())
s = input()
t = input()

answer = count_required_changes(n, m, s, t)
print(answer)

