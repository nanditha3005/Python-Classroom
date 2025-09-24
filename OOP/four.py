class Account:
    def open_acc(self):
        print('Account created succesfully!')
    def deposit_amount(self,amount):
        print(amount,':Amount deposited')
    def get_Bal(self):
        return 0

a1=Account(101,)    
# above statement is creating object
a1.open_acc()      
# above statement is invoking method
a1.deposit_amount(5000)
a1.deposit_amount(1500)