def matrixth_row(a,n,k):
	lo=0
	hi=n-1
	while(lo<=hi):
		b=lo+(hi-lo)//3
		c=lo+((hi-lo)*2)//3
		if(a[b][0]<=k<=a[b][-1]) :
			if b==0:
				return a[b],b
			elif k==a[b-1][-1]:
				hi=-1
			else:
				return a[b],b
		elif (a[c][0]<=k<a[c+1][0]):
			if b==0:
				return a[c],c
			elif k==a[c-1][-1]:
				hi=-1
			else:
				return (a[c],c)
		elif k<a[b][0]:
			hi=b-1
		elif a[b+1][0]<=k<a[c][0]:
			lo=b+1
			hi=c-1
		elif a[c+1][0]<=k:
			lo=c+1
	return -1,-1

def matrixth(a,x):
	lo=0
	hi=len(a)-1
	while(lo<=hi):
		b=lo+(hi-lo)//3
		c=lo+((hi-lo)*2)//3
		if(a[b]==k):
			if b==0:
				return (x,b)
			elif a[b]==a[b-1]:
				hi-=1
			else:
				return (x,b)
		elif(a[c]==k):
			if c==0: 
				return (x,c)
			elif a[c]==a[c-1]:
				hi-=1
			else:
				return(x,c)
		elif k<a[b]:
			hi=b-1
		elif a[b]<k<a[c]:
			lo=b+1
			hi=c-1
		elif a[c]<k:
			lo=c+1
	return -1,-1

n=int(input())
a=[]
for _ in range(n):
	a.append([])
for i in range(n):
	a[i]=list(map(int,input().strip().split(' ')))

k=int(input())
z=[0,0]
z=matrixth_row(a,n,k)
if -1 not in z:
	l=[0,0]
	l=matrixth(z[0],z[1])
	if -1 not in l:
		print(l[0],l[1])
		exit()
print('NO')
