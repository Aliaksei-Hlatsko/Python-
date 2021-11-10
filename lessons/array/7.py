a = [1,3,5,2,4] #3 nech 2 chet
even = 0
odd = 0
for i in range(len(a)):
    if a[i]%2==0:
        even +=1
    else:
        odd +=1
print(f"even: {even}, odd: {odd}") 
