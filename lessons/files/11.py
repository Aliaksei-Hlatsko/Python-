film_titles = ['home','car','moana','koko','friday']
file = open('text11.txt','w')
for i in film_titles:
    file.write(i + '\n')
file.close()