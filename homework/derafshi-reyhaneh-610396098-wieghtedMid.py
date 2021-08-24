def weighted_mid(a,b) :
	for i in range(len(a)) :
		c=0
		d=0
		for j in range(len(a)):
			if b[j]<b[i]:
				c+=a[j]
			if b[i]<b[j] :
				d+=a[j]
		if c< 0.5 and d<=0.5:
			return (i+1)
n=input()
b=list(input().strip().split(' '))
a=list(map(float,input().strip().split(' ')))

print(weighted_mid(a,b))
