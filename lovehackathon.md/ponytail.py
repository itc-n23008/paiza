def check_answers():
    CorrectAnswerQuant = 0
    for _ in range(5):
        dn, en = input().split()
        if dn == en:
            CorrectAnswerQuant += 1

    Answer = "OK" if CorrectAnswerQuant >= 3 else "NG"
    print(Answer)

