print("Bitte warten, die Packages werden geladen...\n\n\n")
print("                   ___________  ______________________________")
print("                .'           .'                              .'")
print("             .'           .'                              .'  |")
print("          .'___________.'______________________________.'     |")
print("          |.----------.|.-----___-----.|.-----___-----.|      |")
print("          |]          |||_____________|||_____________||      |")
print("          ||          ||.-----___-----.|.-----___-----.|      |")
print("          ||    P     |||_____________|||_____________||      |")
print("          ||    Y     ||.-----___-----.|.-----___-----.|      |")
print("          |]    T    o|||_____________|||_____________||      |")
print("          ||    H     ||.-----___-----.|.-----___-----.|      |")
print("          ||    O     |||             |||_____________||      |")
print("          ||    N     |||             ||.-----___-----.|     .'")
print("          |]          |||             |||             ||  .' o)")
print("          ||__________|||_____________|||_____________||'")
print("          ''----------'''-----------------------------''")
print("                      (o)                           (o)")

import os
import sys
from datetime import datetime
from programs.utils import printlb
from programs import leere_seite, fensteradresse, sortieren_nach_dateiname, fensteradressev2, f_numb_checker


ui_support = ["fensteradresse", "leere_seite", "sortiere_nach_dateiname", 
              "fensteradressev2", "absatz_korrigieren", 
              "sortieren_nach_dateiname",
              "f_numb_checker"]

help_text_dic = {
    "fensteradresse"           : fensteradresse.help_text,
    "fensteradressev2"         : fensteradressev2.help_text,
    "leere_seite"              : leere_seite.help_text,
    "sortieren_nach_dateiname" : sortieren_nach_dateiname.help_text,
    "f_numb_checker"           : f_numb_checker.help_text,
}

def get_help_text(program):
    if program in help_text_dic:
        for line in help_text_dic[program]:
            print(line)
    else:
        print("Für dieses Programm gibt es noch keinen Hilfstext.")


# Funktion zum Überprüfen, ob ein Datum abgelaufen ist
def is_expired(date1_str, date2_str, date_format="%Y-%m-%d"):
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return date1 < date2
    except ValueError:
        print("Fehler: Ungültiges Datumsformat. Bitte stellen Sie sicher, dass die Datumsangaben dem Format entsprechen.")
        return None


# Funktion zum Abrufen einer Liste von Programmen aus einem Verzeichnis
def get_list_of_programs(directory="programs"):
    list_of_programs = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".py") and filename not in ["__init__.py", "utils.py"]:  # Ignoriere __init__.py
                list_of_programs.append(filename[:-3])
        list_of_programs.sort()

    except FileNotFoundError:
        print(f"Fehler: Das Verzeichnis '{directory}' wurde nicht gefunden.")
        print(f"Bitte stelle sicher, dass dieses Programm sich im selben Verzeichnis,\n wie der Ordner 'programs' befindet.")

    list_of_programs = ([string.lower() for string in list_of_programs])
    
    
    return list_of_programs


# Funktion zum Abrufen von Benutzereingaben
def get_user_input_menu(list_of_programs):
    while True:
        user_input = input("\n> ").lower()

        # Überprüfung auf 'beenden' oder 'exit'
        if user_input in ["beenden", "exit", "end", "e"]:
            return "beenden"
        
        # Überprüfung auf 'update' oder 'aktualisieren'
        if user_input in ["update", "aktualisieren", "u"]:
            return "update"

        # Überprüfung auf 'starte' oder 'start'
        if user_input in ["starte", "start", "s"]:
            program_name = input(f"Welches Programm möchten Sie starten?\n> starte ").lower()
            if program_name in list_of_programs:
                return f"starte {program_name}"
            else:
                print("Ungültiger Programmname. Bitte versuchen Sie es erneut.")

        # Überprüfung auf 'starte programm1' Format
        elif user_input.startswith("starte ") or user_input.startswith("start "):
            program_name = user_input.split(" ")[1] 
            if program_name in list_of_programs:
                return f"starte {program_name}"
            else:
                print("Ungültiger Programmname. Bitte versuchen Sie es erneut.")

        # Überprüfung auf 'hilfe' oder 'help'
        elif user_input in ["hilfe", "help", "h"]:
            help_input = input("Für welches Programm benötigen Sie Hilfe?\nGib 'alle' für allgemeine Hilfe\n> hilfe ").lower()
            if help_input in list_of_programs or help_input == "alle":
                return f"hilfe {help_input}"
            else:
                print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

        # Überprüfung auf 'hilfe programm1' Format
        elif user_input.startswith("help ") or user_input.startswith("hilfe "):
            program_name = user_input.split(" ")[1] 
            if program_name in list_of_programs:
                print(f"DIE FUNKTION SAGT: hilfe {program_name}")
                return f"hilfe {program_name}"
            else:
                print("Ungültiger Programmname. Bitte versuchen Sie es erneut.")

        # Überprüfung auf andere gültige Eingaben
        elif user_input in ["hilfe", "help"]:
            return user_input

        # Fehlerfall
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")


