import random
def rand(x,y):
    a = 1
    while a == 1:
        b = random.randint(x,y)
        if b % 2 == 0 and b % 3 == 0:
            print(b)
            break
rand(10,50)