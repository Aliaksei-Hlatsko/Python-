array = [4, 3, 7, 1, 3]
def array2str(array):  
    for i in range(len(array)):
        print(f"{array[i]}", end =" ")
    print()
            
def sum(array):
    a = 0
    for i in range(len(array)):
        a +=array[i]
    print(f"Sum of values: {a}")
    

array2str(array)
sum(array)