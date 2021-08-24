def binary(i,n) :
	l=[0]*n
	m=0
	while i>0 :
		l[m] = i - i//2 * 2
		i = i//2
		m+=1
	return l
def parset(a,n):
	m=0
	for i in range(len(a)):
		m+=a[i]
	m=m/2
	for i in range(pow(2,len(a))):
		b = binary(i,n)
		h=0
		for j in range(len(b)-1,-1,-1):
			if b[j] == 1:
				h+=a[j]
		if m-h<=0.0001:
			return b
		

n=int(input())
a=[]
for _ in range(n) :
	a.append(int(input()))
b=parset(a,n)
for i in range(len(b)-1,-1,-1) :
	if b[i] == 1:
		print(a[i],end=' ')


