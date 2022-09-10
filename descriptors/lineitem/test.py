class Quantity:

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        print('__get__')
        return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        print('__set__')
        instance.__dict__[self.storage_name] = value


class Product:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price