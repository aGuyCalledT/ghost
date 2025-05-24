import shutil
import os
import openpyxl

# Funktion zum zeilenweisen Ausgeben von Text
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


def count_pdfs(folder_path):
    if not os.path.exists(folder_path):
        print(f"Der Ordnerpfad '{folder_path}' existiert nicht.")
        return None
    
    pdf_count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_count += 1
    
    return pdf_count


def check_int_within_bounds(value, min_int=None, max_int=None):
  if min_int is not None and value < min_int:
    return False

  if max_int is not None and value > max_int:
    return False

  return True


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
        

def copy_file_to_dir(file, output_dir):
    # Checks whether file and dir exist and creates dir if necessary
    if not os.path.exists(file):
        print(f"Fehler: Die Datei '{file}' existiert nicht.")
        return False
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        shutil.copy2(file, output_dir)

    except Exception as e:
        print(f"Fehler beim Kopieren der Datei: {e}")
        return False

    return True


def pdf_liste_erstellen(ordnerpfad):
  pdf_dateien = []

  for dateiname in os.listdir(ordnerpfad):
    if dateiname.endswith(".pdf"):
      vollständiger_pfad = os.path.join(ordnerpfad, dateiname)
      pdf_dateien.append(vollständiger_pfad)

  return pdf_dateien


def create_dir(ordnerpfad):
  if not os.path.exists(ordnerpfad):
    os.makedirs(ordnerpfad)
  else:
    pass


def xlsx_to_array(filename):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active

    data = []
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        string_list = [str(element) for element in list(row)]
        data.append(string_list)

    return data


def remove_prefix_suffix(input_array, prefix, suffix, index=None):
  result = []
  for element in input_array:
    if isinstance(element, list):  # Überprüfen, ob es sich um ein Array handelt
      if index is not None and 0 <= index < len(element):
        new_item = element.copy()  # Kopieren, um das Original nicht zu verändern
        if new_item[index].startswith(prefix):
          new_item[index] = new_item[index][len(prefix):]
        if new_item[index].endswith(suffix):
          new_item[index] = new_item[index][:-len(suffix)]
        result.append(new_item)
      else: 
        # Wenn kein Index angegeben ist oder der Index ungültig ist, wird das gesamte Array unverändert zurückgegeben
        result.append(element) 
    else: 
      # Wenn es sich um einen String handelt, wird er wie zuvor bearbeitet
      if element.startswith(prefix):
        element = element[len(prefix):]
      if element.endswith(suffix):
        element = element[:-len(suffix)]
      result.append(element)

  return result


def add_prefix_suffix(input_array, prefix, suffix, index=None):
    result = []
    for element in input_array:
        if isinstance(element, list):  # Überprüfen, ob es sich um ein Array handelt
            if index is not None and 0 <= index < len(element):
                new_item = element.copy()  # Kopieren, um das Original nicht zu verändern
                new_item[index] = prefix + new_item[index] + suffix 
                result.append(new_item)
            else:
                # Wenn kein Index angegeben ist oder der Index ungültig ist, wird das gesamte Array unverändert zurückgegeben
                result.append(element)
        else:
            # Wenn es sich um einen String handelt, wird er wie zuvor bearbeitet
            result.append(prefix + element + suffix)

    return result