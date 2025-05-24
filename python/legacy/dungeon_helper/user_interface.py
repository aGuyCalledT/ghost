import angriff, objekt
from lib import dnd_utils

angriff_liste = {
    "speer" : angriff.Waffenangriff().setup(waffe=objekt.Speer()),
    "wurfspeer" : angriff.Waffenangriff().setup(waffe=objekt.Wurfspeer()),
    "hellebarde" : angriff.Waffenangriff().setup(waffe=objekt.Hellebarde()),
    "kampfstab" : angriff.Waffenangriff().setup(waffe=objekt.Kampfstab())
}
print(angriff_liste.keys)
input_angriff = dnd_utils.get_user_input("str", "Welchen Angriff möchtest du berechnen?", valid_strings=angriff_liste.keys)


