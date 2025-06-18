
from abc import ABC, abstractmethod
class Chai(ABC):
    @abstractmethod
    def calculate_Price(self):
        return 5.0
    
    @abstractmethod
    def display_info(self):
        pass
    
    @abstractmethod
    def sum_price(self):
        pass

class MasalaChai(Chai):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_Price(self):
        return super().calculate_Price() + self.price

    def display_info(self):
        return f"Name: {self.name} | price per cup: ${self.calculate_Price()} | stock : {self.quantity}"

    def sum_price(self):
        return self.calculate_Price() * self.quantity

class GingerChai(Chai):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_Price(self):
        return super().calculate_Price() + self.price

    def display_info(self):
        return f"Name: {self.name} | price per cup: ${self.calculate_Price()} | stock : {self.quantity}"
    def sum_price(self):
        return self.calculate_Price() * self.quantity
    
class ElaichiChai(Chai):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_Price(self):
        return super().calculate_Price() + self.price

    def display_info(self):
        return f"Name: {self.name} | price per cup: ${self.calculate_Price()} | stock : {self.quantity}"
    
    def sum_price(self):
        return self.calculate_Price() * self.quantity
    

chai1 = GingerChai("Ginger Chai", 2.5, 10)
print(chai1.display_info())
chai2 = MasalaChai("Masala Chai", 3.0, 5)
print(chai2.display_info())
chai3 = ElaichiChai("Elaichi Chai", 2.0, 8)
print(chai3.display_info())

print(f"total expense is {chai1.sum_price() + chai2.sum_price() + chai3.sum_price()}")