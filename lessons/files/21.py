import random
with open('text21.txt', 'w') as file:
    b = 1
    for i in range(50):
        a = random.randrange(100,1000)
        file.write(f'{b}. {a} \n')
        b+=1
    file.close()