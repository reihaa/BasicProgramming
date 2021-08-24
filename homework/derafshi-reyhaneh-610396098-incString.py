def incString(a) :
	a="0"+a
	v=str.maketrans("012345678","123456789")
	s=0
	while a[-1]=="9" :
		a=a[:-1]
		s+=1
	else :
		a=a[:-1]+a[-1].translate(v)+s*'0'
	if a[0]=="0" :
		a=a[1:]
	print(a)
a=input()
incString(a)
