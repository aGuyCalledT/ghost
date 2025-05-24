import random
from lib.dnd_utils import get_user_input, looping_index
import os

# cards be: 2 3 4 5 6 7 8 9 10 J Q K A - colors be: diamonds (♦), hearts (♥), spades (♠) and clubs (♣)
number_list = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
color_list = ["d","h","s","c"]
currency = "€"
blind = 0.5

color_dict = {
    "d" : "♦",
    "h" : "♥",
    "s" : "♠",
    "c" : "♣",
}

blind_dict = {
    1    : "small_blind",
    2    : "normal_blind",
    3    : "big_blind",
    None : "no_blind"
}

blind_multiplicator_dict = {
    1    : 0.5,
    2    : 1,
    3    : 2,
    None : 0
}

class card():
    def __init__(self, color, number, owner = "pile"):
        self.color = color
        self.number = number
        self.owner = owner

    def __str__(self):
        if self.number != "10":
            return f"[{color_dict[self.color]} {self.number}]"
        else:
            return f"[{color_dict[self.color]}{self.number}]"     

class player():
    def __init__(self, name, money):
        self.name       = name
        self.money      = money
        self.hand       = []
        self.blind      = None
        self.best_hand  = None
        self.fold       = False
    
    def __str__(self):
        return f"Name: {self.name} | Balance: {self.money:.2f}{currency} | Blind: {blind_dict[self.blind]}"
    
    def display_hand(self):
        for card in self.hand:
            print(card)

class river(player):
    def __init__(self, name = "river", money = 0):
        self.card_reveal = 0
        super().__init__(name, money)

    def __str__(self):
        if len(self.hand) < 5:
            return "River is empty"
        else:
            river_display = []
            for card in range(self.card_reveal):
                river_display.append(str(self.hand[card]))
            for x in range(5 - len(river_display)):
                river_display.append("[ X ]")
            
            return "".join(river_display)
        

def create_pile():
    pile = []
    for number in range (13):
        for color in range (4):
            card_number, card_color = number_list[number], color_list[color]
            pile.append(card(number=card_number, color=card_color))

    random.shuffle(pile)
    return pile

def deal_card(pile, player, amount  : int):
    if len(pile) > 0:
        for x in range(amount):
            player.hand.append(pile[0])
            pile.pop(0)
        return True
    else:
        return False
    
def deal_all_cards(player_list):
    pile = create_pile()

    for player in player_list:
        if player.name == "river": amount = 5
        else: amount = 2
        deal_card(pile=pile, player=player, amount=amount)
    
def pay(player_list, player, amount):
    all_in = False
    if amount == "blind":
        amount = blind_multiplicator_dict[player.blind]*blind

    if amount > player.money:
        amount = player.money
        all_in = True
    
    player.money -= amount
    player_list[0].money += amount

    print(f"{player.name} pays {amount:.2f}{currency} into the pot.")
    if all_in: print(f"{player.name} goes All-in!")

    
def create_player_list():
    player_list = []
    number_of_players = get_user_input("int", "How many players are playing?", min_int=2, max_int=12)
    for x in range(number_of_players):
        temp_player_name  = get_user_input("str", f"What is your name player_{x+1:02d}?").capitalize()
        temp_player_money = get_user_input("int", f"How much money are you bringing to the table {temp_player_name}? (amount in {currency})", min_int=10)

        Temp_Player = player(name=temp_player_name, money=int(temp_player_money))
        player_list.append(Temp_Player)

        print("----------")
    return player_list

def give_blinds(player_list):
    first_time_blind = True
    for palyer in player_list:
        if player.blind is not None: 
            first_time_blind = False
            if player.blind == 3:
                last_big_blind_index = player_list.index(player)

    if first_time_blind:    
        big_blind_index = random.randint(0, len(player_list)-1)
        small_blind_index = big_blind_index - 1

    else:
        big_blind_index = last_big_blind_index + 1
        small_blind_index = big_blind_index - 1

    if small_blind_index < 0:
            small_blind_index = len(big_blind_index-1)
    elif small_blind_index > len(player_list)-1:
        pass

    for player in player_list:
        if player.blind is None: player.blind = 2
        print(f"{player.name} has the {blind_dict[player.blind]}")

def pay_blinds(player_list):
    for player in player_list:
        if player.name != "river":
            pay(player_list, player, "blind")
    print(f"There are {player_list[0].money:.2f}{currency} in the Pot!")

def look_at_cards(player):
    input(f"{player.name} it's your turn. Press enter, to see your cards...")
    for card in player.hand:
        print(card)
    input(f"Now press enter, to hide your cards...")
    os.system('cls' if os.name == 'nt' else 'clear')

def betting(player_list):
    player_bets = []
    for player in player_list:
        player_bets.append(None)

    for player in player_list:
        get_user_input("str",  "Now you can either 'check' or 'raise'. (or type 'help')", ["check", "raise", "call", "fold"])
    

def round(player_list, River):
    print("ROUND STARTS")
    print("---------------")

    give_blinds(player_list)
    pay_blinds(player_list)
    deal_all_cards(player_list)


def start_game():
    print("**********************************")
    print("*   Welcome to Texas hold 'em!   *")
    print("**********************************")

    River = river()
    player_list = create_player_list()


    round(player_list, River)

# MAIN CODE
  
index = 2
list_len = 9
increment = 201
looping_index(index=index, increment=increment, list_len=list_len)

player_list = create_player_list()
give_blinds(player_list)
