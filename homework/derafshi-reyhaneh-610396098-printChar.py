def printchar(a) :
	nstr=""
	num=""
	sign=""
	counter=0
	while(counter<len(a)):
		c=a[counter]
		if('a'<=c<='z' or 'A'<=c<='Z'):
			nstr=nstr+c
		elif( '0'<=c<='9'):
			num=num+c
		else:
			sign=sign+c
		counter+=1
	print(nstr)
	print(num)
	print(sign)
a=input()
printchar(a)
