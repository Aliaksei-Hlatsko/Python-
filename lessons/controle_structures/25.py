#The variables a and b contain the dimensions of the sides of the rectangle. Write a program that creates the following rectangle with dimensions a and b. Example result for a = 4 and b = 15:
#***************
#*             *
#*             *
#***************
a = int(input("height"))
b = int(input("size"))

#i = "*"
for i in range(a):
    if i == 0 or i == a-1:
        print("* "*b)
    else:
        print("*" + " " * (b*2-3) + "*")