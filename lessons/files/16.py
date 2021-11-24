with open('text16.txt', 'r') as file:
    line_num = 1
    count = 0
    for i in file:
        print(line_num, i)
        line_num +=1
        count +=1
        if count == 5:
            input()
            count = 0
file.close()