def merge(a, b, c):
	i,j,k=0,0,0
	while ((i<len(a)) and (j<len(b))):
		if(a[i] < b[j]):
			c[k]=a[i]
			i=i+1;
		else: 
			c[k]=b[j]
			j=j+1
		k=k+1 
	if(i<len(a)):
		for L in range(i,len(a)):
			c[k]=a[L]
			k=k+1
	if(j<len(b)):
		for L in range(j, len(b)):
			c[k]=b[L]
			k=k+1

	for e in range(len(c)) :
		print(c[e], end=" ")	
	return

a=list(input().strip().split(" "))
b=list(input().strip().split(" "))
a.sort()
b.sort()
c=['']*(len(a)+len(b))
merge(a, b, c)
