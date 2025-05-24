import shutil
import os
import random
from lib import dnd_utils, lists, dicts

def printlb(text = None):

    konsolenbreite = shutil.get_terminal_size().columns

    if text is None:
        return konsolenbreite
    
    woerter = text.split()
    aktuelle_zeile = ""
    erste_wort_im_text = True 

    for wort in woerter:
        if len(aktuelle_zeile + wort) + 1 > konsolenbreite:
            print(aktuelle_zeile)
            aktuelle_zeile = wort 
            erste_wort_in_zeile = False 
        else:
            if erste_wort_im_text:
                aktuelle_zeile += wort
                erste_wort_im_text = False
            else: 
                aktuelle_zeile += " " + wort

    if aktuelle_zeile:
        print(aktuelle_zeile)


def check_int_within_bounds(value, min_int=None, max_int=None):
  if min_int is not None and value < min_int:
    return False

  if max_int is not None and value > max_int:
    return False

  return True


def get_user_input(input_type, input_message=None, valid_strings=None, min_int=None, max_int=None):
    while True:
        if input_message is None:
            user_input = input(f"\n> ").lower()
        else:
            user_input = input(f"\n{input_message}\n> ").lower()

        if input_type == 'str':
            if valid_strings is None:
                return user_input
            elif user_input in valid_strings:
                return user_input
            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine der folgenden Optionen:\n", valid_strings)

        elif input_type == 'int':
            try:
                user_input_valid_int = int(user_input)
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
            else:
                if check_int_within_bounds(user_input_valid_int, min_int, max_int):
                    return user_input_valid_int
                else:
                    print(f"Ungültiger Wert. Der Wert muss zwischen {min_int} und {max_int} liegen.")
                    continue  # Hier fordern wir einen neuen Input an

        elif input_type == 'path':
            if os.path.exists(user_input):
                return user_input
            else:
                print("Ungültiger Dateipfad. Bitte geben Sie einen existierenden Pfad ein.")

        elif input_type == 'bool':
            if user_input.lower() in ['y', 'yes', 'j', 'ja']:
                return True
            elif user_input.lower() in ['n', 'no', 'nein']:
                return False
            else:
                print("Ungültige Eingabe. Die Eingabe muss 'ja' oder 'nein' sein.")
        

        else:
            raise ValueError(f"Ungültiger Wert. Die Eingabe muss {input_type} sein")
        

def würfeln(ausdruck):
    # Teilen des Ausdrucks in seine Bestandteile
    teile = ausdruck.split('D')
    if len(teile) != 2:
        try: return int(ausdruck)
        except:
            raise ValueError(f"'{ausdruck}' Ist ein ungültiger Ausdruck. Bitte verwenden Sie das Format 'XdY+Z'.")

    anzahl_wuerfel = 1 if teile[0] == '' else int(teile[0])
    wuerfel_art, modifikator = teile[1].split('+') if '+' in teile[1] else (teile[1], 0)
    wuerfel_art = int(wuerfel_art)
    modifikator = int(modifikator)

    # Würfeln
    ergebnis = 0
    for _ in range(anzahl_wuerfel):
        ergebnis += random.randint(1, wuerfel_art)

    # Modifikator hinzufügen
    ergebnis += modifikator

    return ergebnis


def get_übungsbonus(stufe : int):
    if stufe <= 4:
        return 2
    elif stufe <= 8:
        return 3
    elif stufe <= 12:
        return 4
    elif stufe <= 16:
        return 5
    elif stufe <= 20:
        return 6
    else:
        return 7
    

