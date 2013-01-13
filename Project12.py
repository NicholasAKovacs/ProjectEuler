#! /usr/local/bin/python

L1 = []
x = 0
add = 1
while x < 50000000:
	x +=add
	add +=1
	L1.append(x)

for y in L1:
	L2 = []
	div = 1
	while div <= y:
		if y%div == 0:
			L2.append(div)
			div+=1
		else:
			div+=1
	if len(L2) > 500:
		print y, len(L2)


