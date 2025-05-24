from lib import dnd_utils, dicts, lists
from lib.dnd_utils import gend
from lib.dicts import pron
import char, player, angriff, objekt, random, fight_backend


spieler_dict = {
    "atrophaea": player.atrophaea,
    "ragelion" : player.ragelion,
    "cornelius": player.cornelius,
    "llolfaen" : player.llolfaen,
    "ryu"      : player.ryu
}

gegner_dict = {
    "benu_1" : char.Benu_Jäger(),
    "benu_2" : char.Benu_Jäger(),
    "benu_3" : char.Benu_Jäger(),
    "benu_4" : char.Benu_Jäger(),
    "benu_5" : char.Benu_Jäger()
}

aktion_dict = {
    "speerstoß" : objekt.Speer(),
}


kampfreihenfolge = fight_backend.get_kampfreihenfolge(spieler_dict, gegner_dict)
print("-----\n\n")

for char in kampfreihenfolge:
    print(f"\n\n{char[2].eigenname} ist am Zug!\n")
    print(char[2])
    print(f"Status: {char[2].status}")

    aktion = dnd_utils.get_user_input("str", f"Was wird {char[2].pronomen} tun?")

    if aktion not in aktion_dict:
        print("Error")
    else:
        angreifer = char[2]
        ziel = dnd_utils.get_user_input("str", f"Wen wird {char[2].pronomen} mit '{aktion.capitalize()}' angreifen?", spieler_dict.keys())
        ziel = spieler_dict[ziel]
        angriff.Waffenangriff().setup(waffe= aktion_dict[aktion], angreifer=char[2], ziel=ziel)
        