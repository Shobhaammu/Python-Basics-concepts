for i in range(0,3):
    count=0
    password=input(' enter the password:')
    count=count+1
    if(password=='shobha'):
        print('welcom')
        break
    else:
        print('incorrect password enter the correct one:')        
else:
    print('sorry,account is blocked') 


password='shobha'
attempts=3
while attempts >0:
    user_input=input('enter he password:')
    if user_input==password:
        print('Welcome')
        break
    else:
        attempts-=1
        if attempts >0:
            print('wrong password! You have {attempts} attempts left')
        else:
            print('account is blocked')
            break