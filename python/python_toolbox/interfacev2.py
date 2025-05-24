def setup(packages : list):
    print("Bitte warten - die python_toolbox wird geladen")
    for line in interface.wrench:
        print(line)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    programs_dir = os.path.join(script_dir, "programs")

    loaded_packages = []
    loaded_report = []

    for package in packages:
        loaded = interface.import_package(programs_dir, package)
        if loaded.startswith("Modul"): loaded_packages.append(package)
        loaded_report.append(loaded)

    for line in loaded_report:
        print(line)
    if loaded_packages != packages:
        input("Drücke Enter um fortzufahren...")
    interface.clear_console()


def display_greeting():
    print("Wilkommen zu meinem PDF-Editor, den ich im Aufrag des IMIBE erstellt habe. Dieser PDF-Editor ist ein Werkzeugkasten, mit dem man auf verschiedene Art und Weise PDF-Dateien bearbeiten kann. Bei Fragen und Problemen könnt ihr euch gerne an mich wenden:\n")


def display_contact():
    print("┌─────────────────────────────────────────────────────────┐")
    print("│    T Wiesehahn                                          │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│    E-Mail: tim.wiesehahn@uk-essen.de                    │")
    print("│    Tel.:   0201 723 77237                               │")
    print("│    Mobil:  0176 21581129                                │")
    print("└─────────────────────────────────────────────────────────┘\n")


def display_update():
    print("Öffne den folgenden Link in deinem Browser, um die aktuellste Version der Python_Toolbox zu downloaden")
    print("https://drive.google.com/drive/folders/1Gtx-dQJJ4lwIuVgzwS8k_OoahxmbEkNa?usp=sharing")


def display_title():
    title = [
        "┌─────────────────────────────────────────────────────────┐",
        "│                  Ts Python Toolbox© 2.0                 │",
        "└─────────────────────────────────────────────────────────┘",
        f"v-{version_date}\n\n"
    ]
    for line in title:
        print(line)

def display_program_list(packages):
    print(" Programme")
    print("┌─────────────────────────────────────────────────────────┐")
    for x in range(len(packages)):
        if packages[x] == "utils": pass
        else:
            print(f"│ [{x:02d}] - {packages[x]}{" "*(48 - len(packages[x]))} │")
    print("└─────────────────────────────────────────────────────────┘")

def standardize_user_input(user_input, keywords= ["start", "help"]):
    split_input = user_input.split()
    best_matches = [] # ['start', 100]
   
    for word in split_input:
        current_match = []
        for keyword in keywords:
            current_match.append([keyword, fuzz.ratio(word, keyword)])
        best_match = max(current_match, key=lambda element: element[1])
        best_matches.append(best_match)

    return [sublist[0] for sublist in best_matches if len(sublist) > 1]


# ---------------  Main Code  ---------------
import os, sys, platform
import interface_support as interface
from programs import utils
from datetime import datetime
from fuzzywuzzy import fuzz
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

version_date = "2025-03-27"
exp_date     = "2030-01-01"
current_date = datetime.now().strftime('%Y-%m-%d')

if interface.is_expired(exp_date, current_date):
    pass

packages= [
        "utils",
        "leere_seite",
        'sortieren_nach_dateiname',
        'fensteradressev2',
        'f_numb_checker',
    ]
setup(packages)
display_title()
display_greeting()
display_contact()
display_program_list(packages)


keywords = ["start", "help", "starte", "hilfe", "clear", "leeren"] + packages
completer = WordCompleter(keywords)

while True:
    user_input = prompt("\nGib 'start <Programm Name>' ein, um ein Programm auszuführen. Wenn du Hilfe brauchst, gib 'hilfe', oder 'hilfe <Programm Name>' ein.\n>", completer=completer)
    user_input = standardize_user_input(user_input, keywords=keywords)

    if len(user_input) == 1:

        if user_input[0] == "clear":
            interface.clear_console()
            display_title()
            display_greeting()
            display_contact()
            display_program_list(packages)

        if user_input[0] == "start":
            pass
    
        elif user_input[0] == "help":
            pass
    
    if len(user_input) > 2:
        print(f"\nFehler: Deine Eingabe muss aus zwei Komponenten bestehen (du hast {len(user_input)} eingegeben) - einem Befehl wie 'starte', oder 'hilfe' und einem Programmnamen")
        continue
    
    

    




