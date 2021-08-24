from random import uniform
def maxRandom(n,m) :
	a=n
	b=n
	while a>=1 :
		c=uniform(n,m)
		if c>b :
			b=c
		a=a-1
	print(b)
n=int(input())
m=int(input())
maxRandom(n,m)
