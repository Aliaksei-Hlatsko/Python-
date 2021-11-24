import re
with open('grades2.txt', 'r') as file:
    text = file.read()
    grades =  re.findall("\d[.]\d",text)
    sumOfGrades = 0
    for number in grades:
        sumOfGrades += float(number)
print("{:.2f}".format(sumOfGrades/len(grades)))