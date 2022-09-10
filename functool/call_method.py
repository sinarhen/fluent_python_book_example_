import random


class BingoCase:

    def __init__(self, items):
        self.items = sorted(list(items))
        random.shuffle(self.items)

    def __call__(self):
        return self.pick()

    def pick(self):
        try:
            return self.items.pop(), self.items
        except IndexError:
            raise LookupError('fuck')

