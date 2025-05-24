from lib.gen_utils import get_user_input

def ist_primzahl(zahl):
    if zahl <= 1:
        return False  # 1 und negative Zahlen sind keine Primzahlen

    if zahl <= 3:
        return True #2 und 3 sind Primzahlen
        
    if zahl % 2 == 0 or zahl % 3 ==0: # Alle Zahlen die durch 2 oder 3 teilbar sind sind keine Primzahlen.
        return False

    i = 5 # Starte mit 5, die nächsten Primzahl nach 3.
    while i * i <= zahl: # Überprüfe nur bis zur Quadratwurzel der Zahl
        if zahl % i == 0 or zahl % (i + 2) == 0:
            return False
        i += 6 #Optimierung: überprüfe nur Zahlen der Form 6k +-1

    return True # Wenn keine Teiler gefunden wurden, ist die Zahl eine Primzahl



while True:
    start_numb = get_user_input("int", "Gib die Anfangszahl ein")
    end_numb = get_user_input("int", "Gib die Endzahl ein")

    primzahlen_tabelle = []
    temp_line = ""

    for x in range(start_numb, end_numb + 1):
        if ist_primzahl(x):
            primzahlen_tabelle.append(x)
            if len(temp_line) < 80:
                temp_line += f"{x}, "
            else:
                print(temp_line)
                temp_line = ""

            
    print(temp_line)

    print(f"{len(primzahlen_tabelle)} Primzahlen wurden zwischen {start_numb} und {end_numb} gefunden!")