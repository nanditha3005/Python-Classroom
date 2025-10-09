class Account:
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount

a1=Account(101,'Rahul',5000)
print(a1.__dict__)      #{'acc_id': 101, 'acc_name': 'Rahul', 'acc_bal': 5000}
a2=Account(101,'Sonia',15000)
print(a2.__dict__)      #{'acc_id': 101, 'acc_name': 'Sonia', 'acc_bal': 15000}
a3=Account(101,'Priyanka',25000)
print(a3.__dict__)    #{'acc_id': 101, 'acc_name': 'Priyanka', 'acc_bal': 25000}