def get_random_index(wahrscheinlichkeit_liste: list):
    if not isinstance(wahrscheinlichkeit_liste, list) or not all(isinstance(unterliste, list) for unterliste in wahrscheinlichkeit_liste):
        raise ValueError("Die Liste muss zweidimensional sein.")

    # Berechnung der Gesamtsumme der Wahrscheinlichkeiten
    gesamtsumme = sum(wahrscheinlichkeit[1] for wahrscheinlichkeit in wahrscheinlichkeit_liste)

    kumulative_wahrscheinlichkeiten = []
    summe = 0

    for wert, wahrscheinlichkeit in wahrscheinlichkeit_liste:
        summe += wahrscheinlichkeit
        kumulative_wahrscheinlichkeiten.append(summe)

    # Skalierung der Zufallszahl basierend auf der Gesamtsumme
    zufallszahl = random.uniform(0, gesamtsumme)

    for i, kumulative_wahrscheinlichkeit in enumerate(kumulative_wahrscheinlichkeiten):
        if zufallszahl <= kumulative_wahrscheinlichkeit:
            return wahrscheinlichkeit_liste[i][0]
        
def get_personal_identity(gender = None, trans = None, sexualität = None):
    if gender is None:
        gender = get_random_index(lists.gender_chance)
    if trans is None:
        trans = get_random_index(lists.trans_chance)
    if sexualität is None:
        sexualität = get_random_index(lists.sexualität_chance)
        if (trans == "trans" or gender == "divers") and sexualität == "heterosexuell":
            sexualität = get_random_index(lists.sexualität_chance)

    if gender == "weiblich" and sexualität == "homosexuell":
        sexualität = "lesbisch"
    elif gender == "männlich" and sexualität == "homosexuell":
        sexualität = "schwul"
    
    return gender, trans, sexualität

def get_allignment(probability_lawfulness = None, probability_goodness = None, wiederholung = False):
    if probability_lawfulness is None:
        lawfulness = get_random_index(lists.allignment_lawfulness)
    else:
        temp_lawfulnes = []
        for x in range(3):
            temp_lawfulnes.append([lists.allignment_lawfulness[x][0], probability_lawfulness[x]])
            lawfulness = get_random_index(temp_lawfulnes)

    if probability_goodness is None:
        goodness = get_random_index(lists.allignment_goodness)
    else:
        temp_goodness = []
        for x in range(3):
            temp_goodness.append([lists.allignment_goodness[x][0], probability_goodness[x]])
            goodness = get_random_index(temp_goodness)
    
    allignment = f"{lawfulness} {goodness}"

    if allignment == "Neutral Neutral" and wiederholung is False:
        allignment = get_allignment(probability_lawfulness, probability_goodness, wiederholung=True)
    
    elif allignment == "Neutral Neutral" and wiederholung is True:
        allignment = "True Neutral"

    return allignment

def get_random_name(namens_kultur, silben_zahl = [2, 2, 2, 2, 2, 2, 3, 3, 4], gender = "männlich"):
    silben_in_name = random.choice(silben_zahl)
    silben_liste = dicts.namens_kultur[namens_kultur]
    tries = 0

    if namens_kultur not in lists.poly_tabellarisch:
        while True:
            tries += 1
            name = ""
            for x in range(silben_in_name):
                name += random.choice(silben_liste)
            if (is_readable(name) or tries >= 10) and name not in lists.verwendete_namen: break

    else:
        silben_in_name -= 1
        while True:
            tries += 1
            name = ""
            for x in range(silben_in_name):
                name += random.choice(silben_liste[0])
            if gender == "weiblich":
                name += random.choice(silben_liste[2])
            else:
                name += random.choice(silben_liste[1])
            if (is_readable(name) or tries >= 10) and name not in lists.verwendete_namen: break
    lists.verwendete_namen.append(name)
    return name.capitalize()

def is_readable(text):
  vokale = "aeiouäöü"
  konsonanten = "bcdfghjklmnpqrstvwxyz"
  if len(text) < 3:
      return False

  for i in range(len(text) - 2):
      drei_zeichen = text[i:i+3].lower()
      if all(zeichen in vokale for zeichen in drei_zeichen):
          return True

      if all(zeichen in konsonanten for zeichen in drei_zeichen):
          return True
  return False

