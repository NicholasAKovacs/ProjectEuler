palindrome = []
for x in range(777777, 999999):
    y = str(x)
    if y == y[::-1]:
        palindrome.append(x)

for z in palindrome:
    i = 101
    while i < 1000:
        if z%i == 0 and z/i < 1000:
            print (z)
        i+=1
