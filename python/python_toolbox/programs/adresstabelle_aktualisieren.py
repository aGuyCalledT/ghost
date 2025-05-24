import pandas as pd
from utils import get_user_input

def aktualisiere_adressen(alte_adressen_datei, neue_adressen_datei, ausgabe_datei):
    try:
        # Excel-Dateien einlesen
        alte_adressen = pd.read_excel(alte_adressen_datei)
        neue_adressen = pd.read_excel(neue_adressen_datei)

        # ID-Spalten in DataFrames umbenennen, um sie leichter zu vergleichen
        alte_adressen = alte_adressen.rename(columns={alte_adressen.columns[0]: 'ID'})
        neue_adressen = neue_adressen.rename(columns={neue_adressen.columns[0]: 'ID'})

        # Aktualisierte Adressen ermitteln
        neue_ids = neue_adressen['ID'].tolist()
        aktualisierte_adressen = pd.concat([
            neue_adressen[neue_adressen['ID'].isin(neue_ids)],
            alte_adressen[~alte_adressen['ID'].isin(neue_ids)]
        ]).sort_values(by='ID')

        # Aktualisierte Adressen in Excel-Datei ausgeben
        aktualisierte_adressen.to_excel(ausgabe_datei, index=False)

        print(f"Adressen erfolgreich aktualisiert und in '{ausgabe_datei}' gespeichert.")

    except FileNotFoundError:
        print("Fehler: Eine der Eingabedateien wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf
alte_adressen_datei = get_user_input("path", "Bitte gib den Dateipfad von der alten Adressliste an")
neue_adressen_datei = get_user_input("path", "Bitte gib den Dateipfad von der aktualisierten Adressliste an")
ausgabe_datei = get_user_input("str", "Wo soll das ganze gespeichert werden?")

aktualisiere_adressen(alte_adressen_datei, neue_adressen_datei, ausgabe_datei)