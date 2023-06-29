def check_seating_availability(RemainSeatsQuant, PeopleQuant):
    return "OK" if RemainSeatsQuant >= PeopleQuant else "NG"

RemainSeatsQuant, PeopleQuant = map(int, input().split())

answer = check_seating_availability(RemainSeatsQuant, PeopleQuant)
print(answer)

