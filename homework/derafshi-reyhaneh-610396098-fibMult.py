
def factorial(n):
      b=1
      a=n
      while (a >1) :
            b= b * a 
            a = a -1 
      return(b) ;
def fibb(N,a,b):
	while N-2>=1 :
		a=factorial(a)
		b=factorial(b)
		c=a*b
		N=N-1
		a=b
		b=c
	return c
a=1
b=2
N=int(input("inter an integer:"))
if N==1 :
	X=1
elif N==2 :
	X=2
else :
	X=fibb(N,a,b)
print(X)
	
