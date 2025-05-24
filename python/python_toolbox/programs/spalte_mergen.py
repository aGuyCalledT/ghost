import pandas as pd
from utils import get_user_input

def fuellen_leerer_zellen(datei_pfad, ausgabe_datei):
    try:
        # Excel-Datei einlesen
        df = pd.read_excel(datei_pfad)

        # Spaltenindizes definieren
        spalte_6_index = 6  # Spaltenindizes beginnen bei 0
        spalte_26_index = 26

        # Leere Zellen in Spalte 6 mit Inhalt von Spalte 26 füllen
        df.iloc[:, spalte_6_index] = df.iloc[:, spalte_6_index].fillna(df.iloc[:, spalte_26_index])

        # Geänderte Tabelle in neue Excel-Datei speichern
        df.to_excel(ausgabe_datei, index=False)

        print(f"Leere Zellen in Spalte 6 erfolgreich gefüllt und in '{ausgabe_datei}' gespeichert.")

    except FileNotFoundError:
        print("Fehler: Die angegebene Datei wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf
datei_pfad = get_user_input("path", "Bitte geben Sie den Pfad zur XLSX-Datei an:")
ausgabe_datei = get_user_input("str", "Bitte geben Sie den Pfad für die Ausgabedatei an:")

fuellen_leerer_zellen(datei_pfad, ausgabe_datei)