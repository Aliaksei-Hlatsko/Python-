with open('copy.txt','w') as file:
    with open('text16.txt','r') as content:
        for i in content:
            file.write(i)
        file.close()
        