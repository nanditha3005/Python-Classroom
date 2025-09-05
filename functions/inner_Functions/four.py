#how to invoke inner function from outside---using return innerfunction references
def user_module():

    def login():
        print('Login Sucess')

    def logout():
        print('Logout sucess')

    return 100

inn=user_module()
print(type(inn))   #<class,int>
print(inn)         #100