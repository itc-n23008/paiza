def calculate_position_difference(M, N):
    CP = M - N  # CurrentPosition
    return CP if CP > 0 else 0

M, N = map(int, input().split())

answer = calculate_position_difference(M, N)
print(answer)

