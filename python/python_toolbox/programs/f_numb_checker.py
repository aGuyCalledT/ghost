import openpyxl, os

help_text = ["Joa, der prüft Adressen anhand der Komm_ID"]

def check_int_within_bounds(value, min_int=None, max_int=None):
  if min_int is not None and value < min_int:
    return False

  if max_int is not None and value > max_int:
    return False

  return True

def xlsx_to_array(filename):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active

    data = []
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        string_list = [str(element) for element in list(row)]
        data.append(string_list)

    return data

def get_user_input(input_type, input_message=None, valid_strings=None, min_int=None, max_int=None):
    while True:
        if input_message is None:
            user_input = input(f"\n> ")
        else:
            user_input = input(f"\n{input_message}\n> ")

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
            raise ValueError(f"Ungültige Eingabe. Die Eingabe muss {input_type} sein")

def run_this_program():
    path = get_user_input("path", "Gib den Dateipfad der Adressliste an")
    print(f"Die Adressliste wird eingelesen...")
    addressdaten = xlsx_to_array(path)

    all_possible_ids = []
    for line in addressdaten:
        all_possible_ids.append(int(line[0]))
    
    while True:
        input_id = get_user_input("int", "Gib die Komm_ID einer*eines Proband*in ein")

        if input_id not in all_possible_ids: print("ERROR: ID doesn't exist!")
        else:
            adress_line = all_possible_ids.index(input_id)
            adress_data = addressdaten[adress_line]
 

            pb_id = f"Komm_ID: F{adress_data[0]}"
            pb_name = f"{adress_data[3]} {adress_data[2]}"
            pb_street = f"{adress_data[4]} {adress_data[5]}"
            pb_plz = f"{adress_data[6]} {adress_data[7]}"

            print("---------------------------")
            print(pb_id)
            print(pb_name)
            print(pb_street)
            print(pb_plz)
            print("---------------------------")