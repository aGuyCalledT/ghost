import qrcode
from qrcode import constants

def generate_qr_code(url, fill_color="black", back_color="white", filename="qrcode.png"):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"QR-Code erfolgreich als '{filename}' mit Vordergrundfarbe '{fill_color}' und Hintergrundfarbe '{back_color}' gespeichert.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    link_eingabe = input("Bitte gib den Link ein, für den du einen QR-Code generieren möchtest: ")
    farbe_eingabe = input("Bitte gib die gewünschte Farbe für den QR-Code (HTML-Farbcode, z.B. #FF0000 für Rot) ein (Standard: black): ") or "black"
    hintergrund_eingabe = input("Bitte gib die gewünschte Hintergrundfarbe (HTML-Farbcode, z.B. #FFFFFF für Weiß) ein (Standard: white): ") or "white"
    dateiname_eingabe = input("Bitte gib den gewünschten Dateinamen für das Bild ein (z.B. mein_qr_code.png): ")
    generate_qr_code(link_eingabe, farbe_eingabe, hintergrund_eingabe, dateiname_eingabe)