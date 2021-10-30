a = int(input("age "))
dog_age = 21

if a == 1:
    print(f"The dog's age in dog’s years is {dog_age/2} years")
elif a == 2:
    print(f"The dog's age in dog’s years is {dog_age} years")
else:
    result = dog_age + (a-2)*4
    print(f"The dog's age in dog’s years is {result} years")
