A = int(input("Enter first number A:"))
B = int(input("Enter second number B:"))
C=A
D=B
if ((C>=0) and (D>=0)) :
    while ((C!=0) and (D!=0)) :
     C=C-1
     D=D-1
   
    if ((C==0) and (D==0)) :
        print("A is equal to B")
    elif (C==0) :
        print("B is greater than A")
    else :
        print("A is greater than B")
elif ((C<=0) and (D<=0)) :
    while ((C!=0) and (D!=0)) :
     C=C+1
     D=D+1
   
    if ((C==0) and (D==0)) :
        print("A is equal to B")
    elif (C==0) :
        print("A is greater than B")
    else :
        print("B is greater than A")
else :
    while ((C!=0) and (D!=0)) :
     C=C+1
     D=D+1
   
    if (C==0) :
        print("B is greater than A")
    else :
        print("A is greater than B");
