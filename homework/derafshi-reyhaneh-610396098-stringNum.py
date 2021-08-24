def stringNum(nstr) :
	i=c=b=0
	while i<len(nstr) :
		c=ord(nstr[i])-48
		b=b*10+c
		i+=1
	print(b)
str1=input()
str2=input()
nstr=str1+str2
stringNum(nstr)
