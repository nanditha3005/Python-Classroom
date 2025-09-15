def user_module():
    def login():
        print('Login Sucess')
    def logout():
        print('Logout Sucess')

    return 100
x=user_module()
print(x)        #100


def user_module():
    def login ():
        print('login sucess')
    def logout():
        print('logout sucess')

    return login()
x=user_module
print(x)          #None because user moudle is not invoking(),and login is getig invoked so it shows none.

def user_module():
    def login():
        print('login sucess')
    def logout():
        print('logout sucess')

    return login
x=user_module()    #login sucess because user module is invoking and login is just a reference
x()