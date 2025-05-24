import random
from lib.dice import würfeln
import numpy as np

dic_attribut_mod = {
    1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1,
    13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7,
    25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10
}
dic_xp = {
    0: 10, 0.125: 25, 0.25: 50, 0.5: 100, 1: 200, 2: 450, 3: 700, 4: 1100, 5: 1800, 6: 2300,
    7: 2900, 8: 3900, 9: 5000, 10: 5900, 11: 7200, 12: 8400, 13: 10000, 14: 11500, 15: 13000,
    16: 15000, 17: 18000, 18: 20000, 19: 22000, 20: 25000, 21: 33000, 22: 41000, 23: 50000,
    24: 62000, 30: 155000,
}
dic_zauberklassen = {"barde", "kleriker", "druide", "hexenmeister", "magier", "paladin", "waldläufer", "zauberer"}
dic_zauberwirkungsbonus = {
    "barde": {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 4, 7: 4, 8: 4, 9: 5, 10: 5, 11: 5, 12: 5, 13: 6, 14: 6, 15: 6, 16: 6, 17: 7, 18: 7, 19: 7, 20: 7},
    "kleriker": {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 4, 7: 4, 8: 4, 9: 5, 10: 5, 11: 5, 12: 6, 13: 6, 14: 6, 15: 6, 16: 7, 17: 7, 18: 7, 19: 7, 20: 8},
    "druide": {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 4, 7: 4, 8: 4, 9: 5, 10: 5, 11: 5, 12: 6, 13: 6, 14: 6, 15: 6, 16: 7, 17: 7, 18: 7, 19: 7, 20: 8},
    "hexenmeister": {1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 4, 8: 5, 9: 5, 10: 5, 11: 6, 12: 6, 13: 6, 14: 7, 15: 7, 16: 7, 17: 8, 18: 8, 19: 8, 20: 9},
    "magier": {1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 4, 8: 5, 9: 5, 10: 5, 11: 6, 12: 6, 13: 6, 14: 7, 15: 7, 16: 7, 17: 8, 18: 8, 19: 8, 20: 9},
    "paladin": {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 3, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 5, 19: 5, 20: 5},
    "waldläufer": {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 3, 13: 3, 14: 3, 15: 4, 16: 4, 17: 4, 18: 4, 19: 5, 20: 5},
    "zauberer": {1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 4, 8: 5, 9: 5, 10: 5, 11: 6, 12: 6, 13: 6, 14: 7, 15: 7, 16: 7, 17: 8, 18: 8, 19: 8, 20: 9},

    "barbar"      : {None : None},
    "kämpfer"     : {None : None},
    "mönch"       : {None : None},
    "schurke"     : {None : None},
    "artifizient" : {None : None}
}

status_effekt = ["blind", "bezaubert", "taub", "verängstigt", "gepackt", "kampfunfähig", "unsichtbar", "gelähmt", "versteinert", "vergiftet", "liegend", "festgesetzt", "betäubt", "bewusstlos", "tot"]

elfen_silben = [
    "a", "ae", "aer", "ah", "ai", "al", "ala", "an", "ana", "ar", "ara", 
    "as", "atha", "au", "e", "ea", "el", "ela", "en", "ena", "er", "era", 
    "es", "eth", "ev", "eya", "fa", "fae", "fal", "far", "fe", "fi", "fin", 
    "fir", "ga", "gae", "gal", "gar", "ge", "gil", "gla", "ha", "hae", "hal", 
    "har", "he", "hi", "ia", "iel", "il", "ila", "in", "ina", "ir", "ira", 
    "is", "ith", "iv", "iya", "ka", "kae", "kal", "kar", "ke", "ki", "la", 
    "lae", "lan", "lar", "le", "li", "lin", "lir", "lo", "lor", "lu", "lya", 
    "ma", "mae", "mal", "mar", "me", "mi", "min", "mir", "na", "nae", "nal", 
    "nar", "ne", "ni", "nin", "nir", "no", "nor", "nu", "nya", "o", "or", 
    "ra", "rae", "ral", "ran", "re", "ri", "rin", "ro", "ror", "ru", "rya", 
    "sa", "sae", "sal", "sar", "se", "si", "sil", "ta", "tae", "tal", "tar", 
    "te", "tha", "thi", "ti", "va", "vae", "val", "var", "ve", "vi", "vin", 
    "ya", "yel", "yra", "ys"
]

