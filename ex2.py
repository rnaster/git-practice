import collections

card = collections.namedtuple('card', 'number suit')


class CardDeck:
    size = 52

    def __init__(self):
        self.cards = [
                card(number, suit)
                for suit in ['S', 'H', 'C', 'D']
                for number in list(range(2, 11)) + ['J', 'Q', 'K', 'A']
                ]


if __name__ == '__main__':
    card_deck = CardDeck()
    for card in card_deck.cards:
        print(card)
