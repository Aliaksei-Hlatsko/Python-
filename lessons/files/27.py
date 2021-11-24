import re
file = open('text16.txt', 'r')
for lore in file:
    words = re.findall("\w{6,}",lore)
    validate = []
    for word in words:
        validate.append(word)
    print(validate)
    '''