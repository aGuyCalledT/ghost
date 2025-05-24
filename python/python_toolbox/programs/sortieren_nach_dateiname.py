import programs.utils
import shutil
import openpyxl
import os

def xlsx_zu_array(dateipfad):
    workbook = openpyxl.load_workbook(dateipfad)
    worksheet = workbook.active  # Nimmt das erste Arbeitsblatt

    array = []
    for row in worksheet.iter_rows(min_row=1, max_col=1, values_only=True):
        array.append(f"F{row[0]}.pdf")  # Fügt den Wert der ersten Spalte hinzu

    return array


def pdfs_zu_array(verzeichnispfad):
    pdf_dateien = []
    for dateiname in os.listdir(verzeichnispfad):
        if dateiname.endswith(".pdf"):
            pdf_dateien.append(dateiname)

    return pdf_dateien


def finde_gemeinsame_elemente(array1, array2):
    gemeinsame_elemente = []
    for element in array1:
        if element in array2:
            gemeinsame_elemente.append(element)
    return gemeinsame_elemente


def verschiebe_dateien(quelldateien, quellverzeichnis, zielverzeichnis):
    for dateiname in quelldateien:
        quellpfad = os.path.join(quellverzeichnis, dateiname)
        zielpfad = os.path.join(zielverzeichnis, dateiname)

        # Überprüfen, ob die Datei existiert
        if os.path.exists(quellpfad):
            shutil.move(quellpfad, zielpfad)
            print(f"Datei '{dateiname}' wurde verschoben.")
        else:
            print(f"Datei '{dateiname}' nicht gefunden.")


def run_this_program():
    input_dir = programs.utils.get_user_input("path", "Gib das Verzeichnis an, aus dem die PDFs verschoben werden sollen")
    xlsx_table = programs.utils.get_user_input("path", "Gib den Pfad der XLSX-Datei an, welche die Dateinamen enthält, die verschoben werden sollen")
    output_dir = programs.utils.get_user_input("path", "Gib das Verzeichnis an, in das die PDFs verschoben werden sollen")

    komm_id_array = xlsx_zu_array(xlsx_table)
    pdf_array = pdfs_zu_array(input_dir)
    transfer_array = finde_gemeinsame_elemente(komm_id_array, pdf_array)
    print(f"Insgesamt gibt es {len(transfer_array)} FBs")
    verschiebe_dateien(transfer_array, input_dir, output_dir)

help_text = ["Das Programm verschiebt alle PDF-Dateien, deren Name in einer XLSX-Tabelle vorkommen,", 
             "in einen anderen Ordner. Dafür brauchst es 3 Informationen:", 
             "(1) Den Dateipfad des Ordners in dem sich die PDFs befinden",
             "(2) Eine Excel-Tabelle, welche die zu verschiebenden Dateinamen enthält",
             "(3) Den Dateipfad des Ordners, in dem die PDFs am ende abgelegt werden sollen"]