def get_random_race(gender = None, generelles_volk = None):
    if generelles_volk is None:
        volk = get_random_index(lists.volk_chance)
    else:
        volk = generelles_volk

    namenskultur = volk
    if volk == "elf":
        if gender == "weiblich":
            volk = volk+"e"
        präfix = random.choice(lists.elf_präfix)
    elif volk == "halbling":
        präfix = random.choice(lists.halbling_präfix)
    elif volk == "mensch":
        präfix = random.choice(lists.mensch_präfix)
        namenskultur = präfix
        if gender == "weiblich":
            präfix = präfix[:-1]+"in "
    elif volk == "zwerg":
        if gender == "weiblich":
            volk = volk+"in"
        präfix = random.choice(lists.zwerg_präfix)
    elif volk == "drachenblütiger":
        volk = volk[:-1]
        präfix = random.choice(lists.drachenblütiger_präfix)
    elif volk == "gnom":
        if gender == "weiblich":
            volk = volk+"in"
        präfix = random.choice(lists.gnom_präfix)
    else:
        präfix = ""
    
    if präfix.endswith(" ") or präfix == "":
        volk = volk.capitalize()
    if volk.lower() == "mensch":
        volk = f"(Mensch)"
    präfix = präfix.capitalize()


    return präfix+volk, namenskultur

def gend(input_pronomen, output_pronomen = "they"):
    if output_pronomen not in dicts.pron.keys():
        return None
    else:
        generisches_geschlecht = [
        ["nom", "er"], 
        ["gen", "sein"], 
        ["dat", "ihm"], 
        ["akk", "ihn"]]
        kasus = None
        for x in range(4):
            if generisches_geschlecht[x][1] == input_pronomen:
                kasus = generisches_geschlecht[x][0]
                break
        if kasus is None:
            return None
        return dicts.pron[output_pronomen][kasus]
    
def pos_pron(person, objekt, kasus = "akk"):
    gend_index = {"er" : 0, "sie" : 1, "es" : 2, "they" : 2, "xer" : 2, "xie" : 2}
    if person in ["they", "xer", "xie"]:
        person = "es"
    return dicts.pos_pron[person][kasus][gend_index[objekt]]
    
def get_random_pronomen(gender):
    if gender == "männlich": return "er"
    elif gender == "weiblich": return "sie"
    elif gender == "divers":
        return get_random_index(lists.pronomen)
    
def suffix(input_str, pronomen, suffix = "in"):
    pronomen_w = ["sie", "xie"]
    if suffix == "in":
        if pronomen in pronomen_w:
            return f"{input_str}in"
        else:
            return input_str
    if suffix == "er":
        if pronomen in pronomen_w:
            return input_str[-1]
        else:
            return input_str
        
def kampf_beginnt(charaktere : list):
    zugreihenfolge = []
    for charakter in charaktere:
        if charakter.is_player is False:
            initiative = würfeln("1D20") + charakter.geschicklichkeit_mod
            zugreihenfolge.append([initiative, charakter])
        elif charakter.is_player is True:
            initiative = get_user_input("int", f"{charakter.eigenname} - bitte würfel auf Initiative")
            zugreihenfolge.append([initiative, charakter])
        else:
            print(f"Fehler: Charakter {charakter.eigenname} ist weder Spieler noch NPC")
    zugreihenfolge.sort(reverse=True, key=lambda x: x[0])
    return zugreihenfolge

