def patternmatching(a,b) :
	b=list(b)
	a=list(a)
	c=0	
	while(b[0] in a):
		indx=a.index(b[0])
		if len(a[indx:]) >= len(b):
			for i in range(len(b)):
				if a[indx+i]!=b[i]:
					a=a[indx+1:]
					break
			else:
				c=1
				break
		else:
			break
	return c
a=input()
b=input()
if patternmatching(a,b):
	print('Yes')
else:
	print('No')
				 
	

