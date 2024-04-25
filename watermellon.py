w=int(input('weight of watermellon:'))
if(w%2!=0 or w==2):
    print('no')
else:
    x=w/2
    if (x%2==0):
        print('x1= ',x,'and x2= ',x)
    else:
        print('x1= ',x-1,'and x2= ',x+1)