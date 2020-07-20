class Card:
    def __init__(self, is_joker, suit, number):
        self.is_joker = is_joker
        self.suit = suit
        self.number = number
    
    def print_description(self):
        if self.number == 0:
            print('Ace of {}'.format(self.suit))

ace_spades = Card(False, 'spades', 0)

ace_spades.print_description()
