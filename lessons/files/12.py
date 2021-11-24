a = input('Product ')
file = open('product.txt', 'a')
file.write(a + '\n')
file.close()