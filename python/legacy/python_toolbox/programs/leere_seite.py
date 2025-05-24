import os
from PyPDF2 import PdfReader, PdfWriter
import shutil
from .utils import printlb, count_pdfs

def leere_seite(pfad, seitenzahl, output_ordner):
    
    if not os.path.exists(output_ordner):
        os.makedirs(output_ordner)  # Ausgabeordner erstellen, falls er nicht existiert

    if os.path.isfile(pfad):
        dateien = [pfad]
    elif os.path.isdir(pfad):
        dateien = [os.path.join(pfad, f) for f in os.listdir(pfad) if f.endswith('.pdf')]
    else:
        raise ValueError("Ungültiger Pfad. Bitte geben Sie den Pfad zu einer PDF-Datei oder einem Ordner an.")

    counter = 0
    for datei in dateien:
        datei_name = os.path.basename(datei)
        counter += 1

        # Kopie im Ausgabeordner erstellen
        output_datei_pfad = os.path.join(output_ordner, datei_name)
        shutil.copy2(datei, output_datei_pfad)  # Kopieren mit Metadaten

        reader = PdfReader(output_datei_pfad) 
        writer = PdfWriter()

        for seite_num in range(len(reader.pages)):
            seite = reader.pages[seite_num]
            writer.add_page(seite)
            if seite_num == seitenzahl - 1: 
                writer.add_blank_page()

        with open(output_datei_pfad, 'wb') as f:
            writer.write(f)

        print(f"[{counter}] '{datei_name}' wurde bearbeitet")
    print("Alle Dateien wurden bearbeitet!")


def run_this_program(express_input = None, express_output = None):
    while True:  # Endlosschleife, bis ein gültiger Wert erhalten wird
            input_dir = input("\nGib den Ordner an, in dem sich die PDFs befinden.\n> ")
            pdfs_in_input_dir = count_pdfs(input_dir) 

            if pdfs_in_input_dir is not None:
                print(f"Der angegebene Ordner enthält {pdfs_in_input_dir} PDF-Dateinen.")
                break  # Schleife beenden, wenn ein gültiger Wert vorliegt

    page_numb = input(f"\nGib die Seitenzahl an, hinter der bei den {pdfs_in_input_dir} PDFs eine leere Seite eingefügt werden soll.\n> ")

    output_dir = input(f"\nGib den Ordner an, in den die bearbeiteten PDFs abgelegt werden sollen.\n> ")

    printlb(f"In den {pdfs_in_input_dir} PDFs in dem Ordner {input_dir} wird jeweils eine leere Seite hinter der {page_numb}. Seite eingefügt und im Ordner {output_dir} abgespeichert.")

    input("Drücke Enter um fortzufahren...")

    leere_seite(input_dir, int(page_numb), output_dir)

help_text = ["Das Programm fügt eine Leerseite hinter eine vorher definierte Seite, in allen PDF Dateien eines bestimmten Ordners ein.",
             "Dafür braucht es 3 Informationen:",
             "(1) Den Speicherort an dem sich die zu bearbeitenden PDFs befinden",
             "(2) Die Seitenzahl HINTER der eine Leerseite eingefügt werden soll",
             "(3) Den Speicherort in dem die bearbeiteten Dateien abgelegt werden sollen"]