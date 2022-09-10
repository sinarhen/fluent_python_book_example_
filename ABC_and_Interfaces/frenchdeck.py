from collections import namedtuple

card = namedtuple('Card', 'rank suit')


class FrenchDeck:
    RANKS = list(range(6, 11)) + list('JQKA')
    SUITS = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = set(card(rank, suit) for rank in self.RANKS
                      for suit in self.SUITS)

    def __len__(self):
        return len(self._cards)

    def get_all_cards(self):
        return self._cards


f = FrenchDeck()
print(f.get_all_cards())
