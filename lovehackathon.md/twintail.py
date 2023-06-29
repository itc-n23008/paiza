def create_status_string(TotalLength, CurrentStatusNum):
    return ''.join(['+' if i == CurrentStatusNum - 1 else '-' for i in range(TotalLength)])

TotalLength = int(input("総文字列の長さを入力してください: "))
CurrentStatusNum = int(input("現在の位置を入力してください: "))

status_string = create_status_string(TotalLength, CurrentStatusNum)
print(status_string)

