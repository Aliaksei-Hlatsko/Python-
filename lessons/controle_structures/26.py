kod = '0805'
trys = 3

while trys <= 3:
    if trys == 0:
        print("lose pass")
        break
    a = input("your kode")
    if a == kod:
        print("Yes")
        break
    else:
        print("No")
        trys -=1
    