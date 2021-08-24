def ksmallest(a,b):#a:list b:integer
	prv=a[0]
	for _ in range(b) :
		min=a[0]
		for i in range(len(a)):
			if a[i]<min:
				min=a[i]
		del a[a.index(min)]
	return min
n,b=input().split()
n=int(n)
b=int(b)
a=list(map(int,input().strip(" ").split()))
print(ksmallest(a,b))
