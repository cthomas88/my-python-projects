from random import shuffle

suits = 'H D S C'.split()
ranks = '2 3 4 5 6 7 88 9 J Q K A'.split()


class Deck:

    def __init__(self):
        print("Creating new ordered deck!")
        self.allcards = [(s, r) for s in suits for r in ranks]

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return len(f"Contains {self.cards} cards")

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed: {self.name}", drawn_card)
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        This will return true if player still has cards left
        """
        return len(self.hand.cards) != 0

print("Welcome to War, let's begin...")

d = Deck()

d.shuffle()
half1, half2 = d.split_in_half()

comp = Player("Computer", Hand(half1))

name = input("Player, what is your name? ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings: ")
    print(user.name+" has the count: "+str(len(user.hand.cards)))
    print(comp.name+" has the count: "+str(len(comp.hand.cards)))
    print("Play a card!")
    print("\n")

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game Over! Number of rounds: "+str(total_rounds))
print("A war happened "+str(war_count) + " times")
print("Does the computer still have cards? ")
print(str(comp.still_has_cards()))
print(f"Does {user.name} still have cards? ")
print(str(user.still_has_cards()))