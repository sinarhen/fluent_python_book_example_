import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def get_all_cards(self):
        return self._cards


beer = Card('7', 'diamonds')
deck = FrenchDeck()
print(deck[-1])

cards = {
    'spades': 3,
    'diamonds': 2,
    'clubs': 1,
    'hearts': 0
}


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(cards) + cards[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
