import qrcode
from pyzbar.pyzbar import decode
from PIL import Image, ImageDraw, ImageFont  # Importiere die notwendigen Module

def qr_code_generator(data, filename, text, pfad="qr_codes/"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Konvertiere das QR-Code-Bild in den RGB-Modus
    img = img.convert("RGB")

    # Text hinzufügen
    if text:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:\\Users\\timwi\\Documents\\ttf\\FiraCode-VF.ttf", 60)  # Oder einen anderen verfügbaren Font
        text_width = draw.textlength(text, font=font)
        qr_width, qr_height = img.size

        # Erstelle ein neues Bild mit Platz für den Text
        new_img_height = qr_height + 100  # 40 Pixel Abstand zwischen QR-Code und Text
        new_img = Image.new('RGB', (qr_width, new_img_height), 'white')

        # Füge den QR-Code in das neue Bild ein (mit expliziter Größenangabe)
        new_img.paste(img, (0, 0, qr_width, qr_height))

        # Zeichne den Text in das neue Bild
        draw = ImageDraw.Draw(new_img)
        x = (qr_width - text_width) / 2
        y = qr_height + 10  # Abstand zwischen QR-Code und Text
        draw.text((x, y), text, font=font, fill="black")

        img = new_img

    try:
        img.save(pfad + filename)
        print(f"QR-Code wurde erfolgreich unter {pfad + filename} gespeichert.")
    except FileNotFoundError:
        print(f"Fehler: Das Verzeichnis '{pfad}' wurde nicht gefunden.")



def qr_code_leser(bildpfad):
    try:
        # Bild öffnen
        bild = Image.open(bildpfad)

        # QR-Codes im Bild dekodieren
        qr_codes = decode(bild)

        # Daten aus dem ersten QR-Code extrahieren
        if qr_codes:
            daten = qr_codes[0].data.decode('utf-8')
            return daten
        else:
            print("Kein QR-Code im Bild gefunden.")
            return None
    except FileNotFoundError:
        print(f"Fehler: Bilddatei '{bildpfad}' nicht gefunden.")
        return None


def qr_code_reader(bildpfad):
  try:
    # Bild öffnen
    bild = Image.open(bildpfad)

    # QR-Codes im Bild dekodieren
    qr_codes = decode(bild)

    # Daten aus dem ersten QR-Code extrahieren
    if qr_codes:
      daten = qr_codes[0].data.decode('utf-8')
      return daten
    else:
      print("Kein QR-Code im Bild gefunden.")
      return None
  except FileNotFoundError:
    print(f"Fehler: Bilddatei '{bildpfad}' nicht gefunden.")
    return None


# Beispielaufruf
daten = "WIFI:T:WPA;S:Sky's & T's Gaeste WLAN;P:nintendo;H:false;"
dateiname = "new_qr_code.png"
verzeichnis = "C:\\Users\\timwi\\OneDrive\\Desktop"  # Ändere dies in dein gewünschtes Verzeichnis
text = "Gäste WLAN"

bild_pfad = "C:\\Users\\timwi\\Desktop\\download.png"  
# daten = qr_code_leser(bild_pfad)

qr_code_generator(daten, dateiname, text, verzeichnis)

 # >_