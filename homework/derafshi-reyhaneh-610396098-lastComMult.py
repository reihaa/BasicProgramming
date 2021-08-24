def gcd(a, b):
    A, B=a, b
    C=0
    while (B!=0) :
        C= A % B
        A = B
        B = C
    return(A) 


a1 = int(input("Enter first integer:"))
a2 = int(input("Enter second integer:"))
result=a1*a2/gcd(a1, a2)
print("The least common denominator of",  a1 , "and" , a2, "is: " , result)

