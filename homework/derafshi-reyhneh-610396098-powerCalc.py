def powerCalc(b,c,a) :
	c=c/3600
	if(c>a) :
		n=(2*c-a)*b
	else :
		n=c*b
	return n
price=int(input("enter the price for each kwh"))
time=int(input("how many sec you used power?"))
a=int(input("how many hours you can use power for normal price?"))
money=powerCalc(price,time,a)
print("you have to pay",money)
