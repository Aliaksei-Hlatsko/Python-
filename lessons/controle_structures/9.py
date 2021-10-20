a = int(input("First "))
b = int(input("Second "))

def cheak_int(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else: print("its 0")

cheak_int(a)
cheak_int(b)