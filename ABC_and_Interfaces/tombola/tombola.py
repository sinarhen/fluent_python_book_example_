from abc import ABC, abstractmethod


class Tombola(ABC):

    @abstractmethod
    def load(self, iterable):
        """Добавить элементы из итерируемого объекта"""

    @abstractmethod
    def pick(self):
        """Извлечь случайный элемент и вернуть его
        Этот метод должен возбуждать исключение LookupError
        если объект пуст"""

    def loaded(self):
        """Должен возвращать True если есть хотя бы один элемент"""
        return bool(self.inspect)

    @property
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))



