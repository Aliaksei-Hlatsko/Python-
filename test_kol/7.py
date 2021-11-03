def bonus(years):
    a = 100
    b = 200
    c = 50
    #9
    if years <=5:
        result = a*yaers
    else:
        ost_a = a * 5
        ost1 = years%5 # 9 % 5 = 4
        if ost1 <= 3:
            result = ost_a+(b*ost1)
        else:
            ost_b = b * 3
            ost2 = ost1 % 3 #1
            result = ost_a+ost_b+(c*ost2)
    print(result)
            
            
bonus(9)