def abc(a,b,c,s):
	while s<a:
		s=s+c
	while s<=b:
		print(s)
		s=s+c
		
a=int(input("input the beggining of the range"))
b=int(input("input the ending of the range"))
c=int(input("input an integer"))
s=c
abc(a,b,c,s)
 
