import math
palindrome=[]
for x in range(777777,999999):
    y = math.floor
    a=y(x%10)
    b=y(x%100/10)
    c=y(x%1000/100)
    d=y(x%10000/1000)
    e=y(x%100000/10000)
    f=y(x%1000000/100000)
    if(a == f and b == e and c == d):
        palindrome.append(x)

for z in palindrome:
    product = 100
    while product < 1000:
        if(z/product < 1000 and (z/product) - math.floor(z/product) == 0):
           print(str(z) + ' product ' + str(z/product))
        product+=1
    
       
    
    
