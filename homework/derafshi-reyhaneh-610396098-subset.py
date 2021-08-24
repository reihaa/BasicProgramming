def next_binary(n,a):
	for i in range(n):
		if a[-1-i]==0:
			a[-1-i]=1
			break
		else:
			a[-1-i]=0

def subset(n) :
	a=[0]*n
	a[-1]=1
	b=' '
	for i in range(pow(2,n)) :
		l=[]
		for k in range(1,n+1):
			if a[-k]==1:
				l.append(str(k))
		next_binary(n,a)
		print(b.join(l))

n=int(input())
subset(n)
