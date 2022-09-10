class LineItem:

    def __init__(self, description, weight, price):
        self.desc = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


"""
Expected:
raisins = LineItem('golden raisins', 10, 15)
raisins.subtotal()
>>>150
raisins.weight = -20
raisins.subtotal()
>>>-300

"""