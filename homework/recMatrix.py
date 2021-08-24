def read_matrix(n):
	if n == 0:
		return []
	else:
		a = list(map(int, input().split()))
		return ([a]+read_matrix(n-1))


def print_matrix(m,n, a):
	if n == -1:
		return
	print(a[m-n])
	print_matrix(m,n-1,a)

def determinent(a, n):
	det=0
	if n == 2:
		return(a[0][0]+a[1][1]-a[0][1]-a[1][0])
	else:
		b=-1	
		for i in range(n):
			c=[[a[o][j] for j in range(n)]for o in range(n)]
			del(c[i])
			for h in range(n-1):
				del(c[h][i])
			b=-b
			det+=b*a[0][i]*determinent(c,n-1)
	return det			

m = int(input())
a = read_matrix(m)
print_matrix(m-1,m-1,a)
v=determinent(a, m)
print(v)