goblin_silben = [
    "ag", "ak", "arg", "ark", "az", "bag", "bak", "barg", "bark", "baz", 
    "blag", "brak", "brag", "brark", "bug", "buk", "burg", "burk", "buz", 
    "dag", "dak", "darg", "dark", "daz", "drag", "drak", "dreg", "dre", 
    "dro", "dug", "duk", "dur", "durk", "fag", "fak", "farg", "fark", 
    "faz", "frag", "frak", "freg", "frek", "frog", "fruk", "gag", "gak", 
    "garg", "gark", "gaz", "grag", "grak", "greg", "grek", "grog", "grok", 
    "grub", "guk", "gur", "gurk", "hag", "hak", "harg", "hark", "haz", 
    "hrag", "hrak", "hreg", "hrek", "hrug", "huk", "hur", "hurk", "jag", 
    "jak", "jarg", "jark", "jaz", "krag", "krak", "kreg", "krek", "krog", 
    "krok", "kug", "kuk", "kur", "kurk", "lag", "lak", "larg", "lark", 
    "laz", "mag", "mak", "marg", "mark", "maz", "nag", "nak", "narg", 
    "nark", "naz", "og", "ok", "org", "ork", "oz", "rag", "rak", "rarg", 
    "rark", "raz", "reg", "rek", "rog", "rok", "rug", "ruk", "sag", "sak", 
    "sarg", "sark", "ska", "sna", "snik", "snu", "snuk", "stag", "stak", 
    "streg", "strek", "surg", "surk", "tag", "tak", "targ", "tark", "taz", 
    "trag", "trak", "treg", "trek", "tro", "trok", "tug", "tuk", "tur", "urk",
    "zag", "zak", "zarg", "zark", "zog", "zok", "zug", "zuk", "zur", "zurk"
]

benu_silben = [
    "ac", "atl", "cal", "can", "catl", "chal", "chi", "chimal", "coatl", 
    "co", "cuauh", "e", "ecatl", "el", "hua", "hui", "ic", "itzt", "ix", 
    "li", "ma", "mal", "matl", "me", "Metz", "mi", "mic", "moc", "nahua", 
    "nan", "ne", "nen", "oc", "ohtli", "ol", "olli", "otl", "pa", "pal", 
    "qua", "quetzal", "qui", "te", "tec", "tecuhtli", "teo", "teotl", "tetl", 
    "tli", "tla", "tlac", "tlan", "tlat", "to", "toc", "ton", "tonatiuh", 
    "ua", "x", "xi", "xic", "xoch", "xochi", "ya", "yac", "yotl", "zac", 

    # Kombinationsmöglichkeiten für längere Namen (ohne "-"):
    "a", "atl", "cal", "can", "catl", "chal", "chi", "chimal", "coatl", 
    "co", "cuauh", "e", "ecatl", "el", "hua", "hui", "ic", "itzt", "ix", 
    "li", "ma", "mal", "matl", "me", "Metz", "mi", "mic", "moc", "nahua", 
    "nan", "ne", "nen", "oc", "ohtli", "ol", "olli", "otl", "pa", "pal", 
    "qua", "quetzal", "qui", "te", "tec", "tecuhtli", "teo", "teotl", "tetl", 
    "tli", "tla", "tlac", "tlan", "tlat", "to", "toc", "ton", "tonatiuh", 
    "ua", "x", "xi", "xic", "xoch", "xochi", "ya", "yac", "yotl", "zac",

    # Endungen (ohne "-"):
    "a", "atl", "cal", "can", "catl", "chal", "chi", "chimal", "coatl", 
    "co", "cuauh", "e", "ecatl", "el", "hua", "hui", "ic", "itzt", "ix", 
    "li", "ma", "mal", "matl", "me", "Metz", "mi", "mic", "moc", "nahua", 
    "nan", "ne", "nen", "oc", "ohtli", "ol", "olli", "otl", "pa", "pal", 
    "qua", "quetzal", "qui", "te", "tec", "tecuhtli", "teo", "teotl", "tetl", 
    "tli", "tla", "tlac", "tlan", "tlat", "to", "toc", "ton", "tonatiuh", 
    "ua", "x", "xi", "xic", "xoch", "xochi", "ya", "yac", "yotl", "zac"
]

