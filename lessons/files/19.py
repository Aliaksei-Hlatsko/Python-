with open('shoppinglist.txt', 'w') as file_1:
    with open('GrainsAndBread.txt', 'r') as file_2:
        for i in file_2:
            file_1.write(i)
        with open('MeatAndFish.txt', 'r') as file_3:
            for p in file_2:
                file_1.write(p)
            file_1.close()