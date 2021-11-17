def compare(array1,array2):
    #КОЛИЧЕСТВО
    a = 0
    b = 0
    for i in range(len(array1)):
        a+=1
    for k in range(len(array2)):
        b+=1
    if a < b or a > b or array1!=array2:
        print("False")
    else:
        print("True")
    
    
compare(["water","book","sky"],["water","book","sky"])
compare([True,False],[True,False,True])
compare([5,3,1],[5,3,1])
compare([3,2,1],[3,2])
    
    