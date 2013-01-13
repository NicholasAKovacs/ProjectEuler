answer = []
number = 2
while number < 10000:
    prime = True
    divisor = 2
    while divisor < number:
        if number % divisor ==0:
            prime = False
        divisor +=1
    if prime:
        answer.append(number)
    number +=1

#gen = (x for x in answer)
#p = gen.__next__()
factors = []
bignum = 600851475143
x = 0

while bignum > 1:
    if bignum % answer[x]:
        x+=1
    else:
        factors.append(answer[x])
        bignum = bignum / answer[x]
print (factors)
