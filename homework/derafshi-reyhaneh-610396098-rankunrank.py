def rank(a,n,k,c) : #c:list
    c=list(c)
    for i in range(len(c)):
        c[i]= int(c[i])
    i=k-1
    b=0
    while a != c and i>=0:
        b+=1
        while ( (i>=0) and (a[i]==n-k+i+1)):
            i=i-1
        if (i>=0):
            a[i]=a[i]+1
            for j in range(i+1, k):
                a[j]=a[j-1]+1
            i=k-1
    if a==c :
        print(b)
    else:
        print('not found')
    return   


def unrank(a,n,k,c):
    c=int(c)
    i=k-1
    b=0
    while b!=c and i>=0:
        b+=1
        while ( (i>=0) and (a[i]==n-k+i+1)):
            i=i-1
        if (i>=0):
            a[i]=a[i]+1
            for j in range(i+1, k):
                a[j]=a[j-1]+1
            i=k-1
    if b==c :
        print(a)
    else:
        print('not found')
    return

n=int(input("Enter the nember of set elements: "))
k=int(input("Enter the length of sub sets: "))
a=[i+1 for i in range(k)]
d=input('1.rank 2.unrank')
c=input()
if d=='1' :
	rank(a,n,k,c)
if d=='2' :
	unrank(a,n,k,c)
