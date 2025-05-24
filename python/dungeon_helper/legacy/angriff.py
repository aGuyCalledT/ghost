from char import Char
from lib import dicts, dnd_utils, lists
import random, math
import objekt

class Angriff():
    def setup(self, angreifer : Char, ziel : Char, treffer_wurf = None, vorteil = 0):
        if isinstance(ziel, list) and all(isinstance(element, Char) for element in self.ziel):
            self.ziel_anzahl = len(ziel)
        elif isinstance(ziel, Char):
            self.ziel_anzahl = 1
        else:
            raise TypeError(f"'{self.ziel}' ist kein gültiges Ziel. Es muss ein Objekt der Klasse Char(), oder ein Tochterobjekt davon sein.")
        
        self.angreifer = angreifer
        self.ziel = ziel
        self.treffer_wurf = treffer_wurf
        self.schaden = None
        self.schadensart = None

        if treffer_wurf is not None: self.treffer_wurf = treffer_wurf
        else:
            if vorteil >= 0:
                vorteil_auf_wurf = True
            else:
                vorteil_auf_wurf = False 
                vorteil = vorteil * (-1)
            
            würfe = []
            for x in range(vorteil + 1):
                roll = dnd_utils.würfeln("1D20")
                würfe.append(roll)

            würfe.sort()
            if vorteil_auf_wurf:
                self.treffer_wurf = würfe[-1]
            else:
                self.treffer_wurf = würfe[0]

        self.critical_hit, self.critical_miss = False, False
        if self.treffer_wurf == 20: self.critical_hit = True
        elif self.treffer_wurf == 1: self.critical_miss = True

class Nahkampf(Angriff):
    def setup(self, angreifer: Char, ziel: Char, treffer_wurf=None, vorteil=0, finesse=False, rüstungsdurchdringung=0):
        super().setup(angreifer, ziel, treffer_wurf, vorteil)

        self.finesse = finesse
        if self.finesse:
            if self.angreifer.stärke_mod > self.angreifer.geschicklichkeit_mod:
                self.angriffsbonus = self.angreifer.stärke_mod
            else:
                self.angriffsbonus = self.angreifer.geschicklichkeit_mod
        else:
            self.angriffsbonus = self.angreifer.stärke_mod
        self.angriffsbonus += self.angreifer.übungsbonus

    def get_hit_text(self):
        if self.critical_hit:
            print(f"{self.angreifer.name} landet einen kritischen Treffer gegen {self.ziel.name}!")
            return True
        elif self.critical_miss:
            print(f"{self.angreifer.name} hat {self.ziel.name} kritisch verfehlt!")
            return False
        else:
            print(f"{self.angreifer.name} hat eine {self.treffer_wurf + self.angriffsbonus} ({self.treffer_wurf}+{self.angriffsbonus}) gewürfelt.")
            return None
    
    def get_damage_text(self, keyword = "speer"):
        return None


class Waffenangriff(Nahkampf):
    def setup(self, angreifer, ziel, waffe : objekt.Waffe, treffer_wurf=None, vorteil=0, finesse=False, rüstungsdurchdringung=0):
        self.waffe = waffe
        self.angreifer = angreifer
        self.rüstungsdurchdringung = rüstungsdurchdringung

        if self.waffe.finesse:
            self.finesse = True
        else:
            self.finesse = False
        if self.waffe.schwer and self.angreifer.größe in ["klein", "winzig"]:
            vorteil -= 1

        super().setup(angreifer, ziel, treffer_wurf, vorteil, finesse = self.finesse, rüstungsdurchdringung = self.rüstungsdurchdringung)

        self.schadens_wurf = self.waffe.schaden
        self.waffenname = self.waffe.name
        self.waffen_gend = self.waffe.waffen_gend
        self.falvor_text_kategorie = "waffe"
        self.schadensart = self.waffe.schadensart

        self.name = f"{self.waffe.name} Angriff"
        self.hit = self.get_hit_text()
        self.schaden = dnd_utils.würfeln(self.schadens_wurf)

        if self.critical_hit: # critical hit
            self.schaden += dnd_utils.würfeln(self.schadens_wurf)
        elif self.critical_miss: # critical miss
            self.schaden = math.floor(self.schaden/3)

        elif self.hit is None: # hit
            self.bonus = self.angriffsbonus + self.angreifer.übungsbonus
            if self.bonus + self.treffer_wurf >= self.ziel.rüstungsklasse - rüstungsdurchdringung: self.hit = True
            else: self.hit = False
        
        flavor_text = get_flavor_text(self.critical_hit, self.critical_miss, self.hit, self.falvor_text_kategorie, self.waffenname, self.schadensart)
        flavor_text = flavor_text.format(self.angreifer.pronomen.capitalize(), self.ziel.eigenname, dnd_utils.pos_pron(self.angreifer.pronomen, self.waffen_gend, "dat"), self.waffenname.capitalize(), self.schaden, self.schadensart.capitalize())
        print(flavor_text)
        

def get_flavor_text(critical_hit = False, critical_miss = False, hit = True, angriffsart = "nahkampf", angriff_waffe = "faust", schadensart = "hieb"):
    if critical_hit: hit = True
    elif critical_miss: hit = False

    if hit:
        if critical_hit:
            hit_art = "crit_hit"
        else:
            hit_art = "hit"
    else:
        if critical_miss:
            hit_art = "crit_miss"
        else:
            hit_art = "miss"
    attack_text = random.choice(flavor_text[angriffsart][hit_art][0])
    return attack_text

flavor_text= {
    "waffenlos" : {
        "crit_hit": [
            lists.waffenlos_flavor_text[0]
        ],
        "hit": [
            lists.waffenlos_flavor_text[1]
        ],
        "crit_miss": [
            lists.waffenlos_flavor_text[2]
        ],
        "miss": [
            lists.waffenlos_flavor_text[3]
        ]
    },
    "nahkampf" : {
        "crit_hit": [

        ],
        "hit": [

        ],
        "crit_miss": [

        ],
        "miss": [

        ]
    },
    "waffe": {
        "crit_hit": [
            lists.waffenlos_flavor_text[0]

        ],
        "hit": [
            lists.waffenlos_flavor_text[1]

        ],
        "crit_miss": [
            lists.waffenlos_flavor_text[2]

        ],
        "miss": [
            lists.waffenlos_flavor_text[3]

        ]
    }
}    

class Zauber():
    def setup(self, name, zauber_wirker : Char, ziel = None):
        self.name = name
        self.zauber_wirker = zauber_wirker
        self.ziel = ziel

class projektil_zauber(Zauber):
    def setup(self, name, zauber_wirker, ziel=None):
        super().setup(name, zauber_wirker, ziel)

        self.zauber_attribut = zauber_wirker.get_mod(dicts.zauber_attribut[zauber_wirker.klasse])
        self.zauber_angriffsbonus =  self.zauber_attribut + zauber_wirker.übungsbonus

class aoe_zauber(Zauber):
    def setup(self, name, zauber_wirker, ziel=None):
        super().setup(name, zauber_wirker, ziel)

class inst_zauber(Zauber):
    def setup(self, name, zauber_wirker, ziel=None):
        super().setup(name, zauber_wirker, ziel)

class feuer_pfeil(projektil_zauber):
    def setup(self, name, zauber_wirker, ziel=None):
        super().setup(name, zauber_wirker, ziel)






