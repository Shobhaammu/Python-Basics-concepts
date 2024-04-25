def persons_solving(n):
    for i in range(n):
        for x in range (0,n+1):
            x=int(input('enter the persons'))
            if a==1 and b==1 and c==1:
                print('problem is solved with majority of 3')
            elif a==1 and b==0 or c==1:
                print('problem is solving with majority of 2')
            elif a==0 or b==1 and c==1:
                print('problem will solve')
            elif a==1 and b==1 or c==0:
                print('problem will solve')
            elif a==0 or b==0 and c==1:
                print('probllem wont solve')
            elif a==0 and b==0 and c==0:
                print('problem will not solve')
n=int(input('enter the number of problems:'))
a,b,c=map(int,input().split())    