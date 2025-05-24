print("Bitte warten, die Packages werden geladen...\n")
print("                   ___________  ______________________________")
print("                .'           .'                              .'")
print("             .'           .'                              .'  |")
print("          .'___________.'______________________________.'     |")
print("          |.----------.|.-----___-----.|.-----___-----.|      |")
print("          |]          |||_____________|||_____________||      |")
print("          ||   ___    ||.-----___-----.|.-----___-----.|      |")
print("          ||   |P|    |||_____________|||_____________||      |")
print("          ||   |Y|    ||.-----___-----.|.-----___-----.|      |")
print("          |]   |T|   o|||_____________|||_____________||      |")
print("          ||   |H|    ||.-----___-----.|.-----___-----.|      |")
print("          ||   |O|    |||             |||_____________||      |")
print("          ||   |N|    |||             ||.-----___-----.|     .'")
print("          |]   |_|    |||             |||             ||  .' o)")
print("          ||__________|||_____________|||_____________||'")
print("          ''----------'''-----------------------------''")
print("                      (o)                           (o)\n")

try:
    import os
    import sys
    from datetime import datetime
except ImportError as e:
    print(f"---\nKritischer Fehler beim Importieren eines Programms\n{e}\n---")
    input("Die python_toolbox kann so nicht ausgeführt werden\nDrücken sie Enter, um das Programm zu schließen...")
    sys.exit(1)

try:
    from programs import utils
    print("'utils' erfolgreich geladen...")

    from programs import leere_seite
    print("'leere_seite' erfolgreich geladen...")

    from programs import sortieren_nach_dateiname
    print("'sortieren_nach_dateiname' erfolgreich geladen...")

    from programs import fensteradressev2
    print("'fensteradressev2' erfolgreich geladen...")

    from programs import f_numb_checker
    print("'f_numb_checker' erfolgreich geladen...")

    from programs import absatz_korrigieren
    print("'absatz_korrigieren' erfolgreich geladen...")

except ImportError as e:
    print(f"---\nFehler beim Importieren eines Programms\n{e}\n---")
    input()

dict_programme = {
    "absatz_korrigieren" :       lambda: absatz_korrigieren.run_this_program(),
    "f_numb_checker" :           lambda: f_numb_checker.run_this_program(),
    "fensteradresse" :           lambda: fensteradressev2.run_this_program(),
    "leere_seite" :              lambda: leere_seite.run_this_program(),
    "sortieren_nach_dateiname" : lambda: sortieren_nach_dateiname.run_this_program()
}

dict_befehl = {
    ("start", "starte", "s") : "start",
    ("help", "hilfe", "h") :   "help",
    ("update", "aktualisieren", "u", "a"): "update",

}

dict_programme["neues_programm"] = 100
# Initialisiert

def is_expired(date1_str, date2_str, date_format="%Y-%m-%d"):
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return date1 < date2
    except ValueError:
        print("Fehler: Ungültiges Datumsformat. Bitte stellen Sie sicher, dass die Datumsangaben dem Format entsprechen.")
        return None

def display_contact():
    print("\nTim Wiesehahn")
    print("---------------------------------")
    print("E-Mail: tim.wiesehahn@uk-essen.de")
    print("Tel.:   0201 723 77237")
    print("Mobil:  0176 21581129")

def display_update():
    print("Öffne den folgenden Link in deinem Browser, um die aktuellste Version der Python_Toolbox zu downloaden")
    print("https://drive.google.com/drive/folders/1Gtx-dQJJ4lwIuVgzwS8k_OoahxmbEkNa?usp=sharing")


# Main Code

clear        = lambda: os.system('cls')
clear()

this_dir     = os.path.dirname(os.path.abspath(__file__)) 
today_date   = datetime.now().strftime('%Y-%m-%d') 
version_date = "2024-10-17" 
exp_date     = "2026-09-01" 
name_this    = os.path.basename(__file__)[:-3]

os.system(f"title {name_this}") # Setzt den Titel des Konsolenfensters

# Überprüft, ob das Programm abgelaufen ist
if is_expired(exp_date, today_date):
    print("\nDieses Programm ist leider abgelaufen. Kontaktiere bitte den Entwickler.\n")
    display_contact()
    input("\nDrücke Enter um das Programm zu schließen...")
    sys.exit(2)

# Begrüßungsnachricht und Kontaktinformationen
print(f"\n{'-' * utils.printlb()}")
print("                       Ts Python Toolbox©")
print(f"{'-' * utils.printlb()}")
print(f" V-{version_date}\n\n")
utils.printlb("Wilkommen zu meinem PDF-Editor, den ich im Aufrag des IMIBE erstellt habe. Dieser PDF-Editor ist ein Werkzeugkasten, mit dem man auf verschiedene Art und Weise PDF-Dateien bearbeiten kann. Bei Fragen und Problemen könnt ihr euch gerne an mich wenden:")
display_contact()
input("\nDrücke Enter um fortzufahren...")
clear()

user_input = utils.get_user_input("str", "").lower()