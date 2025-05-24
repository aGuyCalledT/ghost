import os
import pandas as pd
import shutil
import PyPDF2


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



def get_pdf_names_without_extension(dateipfad):
    pdf_dateien = []
    for datei in os.listdir(dateipfad):
        if datei.endswith(".pdf"):
            # Entferne die Dateierweiterung und füge den Namen zur Liste hinzu
            pdf_dateien.append(os.path.splitext(datei)[0])
    return pdf_dateien


import pandas as pd

def extrahiere_spalte(dateipfad, spaltennummer, praefix='F'):
    # Excel-Datei einlesen
    df = pd.read_excel(dateipfad)

    # Spalte extrahieren, leere Werte entfernen und Präfix hinzufügen
    spalten_werte = df.iloc[:, spaltennummer].dropna().astype(str).apply(lambda x: praefix + x[:-2]).tolist()

    return spalten_werte


def finde_unterschiede(array1, array2):
  # Umwandlung in Sets für effiziente Mengenoperationen
  set1 = set(array1)
  set2 = set(array2)

  # Differenz der Mengen berechnen (Elemente in set1, aber nicht in set2)
  unterschiede = set1.difference(set2)

  return list(unterschiede)


def verschiebe_pdfs(quelle, ziel, validationsliste):
    num = 0
    log_datei = f"{ziel}/verschobene_dateien.txt"
    with open(log_datei, "w") as log:
        for name in validationsliste:
            num += 1
            quelle_datei = f"{quelle}/{name}.pdf"
            ziel_datei = f"{ziel}/{name}.pdf"
            try:
                shutil.move(quelle_datei, ziel_datei)
                print(f"Datei {num:0{3}} erfolgreich verschoben ({name}.pdf)")
                log.write(f"{name}.pdf\n")
            except FileNotFoundError:
                print(f"Datei NICHT gefunden ({name}.pdf)")
            except shutil.Error as e:
                print(f"Fehler beim Verschieben von {name}.pdf: {e}")


def pdf_seiten_extrahieren(ordnerpfad, seite_nummer, eine_pdf=True):
    if not os.path.exists(ordnerpfad):
        print(f"Fehler: Ordner '{ordnerpfad}' nicht gefunden.")
        return

    pdf_dateien = [f for f in os.listdir(ordnerpfad) if f.endswith('.pdf')]
    if not pdf_dateien:
        print(f"Keine PDF-Dateien im Ordner '{ordnerpfad}' gefunden.")
        return

    if eine_pdf:
        ausgabe_pdf = PyPDF2.PdfWriter()

    for pdf_datei in pdf_dateien:
        pdf_pfad = os.path.join(ordnerpfad, pdf_datei)
        try:
            with open(pdf_pfad, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                if seite_nummer >= len(pdf_reader.pages):
                    print(f"Warnung: Seite {seite_nummer} in '{pdf_datei}' nicht vorhanden. Überspringen.")
                    continue

                seite = pdf_reader.pages[seite_nummer]
                if eine_pdf:
                    ausgabe_pdf.add_page(seite)
                else:
                    ausgabe_pdf_name = f"{os.path.splitext(pdf_datei)[0]}_Seite_{seite_nummer + 1}.pdf"
                    ausgabe_pdf_pfad = os.path.join(ordnerpfad, ausgabe_pdf_name)
                    with open(ausgabe_pdf_pfad, 'wb') as ausgabe_file:
                        pdf_writer = PyPDF2.PdfWriter()
                        pdf_writer.add_page(seite)
                        pdf_writer.write(ausgabe_file)

        except PyPDF2.utils.PdfReadError:
            print(f"Fehler: '{pdf_datei}' ist keine gültige PDF-Datei. Überspringen.")

    if eine_pdf:
        ausgabe_pdf_name = "extrahierte_seiten.pdf"
        ausgabe_pdf_pfad = os.path.join(ordnerpfad, ausgabe_pdf_name)
        with open(ausgabe_pdf_pfad, 'wb') as ausgabe_file:
            ausgabe_pdf.write(ausgabe_file)


def run_this_program():
    while True:  # Endlosschleife, bis ein gültiger Wert erhalten wird
            input_dir = input("\nGib den Ordner an, in dem sich die PDFs befinden.\n> ")
            pdfs_in_input_dir = count_pdfs(input_dir) 

            if pdfs_in_input_dir is not None:
                print(f"Der angegebene Ordner enthält {pdfs_in_input_dir} PDF-Dateinen.")
                break  # Schleife beenden, wenn ein gültiger Wert vorliegt

    table = input(f"\nGib den Dateipfad der XLSX-Tabelle an, in der die Dateinamen enthalten sind, die verschoben werden sollen.\n> ")

    output_dir = input(f"\nGib den Ordner an, in den die PDFs aus der Tabelle abgelegt werden sollen.\n> ")

    printlb(f"Aus dem Ordner mit {pdfs_in_input_dir} PDF-Dateien, werden nun alle Dateien die in der XLSX-Tabelle in {table} enthalten sind, in den Ordner in {output_dir} verschoben.")

    input("Drücke Enter um fortzufahren...")

    


help_text = ["Das Programm verschiebt alle PDF-Dateien, deren Name in einer SLSX-Tabelle vorkommen,", 
             "in einen anderen Ordner. Dafür brauchst es 3 Informationen:", 
             "(1) Den Dateipfad des Ordners in dem sich die PDFs befinden",
             "(2) Eine Excel-Tabelle, welche die zu verschiebenden Dateinamen enthält",
             "(3) Den Dateipfad des Ordners, in dem die PDFs am ende abgelegt werden sollen"]




