from utils.interface import con_in
from utils.evaluation import evaluator
from utils.evaluation import roll
pad_term = [
    "ones", "twos", "threes",
    "fours", "fives", "sixes",
    "three of a kind",
    "four of a kind",
    "full house",
    "small street",
    "big street",
    "kniffel", "chance"
]
pad = [3, 12, None, 8, 20, 18, 22, 23, 25, None, None, None, None]


def display_pad(pad, entry_options=None):
    if entry_options is None:
        entry_options = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
        plus = ""
        display_of_options = False
    else:
        plus = "+"
        display_of_options = True
    top_sum = sum(filter(None, pad[0:5]))
    bottom_sum = sum(filter(None, pad[6:12]))
    if top_sum >= 63:
        bonus = 35
        bonus_spacing = ""
    else:
        bonus = 0
        bonus_spacing = " "
    if top_sum < 10:
        top_spacing = "  "
    elif top_sum < 100:
        top_spacing = " "
    else:
        top_spacing = ""
    if bottom_sum < 10:
        bottom_spacing = "  "
    elif bottom_sum < 100:
        bottom_spacing = " "
    else:
        bonus_spacing = ""
    if top_sum + bottom_sum + bonus < 10:
        total_spacing = "  "
    elif top_sum + bottom_sum + bonus < 100:
        total_spacing = " "
    else:
        total_spacing = ""


    print("\033[4m                          \033[0m")
    for x in range(0, 5):
        spacing = " "*(20 - len(pad_term[x]))
        if display_of_options and entry_options[x] is not None:
            print(f"{pad_term[x]}{spacing}| {pad[x]} {plus}{entry_options[x]} [{x}]")
        else:
            print(f"{pad_term[x]}{spacing}| {pad[x]} ")
    if display_of_options and entry_options[x] is not None:
        print(f"\033[4m{pad_term[5]}{spacing}| {pad[5]}\033[0m {plus}{entry_options[x]} [{x}]")
        print(f"TOP SUM                {top_spacing}{top_sum}")
        print(f"\033[4mBONUS                  +{bonus_spacing}{bonus}\033[0m")
    else:
        print(f"\033[4m{pad_term[5]}{spacing}| {pad[5]}   \033[0m")
    for x in range(6, 12):
        spacing = " " * (20 - len(pad_term[x]))
        if display_of_options and entry_options[x] is not None:
            print(f"{pad_term[x]}{spacing}| {pad[x]} {plus}{entry_options[x]} [{x}]")
        else:
            print(f"{pad_term[x]}{spacing}| {pad[x]} ")
    if display_of_options and entry_options[x] is not None:
        print(f"\033[4m{pad_term[12]}               | {pad[12]} {plus}{entry_options[x]} [{x}]\033[0m")
        print(f"BOTTOM SUM             {bottom_spacing}{bottom_sum}")
        print(f"\033[4mTOTAL SUM              {total_spacing}{bottom_sum+top_sum+bonus} [{x}]\033[0m")
    else:
        print(f"\033[4m{pad_term[12]}{spacing}| {pad[12]} \033[0m")


def display_options(pad, entry_options):
    for x in range(0, 13):
        if pad[x] is None and entry_options[x] is not None:
            print(f"[{x}] '{pad_term[x]}' + {entry_options}")


def pad_entry(final_roll):
    evaluation = evaluator(final_roll, pad)
    display_pad(pad, evaluation)
    print("Where do you want to enter your roll?")
    entry_list = []
    for x in range(0, 13):
        if pad[x] is None:
            entry_list.insert(-1, x)
        entry_list.insert(-1, "strike")
    entry_index = con_in(entry_list)
    if entry_index == "strike":
        print(f"What do you want to strike?")
        strike_options = []
        for x in range(0, 13):
            if pad[x] is None:
                print(f"[{x}] {pad_term[x]}")
                strike_options.insert(-1, x)
            con_in(strike_options)
    print(entry_index)
    pad[entry_index] = evaluation[entry_index]
    return entry_index, evaluation[entry_index]


def init():
    print("Welcome to a match of Kniffel against K.A.I.N.A.")


def turn():
    first_roll = roll(6, 5)
    print(f"Your first roll is: {first_roll}")
    first_reroll = con_in(first_roll, True)
    for x in range(0, len(first_reroll)):
        first_roll.remove(first_reroll[x])
    second_roll = first_roll + roll(6, 5 - len(first_roll))
    second_roll.sort()
    print(f"Your second roll is: {second_roll}")
    second_reroll = con_in(second_roll, True)
    for x in range(0, len(second_reroll)):
        second_roll.remove(second_reroll[x])
    third_roll = second_roll + roll(6, 5 - len(second_roll))
    third_roll.sort()
    print(f"Your final roll is: {third_roll}")
    entry = pad_entry(third_roll)
    print(f"Added {entry[1]} points to '{pad_term[entry[0]]}'")

# main code
init()
while None in pad:
    turn()
print(f"Congratulations! You finished the game")
