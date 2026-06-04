class Wallet:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        print(f"balansi gaizarda: {amount} larit. axali balansi: {self.balance}")

    def spend_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"daxarjia: {amount} lari. darchenili balansi: {self.balance}")
        else:
            print("ar kmara tanxa")

class Animal:
    def __init__(self, name, is_hungry=True):
        self.name = name
        self.is_hungry = is_hungry

    def eat(self):
        self.is_hungry = False
        print(f"{self.name} danayrda")


class Light:
    def __init__(self, is_on=False):
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print("natura chirtva")

    def turn_off(self):
        self.is_on = False
        print("natura gamoirto")