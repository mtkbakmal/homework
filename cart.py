class Cart:
    def __init__(self, title, price, description, count = 0):
        if price < 0:
            print("Negative price.")
        if count < 0:
            print("Negative count.")
        
        self.__title = title
        self.__price = price
        self.__description = description
        self.count = count

    def add_to_cart(self, quantity):
        if quantity < 0:
            print("Can not add a negative number to quantity.")
        else:
            self.count += quantity

    def remove(self, quantity):
        if quantity < 0:
            print("Can not remove a negative number off quantity.")
        else:
            self.count -= quantity
        if self.count < 0:
            self.count = 0

    def total_price(self):
        self.total_price = self.__price * self.count
    
    def __str__(self):
        return (f"Item: {self.__title}\n"
        f"Price: {self.total_price}\n"
        f"Description {self.__description}\n"
        f"How many in cart: {self.count}")

laptop = Cart("Ноутбук", 50000, "Игровой ноутбук", 1)

laptop.add_to_cart(10)
print(laptop)
laptop.remove(9)
print(laptop)
