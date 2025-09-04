#inisde function one more function-inner is defined inside the outer fucntion and is invoked inside only
#if inner is invoked after outer in outside it gives Name Error

def outer():
    print('outer function started')

    def inner():
        print('inner function')
    inner()
    inner()

outer()