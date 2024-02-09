class Account():
    def __init__(self, owner:str, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposite(self, add):
        self.add = add
        self.balance = self.balance + add
    def withdr(self, withdraw):
        self.withdraw = withdraw
        if(self.balance - withdraw >= 0):
            self.balance = self.balance - withdraw
            print("Money withdrawn")
            print('Осталось на карте: ' + str(self.balance))
        else:
            print('Not enough money')
    def info(self):
        print('Name: ' + self.owner)
        print('Balance: ' + str(self.balance))

mako = Account('Aiko', 300)
mako.deposite(200)
mako.withdr(600)
mako.info()     