import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (f"{self.rank} of self.suit")

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in range(2, 15):
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw()
        if card:
            self.hand.append(card)
            return card
        else:
            return None

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop(0)
        else:
            return None 

def compare_cards(card1, card3):
    if card1.rank > card3.rank:
        return 1
    elif card1.rank < card3.rank:
        return 2
    else:
        return 0

def main():
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Deal cards to players
    while True:
        card1 = player1.draw_card(deck)
        card2 = player2.draw_card(deck)
        if card1 is None or card2 is None:
            break

    # Play the game
    score1 = 0
    score2 = 0
    for _ in range(52):  # Total number of cards in a standard deck
        card1 = player1.play_card()
        card2 = player2.play_card()
        if card1 is None or card2 is None:
            break
        result = compare_cards(card1, card2)
        if result == 1:
            score1 += 1
            print(f"{player1.name} wins: {card1} beats {card2}")
        elif result == 2:
            score2 += 1
            print(f"{player2.name} wins: {card2} beats {card1}")
        else:
            print("It's a tie!")

    # Determine the winner
    if score1 > score2:
        print(f"{player1.name} wins the game with {score1} cards!")
    elif score2 > score1:
        print(f"{player2.name} wins the game with {score2} cards!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
