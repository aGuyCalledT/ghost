import os
import shutil
import openpyxl

def count_pdfs(folder_path):
    if not os.path.exists(folder_path):
        print(f"Der Ordnerpfad '{folder_path}' existiert nicht.")
        return None
    
    pdf_count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_count += 1
    
    return pdf_count


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


def xlsx_to_array(filename):
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active

    data = []
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        string_list = [str(element) for element in list(row)]
        data.append(string_list)

    return data