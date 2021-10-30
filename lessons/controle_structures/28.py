x = 0
y = 1

print(x)
print(y)
for i in range(15):
    print(x+y)
    x+=y
    print(y+x)
    y+=x
