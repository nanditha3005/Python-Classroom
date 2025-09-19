def login_required(func):
    def inner(is_login):
        if is_login==False:
            print("login Required")
        else:
            return func(is_login)
    return inner