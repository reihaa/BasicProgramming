A = int(input("Enter first number:"))
B = int(input("Enter second number:"))
if(B==0) :
    print("division is not possible")
elif(A>=0) :
    if(B>0) :
        while (A>=B) :
            A=A-B
    else :
        while (A>=-B) :
            A=A+B
    print(A)
else :
    if(B>0) :
        while (A<0) :
            A=A+B
    else :
        while (A<0) :
            A=A-B
    print(A)
