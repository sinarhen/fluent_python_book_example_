from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    """Товары"""
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    """Полная цена одного товара в n-количестве"""
    def total(self):
        return self.price * self.quantity


class Order:
    """Заказ"""
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    """Цена всех продуктов в корзине"""
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    """Рассчет скидки"""
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f'Order total: {self.total()}, due: {self.due()}'


class Promotion(ABC):
    """ABC класс скидки"""
    @abstractmethod
    def discount(self, order):
        """Вернуть в виде положительной суммы скидку"""


class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargePromo(Promotion):
    def discount(self, order):
        distinct_items = (item.product for item in order.cart)
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
    