import random


def evaluator(value, pad):
    # this function is returning the points a player get when entering their roll into the pad
    potential_pad_entry = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    kind_list = [0, 0, 0, 0, 0, 0]
    for x in range(0, 5):
        kind_list[value[x] - 1] += 1

    street_len = [1, 1, 1]
    str_pointer = 0
    for x in range(0, 5):
        if x > 0 and last_num + 1 == value[x]:
            street_len[str_pointer] +=1
        elif x > 0 and last_num == value[x]:
            pass
        elif x > 0 and last_num + 1 <= value[x]:
            str_pointer += 1
        last_num = value[x]
    street_len = max(street_len)

    for x in range(0, 13):
        if pad[x] is None:
            if x < 6:
                potential_pad_entry[x] = kind_list[x] * (x+1)
            elif x == 6 and max(kind_list) > 2:
                potential_pad_entry[x] = sum(value)
            elif x == 7 and max(kind_list) > 3:
                potential_pad_entry[x] = sum(value)
            elif x == 8 and 3 in kind_list and 2 in kind_list:
                potential_pad_entry[x] = 25
            elif x == 9 and street_len > 3:
                potential_pad_entry[x] = 30
            elif x == 10 and street_len > 4:
                potential_pad_entry[x] = 40
            elif x == 11 and 5 in kind_list:
                potential_pad_entry[x] = 50
            elif x == 12:
                potential_pad_entry[x] = sum(value)
    return potential_pad_entry

def display_options(potential_pad_entry):
    for x in range(0, 13):
        print(f"'{pad_term[x]}' = {pad[x]} --> {potential_pad_entry[x]}")


def roll(sides, rolls):
    # makes a number of 'rolls' with classic PnP dice with defined number of 'sides'
    ret_list = []
    list_of_possible_dice = [2, 4, 6, 8, 10, 12, 20, 100]
    if sides in list_of_possible_dice:
        for x in range(0, rolls):
            ret_list.insert(0, random.randint(1, sides))
        ret_list.sort()
        return ret_list

    else:
        print("Error: die doesn't exist (possible dice: " + str(list_of_possible_dice) + ")")
        return