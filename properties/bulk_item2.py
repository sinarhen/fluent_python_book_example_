class LineItem:
    def __init__(self, description: str, weight: int | float, price: int | float):
        self.__desc = description
        self.__weight = weight
        self.__price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError
        self.__weight = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def subtotal(self):
        return self.weight * self.price

"""
Expected
>>>raisins = LineItem('golden raisins', 40, 10)
>>>raisins.subtotal()
400
>>>raisins.price
10
>>>raisins.weight
40
>>>raisins.weight = 50
>>>raisins.subtotal()
500
>>>raisins.weight = -50
Traceback (most recent call last):
  File "D:/PYTHON/p-book/properties/bulk_item2.py", line 14, in weight
    raise ValueError
ValueError
"""