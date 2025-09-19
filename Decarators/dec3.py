from loginstatus import login_required

def home_page(is_login):
    print("Home Page")

def products(is_login):
    print("Products Page")

@login_required
def orders(is_login):
    print("Orders Page")

@login_required
def profile(is_login):
    print("Profile page")

home_page(False)   #Home Page
products(False)     #Products Page
orders(False)       #login Required
orders(True)        #Orders Page
profile(False)       #login Required
profile(True)        #profile page



