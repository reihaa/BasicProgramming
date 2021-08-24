def ful_matrix(a,n):
	if n//2 == n/2:
		l=(n-1)//2
		h=n-l
		c=5
		a[l][l]=1
		a[l][l+1]=2
		a[l+1][l+1]=3
		a[l+1][l]=4
		l-=1
		h+=1
		i=l+2
		j=l
		while True :
			while i >= l:
				a[i][j]=c
				c+=1
				i-=1
			i+=1
			j+=1
			while j < h:
				a[i][j]=c
				c+=1
				j+=1
			j-=1
			i+=1
			while i< h:
				a[i][j]=c
				c+=1
				i+=1
			i-=1
			j-=1
			while j>=l :
				a[i][j]=c
				c+=1
				j-=1
			l-=1
			h+=1
			if j==-1: break
	else:
		a[n//2][n//2]=1
		l=n//2-1
		h=n//2+1
		i=n//2
		j=n//2+1
		c=2
		while True :
			while i<= h:
				a[i][j]=c
				c+=1
				i+=1
			i-=1
			j-=1
			while l<= j:
				a[i][j]=c
				c+=1
				j-=1
			i-=1
			j+=1
			while i >=l:
				a[i][j]=c
				c+=1
				i-=1
			i+=1
			j+=1
			while j<=h:
				a[i][j]=c
				c+=1
				j+=1
			h+=1
			l-=1	
			if j==n: break



n=int(input())
a=[[0 for _ in range(n)]for _ in range(n)]
ful_matrix(a,n)
for p in range(n):
	for o in range(n):
		print(str(a[p][o]).ljust(3),end=' ')
	print()
