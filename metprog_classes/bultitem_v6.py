import model_v6 as model


@model.entity
class LineItem:
    desc = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, desc, weight, price):
        self.desc = desc
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


