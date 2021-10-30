a = int(input("first point "))
b = int(input("second point "))

if a > 0 and b > 0:
    print(f"P({a},{b}) 1")
elif a < 0 and b > 0:
    print(f"P({a},{b}) 2")
elif a < 0 and b < 0:
    print(f"P({a},{b}) 3")
elif a > 0 and b < 0:
    print(f"P({a},{b}) 4")