# Funktion zum Anzeigen der Liste der Programme
def display_list_of_programs(list_of_programs):
    program_numb = 1
    print("\nProgramme")
    print(f"{'-' * printlb()}")
    for program in list_of_programs:
        print(f"[{program_numb:02d}] {program}")
        program_numb += 1
    print(f"{'-' * printlb()}\n")

def display_header(program):
    if program in ui_support or program == name_this:
        print(f"\n\n-------------- {program} --------------\n")
    else:
        print()
        print(f"\n\n-------------- ({program}) --------------\n")


# Funktion zum Anzeigen von Kontaktinformationen
def display_contact():
    print("\nTim Wiesehahn")
    print("---------------------------------")
    print("E-Mail: tim.wiesehahn@uk-essen.de")
    print("Tel.:   0201 723 77237")
    print("Mobil:  0176 21581129")





# MAIN CODE
clear        = lambda: os.system('cls')
clear()

this_dir     = os.path.dirname(os.path.abspath(__file__)) 
today_date   = datetime.now().strftime('%Y-%m-%d') 
version_date = "2024-09-09" 
exp_date     = "2026-09-01" 
name_this    = os.path.basename(__file__)[:-3]

ui_support.append(name_this)

os.system(f"title {name_this}") # Setzt den Titel des Konsolenfensters

# Überprüft, ob das Programm abgelaufen ist
if is_expired(exp_date, today_date):
    print("\nDieses Programm ist leider abgelaufen. Kontaktiere bitte den Entwickler.\n")
    display_contact()
    input("\nDrücke Enter um das Programm zu schließen...")
    sys.exit(0)

# Begrüßungsnachricht und Kontaktinformationen
print(f"\n{'-' * printlb()}")
print("                       Ts Python Toolbox©")
print(f"{'-' * printlb()}")
print(f" V-{version_date}\n\n")
printlb("Wilkommen zu meinem PDF-Editor, den ich im Aufrag des IMIBE erstellt habe. Dieser PDF-Editor ist ein Werkzeugkasten, mit dem man auf verschiedene Art und Weise PDF-Dateien bearbeiten kann. Bei Fragen und Problemen könnt ihr euch gerne an mich wenden:")
display_contact()
input("\nDrücke Enter um fortzufahren...")
clear()

# Liste der verfügbaren Programme abrufen
list_of_programs = get_list_of_programs(directory=f"{this_dir}\\programs")

# Überprüfung, ob Programme gefunden wurden
if list_of_programs == []:
    input("\nDrücke Enter um das Programm zu schließen...")
    sys.exit(0)
else:
    display_list_of_programs(list_of_programs)

print("Wenn du nicht weist, was du machen sollst, gib 'hilfe' ein, oder gibt 'starte' gefolgt von einem Programmnamen ein.\n")

# Hauptschleife, die das Programm am Laufen hält
while True: 
    user_input = get_user_input_menu(list_of_programs)

    if user_input == "beenden":  # Neue Bedingung zum Beenden des Programms
        break  # Schleife beenden, wenn der Benutzer "beenden" eingibt

    elif user_input == "update":
        print("Öffne den folgenden Link in deinem Browser, um die aktuellste Version der Python_Toolbox zu downloaden")
        print("https://drive.google.com/drive/folders/1Gtx-dQJJ4lwIuVgzwS8k_OoahxmbEkNa?usp=sharing")

    elif user_input.startswith("hilfe "):
        print("du bist in der hilfe schleife")
        program = user_input.split(" ")[1]
        print(f"program = {program}")
        if program == "alle":
            print("HABALLA!")
        else:
            get_help_text(program)


# Hier sind die Programme mit Interface -------------------------------------------------------
    elif user_input.startswith("starte "):
        program = user_input.split(" ")[1]
        if program not in ui_support:
            display_header(program)
            os.chdir(f"{this_dir}\\programs")
            os.system(f"title {program}")
            os.system(f"python {program}.py")

            display_header(name_this)
            os.system(f"title {name_this}")
        else:
            if user_input == "starte leere_seite":
                display_header(program)
                leere_seite.run_this_program()
                display_header(name_this)
        
            elif user_input == "starte fensteradresse":
                display_header(program)
                fensteradresse.run_this_program()
                display_header(name_this)
            
            elif user_input == "starte fensteradressev2":
                display_header(program)
                fensteradressev2.run_this_program()
                display_header(name_this)
            
            elif user_input == "starte absatz_korrigieren":
                display_header(program)
                absatz_korrigieren.run_this_program()
                display_header(name_this)

            elif user_input == "starte sortieren_nach_dateiname":
                display_header(program)
                sortieren_nach_dateiname.run_this_program()
                display_header(name_this)
            
            elif user_input == "starte f_numb_checker":
                display_header(program)
                f_numb_checker.run_this_program()
                display_header(name_this)

            else:
                print(f"ERROR: Die Eingabe '{user_input}' konnte nicht richtig verarbeitet werden.")
                print(f"'{program}' ist in der UI-Support liste, hat aber keinen UI-Support.")

    else:
        print(f"ERROR: Die Eingabe '{user_input}' konnte nicht richtig verarbeitet werden.")

