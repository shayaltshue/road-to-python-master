from playing_cards import Card

# Variables to help instantiate deck
suits = ['Heart', 'Club', 'Diamond', 'Spade']
n_range = 14

cards = []

# Instantiating the Deck
for s in suits:
    for i in range(n_range):
        cards.append(Card(False, s, i))


for card in cards:
    card.print_description()