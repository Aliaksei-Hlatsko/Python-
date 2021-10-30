for a in range(1,31):
    if a % 3 == 0 and a % 5 == 0:
        print("Bingo")
    elif a % 3 == 0:
        print("Try")
    elif a % 5 == 0:
        print("Five")
    else:
        print(a)