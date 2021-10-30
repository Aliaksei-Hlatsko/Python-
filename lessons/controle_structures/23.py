"""
* 
* * 
* * * 
* * * * 
* * * * * max
* * * * -1
* * * 
* * 
*
"""
#a = int(input("hieght odd")) # 9
"""
a = int(input())+1
while a != 0:
    a-=1             min
    print("*"*a)
"""

a = int(input("odd num "))
center = int(a/2)+1 #max
for i in range(1,center+1):
    print("* "*i)
while center != 0:
    center-=1
    print("* "*center)
