#how to invoke inner function from outside

def user_module():

    def login():
        print('Login Sucess')

    def logout():
        print('Logout sucess')

    return login

inner=user_module()
print(type(inner))   #<class,function>
#print(inn)         #<function user_module.<locals>.login at 0x000001BE02D3FB50>
inner()               #login sucess
inner()