class Test:
    a=10   #class variable
    def __init__(self):
        self.b=20
        self.c=30
    def m1(self):
        self.d=40
    def m2(self):
        self.e=50

t1=Test()
t1.m1()
print(t1.__dict__)      #{'b': 20, 'c': 30, 'd': 40}

print(Test.__dict__)  #{'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 
                         #0x000001F612E9FD90>, 'm1': <function Test.m1 at 0x000001F612E9FF40>,
                         #  'm2': <function Test.m2 at 0x000001F612E9FEB0>, '__dict__': <attribute '__dict__' 
                         # of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>,
                         #  '__doc__': None}
t2=Test()
t2.m2()
print(t2.__dict__)      #{'b': 20, 'c': 30, 'e': 50}

print(t1.a+ t2.b+t1.c+t2.e)      #110

t1.a=11
t2.b=21 
print(t1.a+t1.b+t2.b)        #52