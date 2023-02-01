

#----------------------------

a= (input(''))
a=int(a)
b= (input(''))
b=int(b)
c= (input(''))
c=int(c)

if (a>b and a>c) :
    print("il maggiore è" +" "+ str(a))
elif (b>a and b>c) :
    print("il maggiore è" +" "+ str(b))
elif (c>a and c>b) :
    print("il maggiore è" +" "+ str(c))
else:
    print("sono equali")