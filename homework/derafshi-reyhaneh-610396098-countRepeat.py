def countRepeat(b) :
	a=[]
	i=0
	while i<len(b) :
		d=1
		s=i+1
		while i<s<len(b):
			if(b[i]==b[s]) :
				del b[s]
				d+=1
				s-=1
			s+=1
		a.append(d)
		i+=1
	return(a,b)
b=list(input().split())
a,b=countRepeat(b)
for c in range(len(b)) :
	print(b[c],":",a[c])
