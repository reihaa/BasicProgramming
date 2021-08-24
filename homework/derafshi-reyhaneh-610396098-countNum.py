n=int(input())
list1=list(map(int,input().strip().split(" ")))
indx=prv=0
while indx <len(list1) :
	counter=0
	s=indx+1
	while indx<s<len(list1) :
		if list1[indx]==list1[s] :
			counter+=1
			del(list1[s])
			s-=1
		s+=1
	if counter>prv :
		list1=list1[indx:]
		indx=0
		prv=counter
	elif counter<prv :
		del(list1[indx])
		indx-=1
	indx+=1
print(min(list1))
