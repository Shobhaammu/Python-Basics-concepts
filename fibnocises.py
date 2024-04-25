n=int(input('enter number of items:'))
a,b=0,1
for i in range (n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b
   # a,b=b,a+b
    
    