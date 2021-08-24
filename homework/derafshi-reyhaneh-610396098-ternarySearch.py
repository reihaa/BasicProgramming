def ternary_search(a,k):
	lo=0
	hi=len(a)-1
	while(lo<=hi):
		b=lo+(hi-lo)//3
		c=lo+((hi-lo)*2)//3
		if(a[b]==k)or(a[c]==k):
			return 1
		elif k<a[b]:
			hi=b-1
		elif a[b]<k<a[c]:
			lo=b+1
			hi=c-1
		elif a[c]<k:
			lo=c+1
	return 0

n=int(input())
a=list(map(int,input().strip(" ").split()))
key=(int(input()))
if ternary_search(a,key):
	print('Yes')
else:
	print('No')


