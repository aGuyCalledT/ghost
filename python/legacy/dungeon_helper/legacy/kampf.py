from npcs import Benu
from spieler import cornelius, llolfaen, ryu, atrophaea, ragelion
import temp.angriff as angriff
import random
from lib.dice import würfeln
from lib.dnd_utils import get_user_input

dic_gegner = {
    "benu" : Benu()
}

spieler = [
    cornelius,
    llolfaen,
    ryu,
    atrophaea,
    ragelion
]

def get_random_player(spieler_liste = spieler):
    
    spieler_index = random.randint(0, len(spieler_liste)-1)
    return spieler_liste[spieler_index]

def setup(spieler_liste, gegner_liste):
    spawn_liste = []
    for spawn in gegner_liste:
        for x in range(spawn[1]):
            spawn_liste.append(dic_gegner[spawn[0]])
    return spawn_liste



# MAIN CODE

gegner = [
    ["benu", 10],
    ["benu",  5]
]
spawn_liste = setup(spieler_liste=spieler, gegner_liste=gegner)

for element in  spawn_liste:
    print(element)