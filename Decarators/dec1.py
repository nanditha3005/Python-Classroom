#without using decerator
def greet(name):
    print("Hi",name,"Good Morning")

greet("Rahul")
greet("Sonia")
greet("aruna")


#with using decerator:
def verify(func):
    def inner(name):
        if name=="Modi":
            print("Modi is PrimeMinister")
        else:
            return func(name)
    return inner 

@verify
def greet(name):
    print("Hi ",name,"Good Morning")

greet ("sonia")
greet("Rahul")
greet("Modi")   
    
