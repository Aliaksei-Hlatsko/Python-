file = open('countries.txt', 'r')
t = 1
for i in file:
    print(f"{t}. {i}", end="")
    t+=1
file.close()



