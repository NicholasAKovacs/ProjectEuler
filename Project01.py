x = 0
L3 = []
L5 = []
while x < 999:
    x+=1
    if x%3 == 0:
        L3.append(x)
    if x%5 == 0:
        L5.append(x)
for x in L5:
    if x in L3:
        L5.remove(x)
print L3
print L5

print sum(L3)
print sum(L5)
SumList = sum(L3) + sum(L5)
print SumList
