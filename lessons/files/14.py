with open("filename.txt", "r") as f:
#f = open("filename.txt")
    for line in f:
        print(line, end="")
f.close()