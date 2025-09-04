#how to invoke inner function from outside

def user_module():

    def login():
        print('Login Sucess')

    def logout():
        print('Logout sucess')

    return logout

inner=user_module()
print(type(inner))   #<class,function>
print(inner)         #<function user_module.<locals>.logout at 0x000002015D4FEDD0>
inner()               #logout sucess
inner()