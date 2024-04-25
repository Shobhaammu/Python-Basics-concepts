n = int(input('Enter the number of problems: '))
solved_problem=0
unsolved_problem=0
for i in range(n):
    
    #n = int(input('Enter the number of problems: '))
    a, b, c = map(int, input('Enter the persons: ').split())
def persons_solving(n):
    
        if a == 1 and b == 1 and c == 1:
            print('Problem is solved with majority of 3')
            solved_problem+=1
        elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1):
            print('Problem is solving with majority of 2')
        elif (a == 1) or (b == 1) or (c == 1):
            print('Problem will solve')
        elif a == 0 and b == 0 and c == 0:
            print('Problem will not solve')
            unsolved_problem-=1
            
        else:
            print('Problem won\'t solve')

#n = int(input('Enter the number of problems: '))
#a, b, c = map(int, input('Enter the persons: ').split())
print('the number of problems that frnds can implent:')
print(persons_solving(n))
 