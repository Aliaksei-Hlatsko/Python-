n = 1
i = 0
sum = 0
while n != 0:
    n = int(input("Num "))
    if n == 0:
        sum += n
        break
    else:
        sum += n
        i += 1
mean = sum / i
print(f"result: quantity {i}, Sum {sum}, Mean {mean}")
    