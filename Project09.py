a=1
b=2
c=3
while b<c:
    if (a*a)+(b*b)==(c*c) and a+b+c==1000:
        print(a,b,c)
    elif c==1000:
        b+=1
        c=b+1
    elif b==1000:
        a+=1
        b=a+1
        c=b+1
    else:
        c+=1
