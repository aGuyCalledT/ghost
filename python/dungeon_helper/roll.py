from os import error
import random
from collections import defaultdict

import lists

def roll(rolls : int= 1, sides : int= 6) -> list:
    if sides == 0 or rolls == 0: return [0]
    return_list= []
    for dice in range(rolls):
        return_list.append(random.randint(1, sides))
    return_list.sort()
    return return_list


def roll_attributes(main_attributes : list= []):
    return_attributes = []
    for x in range(6):
        temp_roll = sum(roll(rolls= 4, sides=6)[1:])
        return_attributes.append(temp_roll)

    high_rolls = return_attributes
    high_rolls.sort(reverse=True)
    high_rolls = high_rolls[:len(main_attributes)]

    insertables = []
    high_rolls_pointer = 0
    for attribute in main_attributes:
        insertable= [high_rolls[high_rolls_pointer], lists.attr_index_dict[attribute]]
        insertables.append(insertable)
        high_rolls_pointer += 1

    for high_roll in high_rolls: return_attributes.remove(high_roll)
    return insert_elements_at_indices(return_attributes, insertables)

    


def insert_elements_at_indices(main_list: list, insertables: list) -> list:
    result_list = []

    # Gruppiere Elemente nach Index für effiziente Suche
    insertions_by_index = {}
    for element, index in insertables:
        if index not in insertions_by_index:
            insertions_by_index[index] = []
        insertions_by_index[index].append(element)

    main_list_index = 0

    for index in range(len(main_list) + len(insertables)):
        if index in insertions_by_index:
            result_list.extend(insertions_by_index[index])
        else:
            if main_list_index < len(main_list):
                result_list.append(main_list[main_list_index])
                main_list_index += 1
            else:
               pass #Wenn main_list leer ist, und die indexe größer sind als die länge von main_list, einfach weiter machen.

    return result_list

def limited_random(input_list : list, number : int= 1) -> list:
    if not input_list:  # Überprüfen, ob die Liste leer ist
        return []  # Gibt eine leere Liste zurück, anstatt einen Fehler auszulösen
    
    if number == 0: return input_list
    return_list = []
    temp_input_list = input_list[:] #kopie um die original liste zu erhalten.
    for x in range(number):
        if not temp_input_list: #wenn die kopierte liste leer ist, breche die schleife ab.
            break
        random_element = random.choice(temp_input_list)
        temp_input_list.remove(random_element)
        return_list.append(random_element)
    return return_list


def add_to_inventory(inventory, items) -> list:
    if isinstance(items, str):
        items = [(1, items)]
    elif isinstance(items, list) and isinstance(items[0], (int, list)):
        if isinstance(items[0], int):
            items = [items]
    else:
        return inventory

    for quantity, item_name in items:
        if item_name in inventory.keys():
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity

    return inventory


def add_starting_gear(inventory, gear_list):
    counter = 0
    choices = []
    for key in gear_list:
        choices.append(random.choice(gear_list[key]))
    
    gear_list = []
    for line in choices:
        if isinstance(line[0], int) and isinstance(line[1], str):
            gear_list.append(line)
        elif isinstance(line[0], int) and isinstance(line[1], list) and isinstance(line[1][0], str):
            if not consistent_type(line[1]): raise TypeError(f"This list has inconsistent types\n{line[1]}")
            random_items = limited_random(line[1], line[0])
            for item in random_items:
                gear_list.append(item)
        elif isinstance(line[0], int) and isinstance(line[1], list) and isinstance(line[1][0], list):
            if not consistent_type(line[1]): raise TypeError(f"This list has inconsistent types\n{line[1]}")
            if line[0] == 0:
                for item in line[1]:
                    gear_list.append(item)
            else:
                random_items = limited_random(line[1], line[0])
                for item in random_items:
                    gear_list.append(item)
        elif isinstance(line[0], list) and isinstance(line[1], list):
            for item in line:
                gear_list.append(item)
        else:
            raise TypeError("some error occured...")

    for item in gear_list:
        if isinstance(item, list):
            inventory = add_to_inventory(inventory, item)

    return inventory


def consistent_type(input_list):
  if not input_list:
    return True
  types = {type(element) for element in input_list}
  return len(types) == 1
    
# MAIN CODE