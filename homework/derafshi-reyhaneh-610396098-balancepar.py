def print_par(a,n) :
	for i in range(n):
		print('(',end='')
		for j in range(a[i]):
			print(')',end='')
	print()

def balancepar(n):
	a=[0 for _ in range(n)]
	a[n-1]=n
	for i in range(n) :
		while a[n-1-i]>1 :
			print_par(a,n)
			a[n-1-i]-=1
			a[n-2-i]+=1
	print_par(a,n)
n=int(input())
balancepar(n)
