# class Car:
#      #####abstraction##### 
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started.....")

# car1 = Car()
# car1.start()


class Account:
    
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_num = acc
    def debit(self,amt):
        self.balance -= amt
        print("Rs",amt,"Was debitted")

    def credit(self,amt):
        self.balance += amt
        print("Rs",amt,"Was creditted")    



acc1 = Account(1000,12345678)
print(acc1.balance)
print(acc1.account_num)

acc1.debit(200)
acc1.credit(500)

print(acc1.balance)
print(acc1.account_num)