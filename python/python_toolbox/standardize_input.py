from fuzzywuzzy import fuzz
from programs import utils

def standardize_input(user_input: str, keywords: list):
    split_input = user_input.split()
    return_input = []
    input_confidence = []
    for word in split_input:
        match_list = []
        for keyword in keywords:
            match_list.append(fuzz.ratio(keyword, word))
        match_prob = max(match_list)
        match_word = keywords[match_list.index(match_prob)]

        return_input.append(match_word)
        input_confidence.append(match_prob)

    if min(input_confidence) <= 75:
        correctness = utils.get_user_input("bool", f"Meintest du : '{" ".join(return_input)}'?")
        if correctness:
            return return_input
        else:
            return None

    else:
        return return_input
    return None  # Füge einen Rückgabewert hinzu, falls du den Durchschnitt der match_list, oder den höchsten Wert benötigst.


# MAIN CODE
keywords = ["Rojin", "Jale", "hat", "lieb", "Wale", "isst"]

reply = None
while reply is None:
    user_input = utils.get_user_input("str", "Gib einen Befehl ein")
    reply = standardize_input(user_input, keywords)

print(f"Der User_Input lautet: {reply}")