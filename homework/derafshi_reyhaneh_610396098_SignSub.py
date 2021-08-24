Astr = input("Enter first number:")
A=int(Astr)
Bstr = input("Enter second number:")
B=int(Bstr)
C=A
D=B
if (D>=0) :
    while (D!=0) :
        D=D-1
        C=C-1
else :
    while (D!=0) :
        D=D+1
        C=C+1
print(C)

