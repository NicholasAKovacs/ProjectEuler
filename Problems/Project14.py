def Collatz(n):
	count = 0
	while n>1:
		if n%2==0:
			n = n/2
			count+=1
		else:
			n = 3*n+1
			count+=1
	return count

a=0
ans=0
answer=0
while a < 1000000:
	a+=1
	b = Collatz(a)
	if b > ans:
		ans = b
		answer = a
print answer, ans
