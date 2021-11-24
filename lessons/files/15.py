def lines():
    line = 0
    a = input('name of file')
    a = a+ '.txt'
    with open(f'{a}','r') as l:
        for lines in l:
            line +=1
    print(f'File name: {a}')
    print(f'Number of lines: {line}')
    file.close()
lines()
        
