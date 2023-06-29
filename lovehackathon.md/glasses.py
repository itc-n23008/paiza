def find_middle_number(N, NumSequence):
    NumSequence.sort(reverse=True)
    CenterIndex = (N + 1) // 2 - 1
    return NumSequence[CenterIndex]

N = int(input("数字の個数を入力してください: "))
NumSequence = list(map(int, input("数字をスペース区切りで入力してください: ").split()))

Answer = find_middle_number(N, NumSequence)
print(Answer)

