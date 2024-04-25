#1. variable and data types;
x=input('enter the value of x')
print(x)

#2. arithmetic operators;
a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
x=a+b
print(x)
y=a-b
print(y)
z=a*b#
print(z)
t=a/b
print(t)

#3.comparison operators
x=int(input('enter the value of x'))
y=int(input('enter the value of y'))
if (x>y):
    print('x is greater than y')
elif (x<y):
    print('x is lesthan y')
else:
    print('x is equal to y')    
 
#4.logical operators
x=int(input('enter the value of x'))
if (x%2==0 and x%3==0):
    print('a is divisible by 2 and 3')
else:
    print('a is not divisible by 2 and 3')    

#5.string manipulation
s='shobha'
print(len(s))
t=s.upper()
print(t)


#6.conditional statements
x=int(input('enter the value of x'))
if (x>0):
    print('x is positive')
elif (x<0):
    print('x is negative')
else:
    print('x is zero')  

#8.list
x=['apple','banana','mango']
print(x)
x.append("fruit")
print(x)

#9. tuples
x=(10,'hello',True)
print(x)
y=list(x)
print(y)

#10.dictionary
x={'apple':'red','mango':'yello','berry':'orange'}
print(x)
print(type(x))  
x.update({'graps':'green'})
print(x)