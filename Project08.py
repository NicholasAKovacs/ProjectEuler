file = open('/home/nick/Documents/ProjectEuler/Project08.docx')
c1 = 0
answer=[]
for i in file:
	while c1<996:
		x =i[c1:c1+5]
		n=int(x[0])*int(x[1])*int(x[2])*int(x[3])*int(x[4])
		if n != 0:
			answer.append(n)
		c1+=1
num = 0
for a in answer:
    if a > num:
        num = a

print(num)
    
    
