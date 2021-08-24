val=input()
key=input()
s=input()
f=""
for i in range(len(s)) :
	k=s[i:i+1]
	k=k.replace(val[val.find(k[0])],key[val.find(k[0])])
	f=f+k
print(f)
