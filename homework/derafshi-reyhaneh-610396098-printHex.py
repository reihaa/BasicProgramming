def printHex(a) :
	c=""
	for i in range(0,len(a),4) :
		b=0
		v=1
		for j in range(3,-1,-1):
			b+=v*a[i+j]
			v*=2
		c+=str(b)
	print(int(c))
a=list(map(int,input().strip(" ").split()))
printHex(a)
