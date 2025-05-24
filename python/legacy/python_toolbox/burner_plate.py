import os
import shutil
import openpyxl

def pdfs_verschieben(excel_datei, quellordner, zielordner):
  # Excel-Datei laden
  workbook = openpyxl.load_workbook(excel_datei)
  worksheet = workbook.active

  # PDF-Namen aus der Excel-Tabelle extrahieren
  pdf_namen = []
  for row in worksheet.iter_rows():
    for cell in row:
      pdf_namen.append(cell.value)

  # PDFs verschieben
  for dateiname in os.listdir(quellordner):
    if dateiname.endswith(".pdf") and dateiname in pdf_namen:
      quellpfad = os.path.join(quellordner, dateiname)
      zielpfad = os.path.join(zielordner, dateiname)
      shutil.move(quellpfad, zielpfad)