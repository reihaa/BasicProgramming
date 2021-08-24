def maxmatrix(a,m,n): 
	max_=sum_=0
	b=[n-1,n-1]     
	for i in range(n):
		for j in range(n):
			max_+=a[i][j]
	for i in range(m-n+1):
		for j in range(m-n+1):
			for v in range(n):
				for t in range(n):
					sum_+=a[v+j][t+i]
			if sum_ >max_ :
				max_=sum_
				b=[v+j,t+i]
			sum_=0
	return (b)
m,n=map(int,input().split(' '))
a=[[0 for _ in range(m)]for _ in range(m)]

for i in range(m):
	for j in range(m) :
		a[i][j]=int(input())

b=maxmatrix(a,m,n)
for i in range(-n+1,1):
	for j in range(-n+1,1):
		print(a[b[0]+i][b[1]+j],end=' ')
	print()
