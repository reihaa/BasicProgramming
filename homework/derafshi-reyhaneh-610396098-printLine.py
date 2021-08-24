def printLine(a,b) :
	n=b
	while a>0 :
		b=n
		while b>0 :
			print("*",end="")
			b=b-1
		print("")
		n=n-1
		a=a-1
a=int(input("enter line number:"))
b=int(input("enter * number:"))
printLine(a,b)
