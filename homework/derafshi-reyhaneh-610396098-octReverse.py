def oct(a) :
	while a>=8 :
		b=a%8
		a=int(a/8)
		print(b)
	print(a)
n=int(input("enter an enteger:"))
oct(n)
