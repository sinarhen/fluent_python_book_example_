class LineItem:
    def __init__(self, description, weight, price):
        self.desc = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @staticmethod
    def quantity(storage_name):
        def gty_getter(instance):
            return instance.__dict__[storage_name]

        def gty_setter(instance, value):
            if value < 0:
                raise ValueError('val must be > 0')
            instance.__dict__[storage_name] = value

        return property(gty_getter, gty_setter)

    weight = quantity('weight')
    price = quantity('price')

"""Expected
"""