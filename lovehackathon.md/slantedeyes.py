def calculate_discounted_price(p):
    return p // 100 if p < 1000 else p // 100 + 10

p = int(input("買物額を入力してください: "))

answer = calculate_discounted_price(p)
print(answer)