def effekte_anwenden (char, effekte):
    if "betäubt" in effekte:
        # Rettungswürfe auf Geschicklichkeit und Stärke scheitern automatisch
        # Vorteil bei angriffen gegen dieses Ziel
        if "kampfunfähig" not in effekte:
            effekte.append("kampfunfähig")

    if "bewusstlos" in effekte:
        # Rettungswürfe auf Geschicklichkeit und Stärke scheitern automatisch
        # Vorteil bei angriffen gegen dieses Ziel
        # Nahkampfangriffe sind automatisch kritisch
        if "kampfunfähig" not in effekte:
            effekte.append("kampfunfähig")

    for effekt in effekte:
        if effekt.startswith("bezaubert"):
            try:
                zauberwirker = effekt.split(">")[-1]
            except TypeError:
                print(f"Es ist ein Fehler bei der verarbeitung des Effekts '{effekt}' aufgetreten.")
        # Ziel kann den Zauberwirker nicht angreifen
        # Zauberwirker hat vorteil bei sozialer Interaktion mit dem Ziel
        pass
    if "blind" in effekte:
        # scheitert bei jedem Attributswurf der Sicht erfordert
        # Nachteil auf Angriffe
        # Vorteil bei angriffen gegen dieses Ziel
        pass
    for effekt in effekte:
        if effekt.startswith("erschöpft"):
            try:
                level = int(effekt.split()[-1])
            except TypeError:
                print(f"Es ist ein Fehler bei der verarbeitung des Effekts '{effekt}' aufgetreten.")
            if level >= 1:
                # nachteil auf attributswürfe
                pass
            if effekt >=2:
                # halbe bewegungsrate
                pass
            if effekt >=3:
                # nachteil bei angriffs und rettungswürfen
                pass
            if effekt >=4:
                # trefferpunktmaximum halbiert
                pass
            if effekt >=5:
                # bewegungsrate auf 0
                pass
            if effekt >= 6:
                # tod
                pass

    if "festgesetzt" in effekte:
        # bewegungsrate auf 0
        # keine Boni auf Bewegungsrate
        # Nachteil auf Angriffe
        # Vorteil bei angriffen gegen dieses Ziel
        # Nachteil bei Rettungswürfen auf Geschicklichkeit
        pass
    if "gelähmt" in effekte:
        if "kampfunfähig" not in effekte:
            effekte.append("kampfunfähig")
        # Vorteil bei angriffen gegen dieses Ziel
        # Nahkampfangriffe sind automatisch kritisch

        pass
    if "gepackt" in effekte:
        # bewegungsrate auf 0
        # keine Boni auf Bewegungsrate
        # endet wenn kampfunfähig
        pass
    if "kampfunfähig" in effekte:
        # keine Aktion, oder Reaktion
        pass
    if "liegend" in effekte:
        # 1/4 bewegungsrate
        # 1 Aktion zum aufstehen
        # Nachteil bei angriffen
        # Vorteil bei Nahkampfangriffen, Nachteil bei Fernkampfangriffen
        pass
    if "taub" in effekte:
        # kann nicht hören und scheitert bei aktionen die hören erfordern
        pass
    if "unsichtbar" in effekte:
        # Vorteil auf Angriffe
        # Nachteil bei Angriffen gegen dieses Ziel
        pass
    if "verängstigt" in effekte:
        # Wenn der Wirker in Sichtweite ist, hat dieses Ziel Nachteil auf angriffe und Attributswürfe
        # Ziel kann sich nicht entscheiden sich auf das Ziel zuzubewegen
        pass
    if "vergiftet" in effekte:
        # Nachteil auf angriffswürfe und Attributswürfe
        pass
    if "versteinert" in effekte:
        # wird zu Stein und altert nicht
        if "kampfunfähig" not in effekte:
            effekte.append("kampfunfähig")
        # Vorteile bei Angriffen gegen dieses Ziel
        # Rettungswürfe auf Geschicklichkeit und Stärke scheitern automatisch
        # Resistenz gegen alle Schadensarten
        # Immun gegen vergiftet und krankheit (vergiftung und Krankheit werden pausiert bis nicht mehr versteinert)
        pass

def get_meta_effekt(meta_effekte):
    if "rettungswurf scheitert automatisch" in meta_effekte:
        pass
    if "vorteil gegen mich" in meta_effekte:
        pass
    if "nahkampf automatisch kritisch gegen mich" in meta_effekte:
        pass
    if "nachteil gegen andere" in meta_effekte:
        pass
    if "nachteil auf attributwürfe" in meta_effekte:
        pass
    if "nachteil auf angriffe" in meta_effekte:
        pass
    if "nachteil auf rettungswürfe" in meta_effekte:
        pass


def looping_index(index, increment, list_len):
    new_index = (index + increment) % list_len
    print(new_index)

