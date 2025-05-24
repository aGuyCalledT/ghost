from .utils import xlsx_to_array, get_user_input

help_text = ["Joa, der prüft Adressen anhand der Komm_ID"]

def run_this_program():
    path = get_user_input("path", "Gib den Dateipfad der Adressliste an")
    print(f"Die Adressliste wird eingelesen...")
    addressdaten = xlsx_to_array(path)

    while True:
        input = get_user_input("string", "Gib die Komm_ID einer*eines Proband*in ein")
        found = False
        for line in addressdaten:
            if line[0] == input:
                for element in line:
                    if element == input:
                        print(f"---------F{input}---------\n")
                    print(f"- {element}")
                found = True
                break
        if found is False:
            print("Sorry there was a problem")
        print("\n")