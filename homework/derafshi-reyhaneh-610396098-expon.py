def expon(p,x) :
	b=c=1
	n=0
	while p>0 :
		n+=b
		b=b*x/c
		c+=1
		p-=1
	return n		
p=int(input("enter p"))
x=int(input("enter x"))
n=expon(p,x)
print("e^x:",n)
