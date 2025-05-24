from lib import dnd_utils, lists, dicts
import random

class Char:
    def __init__(self, 
                 is_player=        False,
                 stufe=            1,
                 klasse=           "keine_klasse",
                 trefferpunkte=    10, 
                 rüstungsklasse=   None,
                 bewegungsrate=    9, 
                 hg= 0.25,
                 status=           [],
                 größe=            "normal",
                 allignment=       None, 
                 volk=             None, 
                 name=             "Bürger",
                 eigenname=        None,
                 gender=           None,
                 trans=            None,
                 sexualität=       None,
                 pronomen =        None,
                 bewegungsart=     ["l"], 
                 geübt=            [],
                 random_geübt=     3,
                 stärke=           10, 
                 konstitution=     10, 
                 geschicklichkeit= 10,
                 charisma=         10, 
                 weisheit=         10, 
                 intelligenz=      10,
                 ):

        # Informationen
        self.is_player = is_player
        self.stufe = stufe
        self.klasse = klasse
        self.bewegungsrate = bewegungsrate
        self.herausforderungsgrad = hg
        self.status = status

        self.größe = größe
        self.name = name
        self.gender, self.trans, self.sexualität = dnd_utils.get_personal_identity(gender, trans, sexualität)

        if volk is None: self.volk, self.namenskultur = dnd_utils.get_random_race(self.gender)
        else: self.volk, self.namenskultur = volk.lower(), volk.lower()
        if self.namenskultur.endswith(" "): self.namenskultur = self.namenskultur[:-1]

        if eigenname is None: self.eigenname = dnd_utils.get_random_name(self.namenskultur, gender=self.gender)
        else: self.eigenname = eigenname

        if pronomen is None: self.pronomen = dnd_utils.get_random_pronomen(self.gender)
        else:
            if pronomen in dicts.pron:
                self.pronomen = pronomen
            else:
                print(f"{self.eigenname}s Pronomen sind nicht valid!")

        self.bewegungsart = bewegungsart  # [l,f,s] --> laufen, fliegen, schwimmen
        self.geübt = geübt
        self.random_geübt = random_geübt

        if isinstance(trefferpunkte, str): self.trefferpunkte = dnd_utils.würfeln(trefferpunkte)
        elif isinstance(trefferpunkte, int): self.trefferpunkte = trefferpunkte
        else: raise TypeError("'Trefferpunkte' must be a roll or an int.")
        
        if allignment is None: self.allignment = dnd_utils.get_allignment()
        else: self.allignment = allignment

        # Attribute
        self.stärke, self.stärke_mod = stärke, dicts.attribut_mod[stärke]
        self.konstitution, self.konstitution_mod = konstitution, dicts.attribut_mod[konstitution]
        self.geschicklichkeit, self.geschicklichkeit_mod = geschicklichkeit, dicts.attribut_mod[geschicklichkeit]
        self.charisma, self.charisma_mod = charisma, dicts.attribut_mod[charisma]
        self.weisheit, self.weisheit_mod = weisheit, dicts.attribut_mod[weisheit]
        self.intelligenz, self.intelligenz_mod = intelligenz, dicts.attribut_mod[intelligenz]

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
        if rüstungsklasse is None: self.rüstungsklasse = 10 + self.geschicklichkeit_mod
        else: self.rüstungsklasse = rüstungsklasse

        self.übungsbonus = dnd_utils.get_übungsbonus(stufe)

        if random_geübt > 0:
            fert_temp = lists.fertigkeiten.copy()  # Make a copy to avoid modifying the original list
            for element in geübt:
                if element in fert_temp: 
                    fert_temp.remove(element)
            for x in range(random_geübt):
                if len(fert_temp) > 1:  # Check if there are at least two elements left
                    ind = random.randint(0, len(fert_temp) - 1)
                    geübt.append(fert_temp[ind])
                    fert_temp.pop(ind)
                else:
                    break  # Stop the loop if there are not enough elements left

        for i, fertigkeit in enumerate(self.fertigkeiten):
            if fertigkeit[0] in geübt:
                self.fertigkeiten[i][1] += self.übungsbonus  # Modifikator aktualisieren

        self.passive_wahrnehmung = 10 + self.fertigkeiten[17][1] 
        self.initiative = self.geschicklichkeit_mod + dnd_utils.würfeln("1D20")
        
        self.xp_wert = dicts.xp[hg]
        
        if self.klasse in dicts.zauberwirkungsbonus.keys():
            self.zauberwirkungsbonus = dicts.zauberwirkungsbonus[self.klasse][stufe]
        else:
            self.zauberwirkungsbonus = 0


    def __str__(self):
        gender_symbol = dicts.gender_symbol[self.gender]
        sexualität_symbol = dicts.sexualität_symbol[self.sexualität]
        if self.status == []:   display_status = ""
        else:                   display_status = self.status

        line_1 = f"\033[4m{self.name} ({self.volk.capitalize()}) '{self.eigenname}'\033[0m {gender_symbol} {sexualität_symbol}"
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
        if status_input not in lists.status_effekt: return False
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


