class user_details:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    def display_details(self):
        print('User Name:',self.username)
        print('Password:',self.password)
        
    def get_password(self):
        return self.password
        
        if self.password=='shobha':
            return ('Welcome')
        else:
            return ('try again')
x=user_details(username='shabana',password='shobha')
print('User name:',x.username)
print('Password:',x.password)