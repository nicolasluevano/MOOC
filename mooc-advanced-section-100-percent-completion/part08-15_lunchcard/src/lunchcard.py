# Write your solution here:



class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        balance = round(float(self.balance), 1)
        return f'The balance is {balance} euros'

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, deposit):
        if deposit < 0:
            raise ValueError
        else:
            self.balance += deposit


peter = LunchCard(20)
grace = LunchCard(30)

peter.eat_special()
grace.eat_lunch()

print(f'Peter: {peter}')
print(f'Grace: {grace}')

peter.deposit_money(20)
grace.eat_special()

print(f'Peter: {peter}')
print(f'Grace: {grace}')

peter.eat_lunch()
peter.eat_lunch()
grace.deposit_money(50)

print(f'Peter: {peter}')
print(f'Grace: {grace}')