class Benu_Jäger(Char):
    def __init__(self, 
                 is_player=False,
                 stufe=3, 
                 klasse="keine_klasse", 
                 trefferpunkte= "4D8+4", 
                 rüstungsklasse=12, 
                 bewegungsrate=9, 
                 hg=3, 
                 status=[], 
                 größe="normal", 
                 allignment=None, 
                 volk="benu", 
                 name="Benu Jäger", 
                 eigenname=None, 
                 gender=None, 
                 trans=None, 
                 sexualität=None, 
                 pronomen=None, 
                 bewegungsart=["l"], 
                 geübt=[], 
                 random_geübt=3, 
                 stärke=10, 
                 konstitution=12, 
                 geschicklichkeit=16, 
                 charisma=10, 
                 weisheit=16, 
                 intelligenz=12):
        super().__init__(is_player, stufe, klasse, trefferpunkte, rüstungsklasse, bewegungsrate, hg, status, größe, allignment, volk, name, eigenname, gender, trans, sexualität, pronomen, bewegungsart, geübt, random_geübt, stärke, konstitution, geschicklichkeit, charisma, weisheit, intelligenz)

class Benu_Ritter(Char):
    def __init__(self, 
                 is_player=False, 
                 stufe=4, 
                 klasse="keine_klasse", 
                 trefferpunkte="6D8+4", 
                 rüstungsklasse=16, 
                 bewegungsrate=9, 
                 hg=4, 
                 status=[], 
                 größe="normal", 
                 allignment=None, 
                 volk="benu", 
                 name="Benu Ritter", 
                 eigenname=None, 
                 gender=None, 
                 trans=None, 
                 sexualität=None, 
                 pronomen=None, 
                 bewegungsart=["l"], 
                 geübt=[], 
                 random_geübt=3, 
                 stärke=21, 
                 konstitution=17, 
                 geschicklichkeit=8, 
                 charisma=8, 
                 weisheit=10, 
                 intelligenz=6):
        super().__init__(is_player, stufe, klasse, trefferpunkte, rüstungsklasse, bewegungsrate, hg, status, größe, allignment, volk, name, eigenname, gender, trans, sexualität, pronomen, bewegungsart, geübt, random_geübt, stärke, konstitution, geschicklichkeit, charisma, weisheit, intelligenz)

class Benu_Magi(Char):
    def __init__(self, 
                 is_player=False,
                 stufe=3, 
                 klasse="keine_klasse", 
                 trefferpunkte= "4D8+4", 
                 rüstungsklasse=12, 
                 bewegungsrate=9, 
                 hg=3, 
                 status=[], 
                 größe="normal", 
                 allignment=None, 
                 volk="benu", 
                 name="Benu Magi", 
                 eigenname=None, 
                 gender=None, 
                 trans=None, 
                 sexualität=None, 
                 pronomen=None, 
                 bewegungsart=["l"], 
                 geübt=[], 
                 random_geübt=3, 
                 stärke=10, 
                 konstitution=12, 
                 geschicklichkeit=12, 
                 charisma=14, 
                 weisheit=16, 
                 intelligenz=20):
        super().__init__(is_player, stufe, klasse, trefferpunkte, rüstungsklasse, bewegungsrate, hg, status, größe, allignment, volk, name, eigenname, gender, trans, sexualität, pronomen, bewegungsart, geübt, random_geübt, stärke, konstitution, geschicklichkeit, charisma, weisheit, intelligenz)