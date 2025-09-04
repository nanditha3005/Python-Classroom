def user_module(name,status):

    def login():
        print('login sucess')

    def logout():
        print('logout sucess')

    if status==True:
        return login
    else:
        return logout

inner=user_module('rahul',False)
inner()           #logout sucess
    