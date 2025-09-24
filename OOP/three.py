class Test:
    def m1(self):
        print('m1 method -instance method')

    @classmethod   
    def m2(cls):
        print('m2 method - class method')

    @staticmethod    
    def m3():
        print('m3 method -static method ')

t1=Test()
t1.m1()           #m1 method -instance method
t1.m2()           #m2 method - class method
t1.m3()           #m3 method-static method
t2=Test()
t2.m1()          #m1 method -instance method
t2.m2()          #m2 method - class method
t2.m3()          #m3 method -static method

