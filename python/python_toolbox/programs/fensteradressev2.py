import openpyxl
import os
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from utils import get_user_input, copy_file_to_dir, printlb, xlsx_to_array, remove_prefix_suffix


def add_address_to_pdfs(directory, address_data, return_address_input):
    counter = 0
    pdfs_without_address = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            counter += 1
            print(f"\n[{counter:04d}] '{filename}' wird bearbeitet...")
            pdf_path = os.path.join(directory, filename)

            # Finden der passenden Adressinformationen
            matching_address = None
            
            for address in address_data:
                for table_line in address_data:
                    if matching_address: break
                    if f"F{address[0]}.pdf" == filename:
                        print("       Adresse zu PDF gefunden...")
                        matching_address = address[1:]  # Restliche Elemente sind die Adressinformationen
                        break
                    else:
                        break

            if matching_address is None:
                print("       Adresse zu PDF nicht gefunden...")
                pdfs_without_address.append(filename)


            if matching_address:
                # Erstellen einer neuen PDF mit der Adresse (nur eine Seite)
                breite = 595
                höhe   = 1242
                temp_pdf_path = os.path.join(directory, "temp_address.pdf")
                c = canvas.Canvas(temp_pdf_path, pagesize=(breite, höhe))

                print(f"Gender marker is: {matching_address[0]}")

                if matching_address[0].lower() == "m":
                    print(f"is 'm'")
                    matching_address[0] = "Herr"
                    salut = "Sehr geehrter Herr"
                elif matching_address[0].lower() == "w":
                    print(f"is 'w'")
                    matching_address[0] = "Frau"
                    salut = "Sehr geehrte Frau"
                else:
                    print(f"is not 'm' or 'w'")
                    matching_address[0] = None
                    salut = "Sehr geehrte/r Herr/Frau"

                x_pos               = 48
                y_pos_return_adress = 696
                y_pos_line          = 690
                y_pos_name          = 675  
                y_pos_street        = 660  
                y_pos_postal        = 645  
                y_pos_salutation    = 475 

                return_address = return_address_input
                div_line       = "_________________________________"
                street         = f"{matching_address[3]} {matching_address[4]}"
                postal         = f"{matching_address[5]} {matching_address[6]}"
                salutation     = f"{salut} {matching_address[1]},"

                if matching_address[0] is None:
                    name = f"{matching_address[2]} {matching_address[1]}"
                else:
                    name = f"{matching_address[0]} {matching_address[2]} {matching_address[1]}"

                c.setFont("Helvetica-Oblique", 10)
                c.drawString(x_pos, y_pos_return_adress, return_address)

                c.setFont("Helvetica", 12)
                c.drawString(x_pos, y_pos_line, div_line)
                c.drawString(x_pos, y_pos_name, name)
                c.drawString(x_pos, y_pos_street, street)
                c.drawString(x_pos, y_pos_postal, postal)
                c.drawString(x_pos, y_pos_salutation, salutation)

                c.save() 

                # Zusammenführen der PDFs
                with open(pdf_path, "rb") as original_pdf, \
                        open(temp_pdf_path, "rb") as address_pdf:
                    reader_original = PdfReader(original_pdf)
                    reader_address = PdfReader(address_pdf)

                    writer = PdfWriter()

                    # Erste Seite des Originals holen
                    first_page_original = reader_original.pages[0]

                    # Erste Seite der Adresse mit der ersten Seite des Originals zusammenführen
                    first_page_original.merge_page(reader_address.pages[0])

                    # Zusammengeführte Seite hinzufügen
                    writer.add_page(first_page_original)

                    # Restliche Seiten des Originals hinzufügen (beginnend bei Seite 1)
                    for page_num in range(1, len(reader_original.pages)):
                        writer.add_page(reader_original.pages[page_num])

                    # Neue PDF speichern
                    with open(pdf_path, "wb") as output_pdf:
                        writer.write(output_pdf)

                # Temporäre PDF löschen
                os.remove(temp_pdf_path)

                print(f"       Adresse erfolgreich hinzugefügt  --  {matching_address[1]}, {matching_address[2]}")
    
    return pdfs_without_address

