from lib import dnd_utils

def get_kampfreihenfolge(spieler_dict, gegner_dict):
    if spieler_dict is None:
        char_list = list(gegner_dict.keys())
    elif gegner_dict is None:
        char_list = list(spieler_dict.keys())
    else:
        char_list = list(spieler_dict.keys()) + list(gegner_dict.keys())
    
    kampfreihenfolge = []
    
    for char in char_list:
        if char in spieler_dict:
            initiative = dnd_utils.get_user_input("int", f"{char}, was ist deine Initiative?")
            char_object = spieler_dict[char]

        elif char in gegner_dict:
            initiative = gegner_dict[char].initiative
            char_object = gegner_dict[char]
            

        kampfreihenfolge.append([char, initiative, char_object])
    
    sortierte_kampfreihenfolge = sorted(kampfreihenfolge, key = lambda item: item[1], reverse=True)

    display_kampfreihenfolge(sortierte_kampfreihenfolge, gegner_dict)

    return sortierte_kampfreihenfolge


def display_kampfreihenfolge(kampfreihenfolge, gegner_dict):
    counter = 0
    round_numb = len(kampfreihenfolge)
    if round_numb > 9: leading_zero = True
    else: leading_zero = False

    print("\n")
    for line in kampfreihenfolge:
        counter += 1
        if leading_zero: display_turn_counter = f"{counter:02d}"
        else: display_turn_counter = f"{counter}"
        
        char_name = ""
        if line[0] in gegner_dict:
            char_name = f" ({gegner_dict[line[0]].eigenname})"

        print(f"{display_turn_counter}. {line[0].capitalize()}{char_name}")

