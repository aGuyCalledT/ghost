from char import Char
from lib import dicts, dnd_utils, lists
import random

class Angriff:
    def __init__(self, angreifer : Char, ziel : Char, treffer_wurf = None, vorteil = 0):
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
    def __init__(self, angreifer, ziel, treffer_wurf=None, vorteil=0, finesse = False, rüstungsdurchdringung = 0):
        super().__init__(angreifer, ziel, treffer_wurf, vorteil)
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
        flavor_text_list = dic_damage_text[keyword]
        flavor_text = random.choice(flavor_text_list)
        flavor_text = flavor_text.format(self.angreifer.name, self.ziel.name, self.schaden, self.schadensart)
        return flavor_text


class Speerstoß(Nahkampf):
    def __call__(self, angreifer, ziel, treffer_wurf=None, vorteil=0, finesse=True, rüstungsdurchdringung = 0):
        self.name = "Speerstoß"
        super().__init__(angreifer, ziel, treffer_wurf, vorteil, finesse, rüstungsdurchdringung)
        self.hit = self.get_hit_text()
        self.schaden = dnd_utils.würfeln("1D6+3")
        self.schadensart = "stich"
        if self.hit is None:
            self.bonus = self.angriffsbonus + self.angreifer.übungsbonus
            if self.bonus + self.treffer_wurf >= self.ziel.rüstungsklasse - rüstungsdurchdringung: self.hit = True
            else: self.hit = False

        if self.hit:
            print(self.get_damage_text("speer"))
        else:
            print(f"{self.angreifer.name} macht sich voll zum Affen und sticht in die Luft neben {self.ziel.name}")


flavor_text = [
    "{0} sticht {1} mit seinem Speer in die Brust und verursacht {2} {3}schaden!",
    "{0} stürmt auf {1} zu und rammt ihm seinen Speer in die Seite. {2} {3}schaden!",
    "Mit einem lauten Schrei stösst {0} seinen Speer in {1}s Bauch. {2} {3}schaden!",
    "{0} zielt sorgfältig und trifft {1} mit dem Speer in den Oberschenkel. {2} {3}schaden!",
    "{0} schleudert seinen Speer mit Wucht auf {1} und trifft ihn in die Schulter. {2} {3}schaden!",
    "Blitzschnell sticht {0} mit dem Speer nach {1} und trifft ihn in den Rücken. {2} {3}schaden!",
    "{0} führt einen geschickten Stich mit dem Speer aus und trifft {1} in den Hals. {2} {3}schaden!",
    "{0} packt seinen Speer fester und rammt ihn {1} in die Rippen. {2} {3}schaden!",
    "In einem Überraschungsangriff durchbohrt {0} {1}s Bein mit seinem Speer. {2} {3}schaden!",
    "{0} springt vor und versetzt {1} einen Stich in den Arm mit dem Speer. {2} {3}schaden!",
    "Mit einem präzisen Stoss trifft {0} {1} mit dem Speer in die Hand. {2} {3}schaden!",
    "{0} wirbelt herum und schleudert seinen Speer nach {1}, der ihn in den Fuss trifft. {2} {3}schaden!",
    "{0} stürzt sich auf {1} und begräbt seinen Speer in dessen Brustkorb. {2} {3}schaden!",
    "{1} kann {0}s Speer nicht ausweichen und wird in den Magen getroffen. {2} {3}schaden!",
    "Der Speer von {0} findet sein Ziel in {1}s Hüfte. {2} {3}schaden!",
    "{0} visiert {1} an und durchbohrt dessen Schulterblatt mit dem Speer. {2} {3}schaden!",
    "Mit einem kraftvollen Wurf trifft {0} {1} mit dem Speer in den Nacken. {2} {3}schaden!",
    "{0} rennt auf {1} zu und sticht ihm den Speer in den Kiefer. {2} {3}schaden!",
    "{1} taumelt zurück, als {0}s Speer ihn in die Schläfe trifft. {2} {3}schaden!",
    "{0} zielt mit dem Speer auf {1}s Herz und trifft. {2} {3}schaden!"
]

dic_damage_text = {
    "speer" : flavor_text
}









