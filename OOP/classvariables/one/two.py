class Account:
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def open_acc(Self):
            print('Account Created Succesfully')
    def deposit(self,amount):
            self.acc_bal=self.acc_bal+amount
    def withdrawl(self,amount):
            self.acc_bal=self.acc_bal-amount
    def get_bal(self):
            return self.acc_bal -self.min_bal

a1=Account(101,'Rahul',5000)
a1.deposit(500)
a1.deposit(1500)
a1.withdrawl(50)
# print(a1.__dict__) 
print(a1.get_bal())    #6450

a2=Account(101,'Sonia',15000)
a2.deposit(150)
print(a2.get_bal())  #14650
   
a3=Account(101,'Priyanka',25000)
a3.withdrawl(15000)
print(a3.get_bal())     #9500