dic_gender = {
      "m": "♂",
      "w": "♀",
      "d": "🜨"
  }

dic_trans = {
    True : "⚧",
    False: ""
}

gender_list = ["m", "w", "d"]

dic_sexualität = {
    "lesbisch" : "⚢",
    "schwul" : "⚣",
    "pan" : "⚤",
    "ace" : "⚲",
    "hetero" : ""
}

# Definition der Basisklasse Gegner
class Gegner:
    def __init__(self, 
                 stufe=                1,
                 klasse=               "barbar",
                 stärke=               10, 
                 konstitution=         10, 
                 geschicklichkeit=     10,
                 charisma=             10, 
                 weisheit=             10, 
                 intelligenz=          10, 
                 trefferpunkte=        "2D8", 
                 rüstungsklasse=       10,
                 bewegungsrate=        9, 
                 herausforderungsgrad= 0.25,
                 status =              [],

                 größe=                "Mittelgroß",
                 allignment=           "Neutral Neutral", 
                 volk=                 "Mensch", 
                 name=                 "Bauer",
                 eigenname =           "None",
                 gender =              None,
                 trans =               None,
                 sexualität =          None,
                 bewegungsart=         ["l"], 
                 geübt=                [],
                 random_geübt =        0
                 ):

        # Informationen
        self.stufe = stufe
        self.klasse = klasse
        self.größe = größe
        self.rüstungsklasse = rüstungsklasse
        self.bewegungsrate = bewegungsrate
        self.allignment = allignment
        self.volk = volk
        self.name = name
        self.eingenname = eigenname
        self.bewegungsart = bewegungsart  # [l,f,s] --> laufen, fliegen, schwimmen
        self.geübt = geübt
        self.random_geübt = random_geübt

        self.herausforderungsgrad = herausforderungsgrad
        self.xp_wert = dic_xp[herausforderungsgrad]

        self.trefferpunkte = würfeln(trefferpunkte)
        self.status = status

        # Attribute
        self.stärke = stärke
        self.stärke_mod = dic_attribut_mod[stärke]

        self.konstitution = konstitution
        self.konstitution_mod = dic_attribut_mod[konstitution]

        self.geschicklichkeit = geschicklichkeit
        self.geschicklichkeit_mod = dic_attribut_mod[geschicklichkeit]

        self.charisma = charisma
        self.charisma_mod = dic_attribut_mod[charisma]

        self.weisheit = weisheit
        self.weisheit_mod = dic_attribut_mod[weisheit]

        self.intelligenz = intelligenz
        self.intelligenz_mod = dic_attribut_mod[intelligenz]

        # Fertigkeiten - Korrigierte Initialisierung mit runden Klammern
        self.fertigkeiten = (
            ["akrobatik", self.geschicklichkeit_mod],
            ["arkane_kunde", self.intelligenz_mod],
            ["athletik", self.stärke_mod],
            ["auftreten", self.charisma_mod],
            ["einschüchtern", self.charisma_mod],
            ["fingerfertigkeit", self.geschicklichkeit_mod],
            ["geschichte", self.intelligenz_mod],
            ["heilkunde", self.weisheit_mod],
            ["heimlichkeit", self.geschicklichkeit_mod],
            ["mit_tieren_umgehen", self.weisheit_mod],
            ["motiv_erkennen", self.weisheit_mod],
            ["nachforschungen", self.intelligenz_mod],
            ["naturkunde", self.intelligenz_mod],
            ["religion", self.intelligenz_mod],
            ["täuschen", self.charisma_mod],
            ["überlebenskunst", self.weisheit_mod],
            ["überzeugen", self.charisma_mod],
            ["wahrnehmung", self.weisheit_mod]
        )

        # Übungsbonus
        if self.stufe <= 4:
            self.übungsbonus = 2
        elif self.stufe <= 8:
            self.übungsbonus = 3
        elif self.stufe <= 12:
            self.übungsbonus = 4
        elif self.stufe <= 16:
            self.übungsbonus = 5
        elif self.stufe <= 20:
            self.übungsbonus = 6
        else:
            self.übungsbonus = 7

        if random_geübt > 0:
            fertigkeiten = ['akrobatik', 'arkane_kunde', 'athletik', 'auftreten', 'einschüchtern', 'fingerfertigkeit', 'geschichte', 'heilkunde', 'heimlichkeit', 'mit_tieren_umgehen', 'motiv_erkennen', 'nachforschungen', 'naturkunde', 'religion', 'täuschen', 'überlebenskunst', 'überzeugen', 'wahrnehmung']
            for element in geübt:
                if element in fertigkeiten: fertigkeiten.remove(element)
            for x in range(random_geübt):
                ind = random.randint(0, len(fertigkeiten) - 1)  # Beachte die Anpassung hier
                geübt.append(fertigkeiten[ind])  # Korrigierte Zeile
                fertigkeiten.pop(ind)
        
        if self.klasse in dic_zauberklassen:
            self.zauberwirkungsbonus = dic_zauberwirkungsbonus[self.klasse][stufe]
        else:
            self.zauberwirkungsbonus = 0

                

        # Anwendung des Übungsbonus auf geübte Fertigkeiten
        for i, fertigkeit in enumerate(self.fertigkeiten):
            if fertigkeit[0] in geübt:
                self.fertigkeiten[i][1] += self.übungsbonus  # Modifikator aktualisieren

        self.passive_wahrnehmung = 10 + self.fertigkeiten[17][1] 
        self.initiative = self.geschicklichkeit_mod 


    def __str__(self):
        if self.status == []:   display_status = ""
        else:                   display_status = self.status

        line_1 = f"\033[4m{self.name} '{self.eingenname}'\033[0m"
        line_2 = f"| {self.trefferpunkte}TP | {display_status}"
        return f"{line_1}\n{line_2}"
    

    def get_mod(self, name):
        # Überprüfen, ob es sich um eine Fertigkeit handelt
        name = name.lower()

        for fertigkeit in self.fertigkeiten:
            if fertigkeit[0] == name:
                return fertigkeit[1]

        attribute = {
            "stärke": self.stärke_mod,
            "geschicklichkeit": self.geschicklichkeit_mod,
            "konstitution": self.konstitution_mod,
            "intelligenz": self.intelligenz_mod,
            "weisheit": self.weisheit_mod,
            "charisma": self.charisma_mod
        }
        if name in attribute:
            return attribute[name]

        return None  # Weder Fertigkeit noch Attribut gefunden
    
    def status_ändern (self, status_input, add = True):
        if status_input not in status_effekt: return False
        if status_input not in self.status:
            if add: 
                self.status.append(status_input)
                return True
            else: 
                return None
        elif status_input in self.status:
            if add:
                return None
            else:
                self.status.remove(status_input)
                return True
        else:
            print("Error: Status Fehler")


def get_random_name(silben_liste, silben_zahl_1 = [2, 2, 2, 3, 3, 4], silben_zahl_2 = [1, 2, 2, 2, 3, 3], nachname_wahrscheinlichkeit = 3):
    while True:
        name_1 = ""
        name_2 = ""
        silben_name_1 = random.choice(silben_zahl_1)
        if random.randint(1, nachname_wahrscheinlichkeit) == nachname_wahrscheinlichkeit:
            silben_name_2 = random.choice(silben_zahl_2)
        else:
            silben_name_2 = None
        
        for x in range(silben_name_1):
            name_1 += random.choice(silben_liste).lower()
        name_1 = name_1.capitalize()
        
        
        if silben_name_2 is not None:
            for x in range(silben_name_2):
                name_2 += random.choice (silben_liste).lower()
            name_2 = name_2.capitalize()
            
        if len(name_1 + name_2) <= 16:
            break
    if name_2 is None or name_2 == "":
        gap = ""
    else:
        gap = " "

    return f"{name_1}{gap}{name_2}"

