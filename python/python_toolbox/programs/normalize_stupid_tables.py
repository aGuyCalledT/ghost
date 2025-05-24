import pandas as pd

def erste_spalte_als_liste(dateipfad):
    try:
        df = pd.read_excel(dateipfad)
        erste_spalte = df.iloc[:, 0].tolist()
        return erste_spalte

    except FileNotFoundError:
        print(f"Fehler: Datei nicht gefunden: {dateipfad}")
        return None
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return None


def string_aufteilen(eingabe_string):
  komma_index = eingabe_string.find(",")
  if komma_index == -1:
    return None  # Kein Komma gefunden

  erster_teil = eingabe_string[:komma_index]
  zweiter_teil = eingabe_string[komma_index + 1 :]
  return erster_teil, zweiter_teil

def liste_in_xlsx_spalte_einfuegen(dateipfad, liste, spaltennummer):
    try:
        df = pd.read_excel(dateipfad)

        # Stelle sicher, dass die Spaltennummer gültig ist
        if spaltennummer < 0:
            raise ValueError("Spaltennummer muss nicht negativ sein.")

        # Stelle sicher, dass der Dataframe groß genug ist.
        if len(liste) > len(df):
            differenz = len(liste) - len(df)
            for i in range(differenz):
                df.loc[len(df)] = [None] * len(df.columns)

        # Stelle sicher, dass der Dataframe genug Spalten hat.
        if spaltennummer >= len(df.columns):
          differenz = (spaltennummer + 1) - len(df.columns)
          for i in range(differenz):
            df[len(df.columns)] = None

        # Füge die Liste in die gewünschte Spalte ein
        df.iloc[:len(liste), spaltennummer] = liste

        # Speichere die Änderungen in der XLSX-Datei
        df.to_excel(dateipfad, index=False)

    except FileNotFoundError:
        print(f"Fehler: Datei nicht gefunden: {dateipfad}")
    except ValueError as e:
        print(f"Fehler: {e}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def neue_xlsx_tabelle_erstellen(dateipfad, spalte_a, spalte_b):
    try:
        df = pd.DataFrame({'Spalte 1': spalte_a, 'Spalte 2': spalte_b})
        df.to_excel(dateipfad, index=False)
        print(f"Neue Excel-Tabelle erstellt: {dateipfad}")
    except Exception as e:
        print(f"Fehler beim Erstellen der Excel-Tabelle: {e}")

# MAIN CODE
dateipfad_rohdaten = "C:\\Users\\timwi\\OneDrive\\Desktop\\optilater.ods"
dateipfad_feindaten = "C:\\Users\\timwi\\OneDrive\\Desktop\\KOMMIDs_split.xlsx"

spalten_werte = erste_spalte_als_liste(dateipfad_rohdaten)

spalte_a = []
spalte_b = []

for element in spalten_werte:
    teile = string_aufteilen(element)
    if teile:
        element_a, element_b = teile
        spalte_a.append(f"F{element_a}")
        spalte_b.append(element_b)
    else:
        spalte_a.append(None)
        spalte_b.append(None)

neue_xlsx_tabelle_erstellen(dateipfad_feindaten, spalte_a, spalte_b)