def run_this_program():

    input_dir  = get_user_input("path", "Gib den Pfad des Ordners ein, der die zu bearbeitenden PDFs enthält")
    xlsx_table = get_user_input("path", "Gib den Pfad der XLSX-Tabelle ein, welche die Adressen enthält")
    output_dir = get_user_input("path", "Gib den Pfad des Ordners ein, in dem die bearbeiteten PDFs abgelegt werden sollen")
    
    while True:
        prefix_suffix = get_user_input("bool", "Dieses Programm kann außerdem einen Prefix, oder Suffix ignorieren, den alle PDFs aufweisen.\nMöchtest du einen Pre-, oder Suffix definieren, der ignoriert werden soll?")
        if prefix_suffix:
            def_prefix = get_user_input("bool", "Möchtest du einen Prefix definieren, der bei allen PDFs ignoriert werden soll?")
            if def_prefix:
                prefix = get_user_input("string", "Welcher Prefix soll ignoriert werden?")
            
            def_suffix = get_user_input("bool", "Möchtest du einen Suffix definieren, der bei allen PDFs ignoriert werden soll?")
            if def_suffix:
                suffix = get_user_input("string", "Welcher Prefix soll ignoriert werden?")
            else:
                break
            break
        else:
            break
    while True:
        change_return_adress = get_user_input("bool", "Die Rücksendeadresse lautet standardmäßig:\n'IMIBE UK-Essen, Hufelandstr. 55, 45147 Essen'\nMöchtest du das ändern?")
        if change_return_adress:
            return_adress = get_user_input("string", "Gib die Rücksendeadresse ein, die du verwenden willst")
            if len(return_adress) >= 45:
                approve_return_adress = get_user_input("bool", "Diese Rücksendeadresse ist etwas länger als gewöhnlich. Dies könnte bedeuten, dass sie im Adressfenster nicht richtig zu sehen ist.\nWillst du trotzdem fortfahren?")
                if approve_return_adress:
                    break
                
        else:
            return_adress = "IMIBE UK-Essen, Hufelandstr. 55, 45147 Essen"
            break

    print("Wird ausgeführt...")
    file_numb = 0
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            file_numb +=1
            copy_file_to_dir(f"{input_dir}\\{filename}", output_dir)
    print(f"\n{file_numb} PDFs wurden in das Zielverzeichnis kopiert.")

    adress_data = xlsx_to_array(xlsx_table)
    print(f"\n{len(adress_data)} Adresszeilen wurden aus der XLSX-Tabelle ausgelesen.")

    print(f"\nPDFs werden mit Adressfenstern versehen...")

    pdfs_without_address = add_address_to_pdfs(output_dir, adress_data, return_adress)

    if pdfs_without_address != []:
        print("\n")
        printlb("Die folgenden PDFs konnten nicht in der XLSX-Tabelle gefunden und deshalb nicht bearbeitet werden: ")
        print("")
        for pdf_file in pdfs_without_address:
            print(f"       '{pdf_file}'")
        remove_pdfs_without_adress = get_user_input("bool", "Möchtest du diese PDFs aus dem Ablageordner entfernen?")
        if remove_pdfs_without_adress:
            for pdf_file in pdfs_without_address:
                os.remove(f"{output_dir}\\{pdf_file}")
            print("Die unbearbeiteten PDFs wurden entfernt.")

    input("\nDrücke Enter, um fortzufahren...")


help_text = ["Das Programm automatisiert das Hinzufügen von Adressinformationen zu PDF-Dokumenten. Es liest Adressen aus einer",
             "XLSX-Tabelle aus und fügt sie als Fensteradresse die PDFs ein. Die Adressinformationen werden so positioniert, dass sie",
             "in einem Adressfenster gut zu sehen sind. Dafür musst du nur 3 Informationen angeben:",
             "(1) Den Dateipfad an dem sich die zu bearbeitenden PDFs befinden",
             "(2) Die XLSX-Tabelle in der sich die Adressinformationen befinden und",
             "(3) Den Dateipfad in dem die bearbeiteten Dateien abgelegt werden sollen",
             "\nHinweis: Die Tabelle muss folgendermaßen formatiert sein:",
             "dateiname | anrede |  name   | vorname | strasse   | hausnummer | plz   | ort",
             "F12345    | Herr   | Caesar  | Julius  | Romstraße | 12345      | 00184 | roma",]