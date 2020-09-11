class Card:
    def __init__(self, is_joker, suit, number):
        self.is_joker = is_joker
        self.suit = suit
        self.number = number
    
    def print_description(self):
        if self.is_joker == False:
            # Checks for non-joker face cards (Ace, King, Queen, Jack)
            if self.number in [0, 13, 12, 11]:
                if self.number == 0:
                    print('Ace of {}'.format(self.suit))
                elif self.number == 13:
                    print('King of {}'.format(self.suit))
                elif self.number == 12:
                    print('Queen of {}'.format(self.suit))
                elif self.number == 11:
                    print('Jack of {}'.format(self.suit))
            # If not a joker and not a face card, print the number and the suit
            else:
                print('{} of {}'.format(self.number, self.suit))
        else:
            print('Card is a Joker')