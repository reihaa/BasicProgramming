import math
from random import randint
def soudoko(a,n):
	for i in range(n):
		for j in range(1,n+1):
			if j not in a[i]:
				print('is not soudoko')
				return
	for i in range(n):
		c=range(1,n+1)
		for j in range(n):
			for i in range(n):
				k =c.find(a[i][j])
				if k != -1:
					del c[k]
			if not c:
				print('is not soudoko')
				return
	h = math.sqrt(n)
	for k in range(0,n,h):
		for h in range(0,n,h):
			c=range(1,n+1)
			for i in range(h):
				for j in range(h):
					k = c.find(a[k+i][h+j])
					if k != -1:
						del c[k]
			if not c:
				print('is not soudoko')
				return
	print('is oudoko')

n=int(input('enter n'))
a=[[randint(1,n) for _ in range(n)]for _ in range(n)]
soudoko(a,n)
	
