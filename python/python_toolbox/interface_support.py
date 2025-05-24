import importlib, sys, platform, os, sys
from datetime import datetime


wrench = [
"          ..--",                                    
"          @@######",                                
"            @@######",                              
"              @@######",                            
"              --######..",                          
"mm::          ########MM",                          
"MM##++        ########@@",                          
"  ####++  ############::",                          
"  ######################",                          
"  --######################",                        
"    ::######################",                      
"        mm####mm##############..",                  
"                  ##############",                  
"                    ##############",                
"                      ##############",              
"                        ##############",            
"                          ##############",          
"                            ##############",        
"                              ##############",      
"                                ##############..",  
"                                  ##############..",
"                                    ##############",
"                                      #######  ###",
"                                        #####__###",
"                                          ########"
]


def import_package(ordnerpfad, modulname):
    try:
        sys.path.append(ordnerpfad)
        global module
        module = importlib.import_module(modulname)
        return f"Modul '{modulname}' erfolgreich importiert."

    except ImportError as e:
        return f"Fehler: Modul '{modulname}' konnte nicht importiert werden: \n  {e}"

    finally:
        # Entferne den Ordnerpfad aus sys.path (optional, aber empfohlen)
        if ordnerpfad in sys.path:
            sys.path.remove(ordnerpfad)


def clear_console():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux' or system == 'Darwin':
        os.system('clear')
    else:
        print("Betriebssystem wird nicht unterstützt.")


def exit_console():
    betriebssystem = platform.system()
    if betriebssystem == "Windows":
        try:
            os.system("taskkill /pid %d /f" % os.getpid())
        except Exception as e:
            print(f"Fehler beim Schließen der Konsole unter Windows: {e}")
    elif betriebssystem == "Linux" or betriebssystem == "Darwin":
        try:
            sys.exit()
        except Exception as e:
            print(f"Fehler beim Schließen der Konsole unter Linux/macOS: {e}")
    else:
        print("Betriebssystem wird nicht unterstützt.")


def is_expired(date1_str, date2_str, date_format="%Y-%m-%d"):
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        expired = date1 < date2
    except ValueError:
        print("Fehler: Ungültiges Datumsformat. Bitte stellen Sie sicher, dass die Datumsangaben dem Format entsprechen.")
        return None
    if expired:
        print("\nDieses Programm ist leider abgelaufen. Kontaktiere bitte den Entwickler.\n")
        display_contact()
        input("Drücke Enter um das Programm zu schließen...")
        interface.exit_console()
