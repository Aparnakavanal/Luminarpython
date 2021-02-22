import datetime         #datetime.today(), datetime.datetime.now()
class Bank:
    bank_name="sbi"   #static variable or class variable    access as classname.static var

    def create_account(self,acno,c_name,phno,balance):
        
        self.acno=acno
        self.c_name=c_name
        self.phno=phno
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(Bank.bank_name,"account number",self.acno,"credited with",amount,"on",datetime.datetime.now(),"aval balance is",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed")
        else:
            self.balance-=amount
            print(Bank.bank_name,"account number",self.acno,"debited with",amount,"aval balance is",self.balance)

    def balance_enq(self):
        print("account balance is",self.balance)


        
obj=Bank()
obj.create_account(1001120,"shilpa",9547854112,5000)
obj.deposit(4000)
obj.withdraw(500)
obj.balance_enq()
