class Account:
    def __init__(self,id,name,amount):
        min_Bal=500        #class variable i.e one copy is created and share to all object
        self.acc_id=id
        self.acc_name=name
        self.acc_amount=amount
    def open_account(self):
        print('Account created succesfully!')


a1=Account(101,"Rahul Gandhi",50000)
a2=Account(102,"Sonia Gandhi",60000)
a3=Account(103,"Priyanka Gandhi",70000)

#to print in dictionary format
print(a1.__dict__)      #{'acc_id': 101, 'acc_name': 'Rahul Gandhi', 'acc_amount': 50000}
print(a2.__dict__)      #{'acc_id': 102, 'acc_name': 'Sonia Gandhi', 'acc_amount': 60000}
print(a3.__dict__)      #{'acc_id': 103, 'acc_name': 'Priyanka Gandhi', 'acc_amount': 70000}
print(Account.__dict__)