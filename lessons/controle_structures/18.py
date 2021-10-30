a = int(input('money'))
five = 5
two = 2
one = 1
five_m = int(a/five)
five_ost = a % five

two_m = int(five_ost/two)
two_ost = five_ost % two

print(f"your money{a} is 5zł = {five_m}, 2zł = {two_m}, 1zł = {two_ost}")