def vigitAdd(a) :
	while a>=10 :
		b=0
		while a>=10 :
			n=a-(a//10)*10
			b=b+n 
			a=a//10
		b=b+a
		a=b
	return a
a=int(input("enter an integer:"))
A=vigitAdd(a)
print(A)
