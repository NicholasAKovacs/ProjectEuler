answer = [2]
number = 3
while len(answer) < 10001:
    prime = True
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            prime = False
        divisor += 1
    if prime:
        answer.append(number)
    number+=2

print (answer[-1])

