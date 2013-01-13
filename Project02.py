fib = [0,1]
answer=[]

for i in range(32):
    fib.append(fib[i]+fib[-1])

print(fib)

for i in fib:
    if i%2==0:
        answer.append(i)

print(sum(answer))
        
        
