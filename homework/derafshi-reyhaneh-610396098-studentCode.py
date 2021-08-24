def studentCode(x,p):
	a=int(p[0::2])
	b=int(p[1::2])
	print(a+b*x)
x,p=input().split()
x=int(x)
studentCode(x,p)
