import fitz, os
from PIL import Image, ImageDraw, ImageFont
import PyPDF2
from .utils import get_user_input, create_dir, copy_file_to_dir, count_pdfs, pdf_liste_erstellen

def pdf_erste_seite_zu_png(pdf_pfad, png_pfad=None, dpi=150): # dpi als Argument hinzufügen
    doc = fitz.open(pdf_pfad)
    page = doc.load_page(0)
    mat = fitz.Matrix(dpi / 72, dpi / 72) # Skalierungsmatrix erstellen
    pix = page.get_pixmap(matrix=mat) 

    if not png_pfad:
        png_pfad = pdf_pfad.replace(".pdf", ".png")

    pix.save(png_pfad)
    return png_pfad


def insert_white_stripe(image_path, stripe_width, stripe_position="center", opacity=1.0):
    # Bild öffnen
    img = Image.open(image_path)
    img = img.convert("RGBA") 

    # stripe_position in Pixelposition umrechnen
    if stripe_position == "top":
        stripe_pos = 0
    elif stripe_position == "bottom":
        stripe_pos = img.height - stripe_width  # Streifen beginnt kurz vor dem unteren Rand
    elif stripe_position == "center":
        stripe_pos = 450
    else:
        raise ValueError("Ungültige Streifenposition. Wählen Sie 'top', 'bottom' oder 'center'.")

    # Neue Bildgröße berechnen
    new_height = img.height + stripe_width

    # Neues Bild erstellen
    new_img = Image.new('RGBA', (img.width, new_height), (0, 0, 0, 0)) 

    # Unteren Teil des Originalbildes mit Offset einfügen
    bottom_part = img.crop((0, stripe_pos, img.width, img.height))
    new_img.paste(bottom_part, (0, stripe_pos + stripe_width))

    # Oberen Teil des Originalbildes einfügen (falls stripe_position nicht "top" ist)
    if stripe_position != "top":
        top_part = img.crop((0, 0, img.width, stripe_pos))
        new_img.paste(top_part, (0, 0))

    # Streifen erstellen
    stripe = Image.new('RGBA', (img.width, stripe_width), (255, 255, 255, int(255 * opacity)))

    # Streifen einfügen
    new_img.paste(stripe, (0, stripe_pos))

    # Bild speichern
    new_img.save(image_path)


def remove_bottom_pixels(image_path, num_pixels=200):
    try:
        img = Image.open(image_path)

        # Überprüfen, ob das Bild im PNG-Format ist
        if img.format != 'PNG':
            raise ValueError("Das Bild muss im PNG-Format sein.")

        width, height = img.size
        new_height = height - num_pixels

        # Sicherstellen, dass genügend Pixel zum Entfernen vorhanden sind
        if new_height <= 0:
            raise ValueError("Nicht genügend Pixel zum Entfernen. Das Bild ist zu klein.")

        # Bild zuschneiden
        cropped_img = img.crop((0, 0, width, new_height))

        # Speichern des zugeschnittenen Bildes (optional, überschreibt Original)
        cropped_img.save(image_path)

    except FileNotFoundError:
        print(f"Fehler (remove_bottom_pixels): Die Datei '{image_path}' wurde nicht gefunden.")
    except ValueError as e:
        print(f"Fehler (remove_bottom_pixels): {e}")
    except OSError:
        print("Fehler (remove_bottom_pixels): Ein Problem beim Öffnen oder Verarbeiten des Bildes ist aufgetreten.")


def convert_png_to_pdf(png_path, pdf_path=None):
    try:
        img = Image.open(png_path)
        if img is None:
            raise ValueError("Das Bild konnte nicht geöffnet werden.")
        if img.format != 'PNG':
            raise ValueError("Das Bild muss im PNG-Format sein.")
        if pdf_path is None:
            pdf_path = png_path.replace(".png", ".pdf")

        # Aktuelle Auflösung und Größe des Bildes ermitteln
        current_dpi = img.info.get('dpi', (72, 72))  # Standardmäßig 72 DPI annehmen, falls nicht vorhanden
        width, height = img.size

        # Neue Abmessungen basierend auf der Zielauflösung berechnen
        target_dpi = 72
        new_width = int(width * target_dpi / current_dpi[0])
        new_height = int(height * target_dpi / current_dpi[1])

        # Bild herunterskalieren
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        # Bild in PDF konvertieren
        resized_img.save(pdf_path, "PDF", resolution=100.0)

    except FileNotFoundError:
        print(f"Fehler (convert_png_to_pdf): Die Datei '{png_path}' wurde nicht gefunden.")
    except ValueError as e:
        print(f"Fehler (convert_png_to_pdf): {e}")
    except OSError as e:
        print(f"Fehler (convert_png_to_pdf): Ein Problem beim Öffnen oder Verarbeiten des Bildes ist aufgetreten: {e}")
    except Exception as e:
        print(f"Fehler (convert_png_to_pdf): Unerwarteter Fehler: {e}")


def dateinamen_in_pdf_schreiben(pdf_datei_pfad):
    with open(pdf_datei_pfad, 'rb') as pdf_datei:
        pdf_reader = PyPDF2.PdfReader(pdf_datei)
        pdf_writer = PyPDF2.PdfWriter()

        # Erste Seite holen
        seite = pdf_reader.pages[0]

        # Dateinamen extrahieren
        dateiname = pdf_datei_pfad.split('/')[-1]  # Nur den Dateinamen, ohne Pfad

        # Text hinzufügen (unten rechts)
        seite.add_text(dateiname, (seite.mediabox.right - 100, 20), fontsize=10) 

        # Seite zum Writer hinzufügen
        pdf_writer.add_page(seite)

        # Neue PDF-Datei schreiben (mit "_bearbeitet" am Ende)
        with open(pdf_datei_pfad.replace('.pdf', '_bearbeitet.pdf'), 'wb') as ausgabe_datei:
            pdf_writer.write(ausgabe_datei)


def write_id_to_corner(image_path, corner_id="KEINE ID", font_size=80, font_path=None, text_color=(0, 0, 0)):
    # Überprüfung, ob die Bilddatei existiert
    if not os.path.exists(image_path):
        print(f"Fehler (write_id_to_corner): Die Datei '{image_path}' wurde nicht gefunden.")
        return

    try:
        img = Image.open(image_path)

        # Konvertierung in RGBA, falls erforderlich
        if img.format != 'PNG':
            img = img.convert('RGBA')

        draw = ImageDraw.Draw(img)
        width, height = img.size

        # Schriftart laden (optional)
        if font_path:
            try:
                font = ImageFont.truetype(font_path, font_size)
            except OSError:
                print(f"Fehler (write_id_to_corner): Die Schriftartdatei '{font_path}' konnte nicht geöffnet werden. Die Standardschriftart wird verwendet.")
                font = ImageFont.load_default()
        else:
            font = ImageFont.load_default()

        # Textgröße berechnen
        text_bbox = draw.textbbox((0, 0), corner_id, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Position für den Text berechnen (unten rechts mit etwas Abstand)
        x = width - text_width - 120
        y = height - text_height - 100

        # Text zeichnen
        draw.text((x, y), corner_id, font=font, fill=text_color)

        # Bild speichern (überschreibt Original)
        img.save(image_path)

    except OSError as e:
        print(f"Fehler (write_id_to_corner): Ein Problem beim Öffnen oder Verarbeiten des Bildes ist aufgetreten: {e}")


def append_pdf_without_first_page(pdf_head_path, pdf_body_path, output_path):
    try:
        with open(pdf_head_path, 'rb') as head_file, open(pdf_body_path, 'rb') as body_file:
            head_reader = PyPDF2.PdfReader(head_file)
            body_reader = PyPDF2.PdfReader(body_file)

            writer = PyPDF2.PdfWriter()

            # Seiten von pdf_head hinzufügen
            for page in head_reader.pages:
                writer.add_page(page)

            # Seiten von pdf_body ab der zweiten Seite hinzufügen
            for page in body_reader.pages[1:]:  # Startet bei Index 1, um die erste Seite zu überspringen
                writer.add_page(page)

            # Neue PDF-Datei schreiben
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

    except FileNotFoundError:
        print(f"Fehler: Eine der PDF-Dateien wurde nicht gefunden.")
    except PyPDF2.utils.PdfReadError:
        print(f"Fehler: Eine der PDF-Dateien ist beschädigt oder kann nicht gelesen werden.")
    except Exception as e:
        print(f"Fehler: Ein unerwarteter Fehler ist aufgetreten: {e}")


help_text = "bleep bloop, den Hilfe Text hab ich noch nicht geschrieben :("

# MAIN CODE
'''
current_pdf = "\\F81.pdf"
pdf_folder = "C:\\Python\\python_toolbox\\PDFs"

current_png = "\\temp.png"
temp_folder = "C:\\Python\\python_toolbox\\temp"

pdf_final_folder = "C:\\Python\\python_toolbox\\PDFs\\edited"
font = "C:\\Python\\python_toolbox\\programs\\FiraCode-Light.ttf"

absatz_abstand = 150
auflösung = 150


komm_id = current_pdf.split("\\")[-1][:-4][1:]
pdf_erste_seite_zu_png(pdf_folder+current_pdf, f"{temp_folder}{current_png}", auflösung)
insert_white_stripe(f"{temp_folder}{current_png}", absatz_abstand)
remove_bottom_pixels(f"{temp_folder}{current_png}", absatz_abstand)
write_id_to_corner(f"{temp_folder}{current_png}", komm_id, font_path=font, font_size=30)
convert_png_to_pdf(f"{temp_folder}{current_png}", f"{pdf_final_folder}{current_pdf}")
append_pdf_without_first_page(f"{pdf_final_folder}{current_pdf}", f"{pdf_folder}{current_pdf}", f"{pdf_final_folder}{current_pdf}")
'''

def run_this_program ():
    input_dir  = get_user_input("path", "Gib den Pfad des Ordners ein, der die zu bearbeitenden PDFs enthält")
    pdf_num = count_pdfs(input_dir)
    print(f"Der Ordner enthält {pdf_num} PDFs")
    output_dir = get_user_input("path", "Gib den Pfad des Ordners ein, in dem die bearbeiteten PDFs abgelegt werden sollen")

    input("\nDrücke Enter, um fortzufahren...")
    
    pdf_liste = pdf_liste_erstellen(input_dir)
    pdf_folder = input_dir
    temp_folder = f"{output_dir}{"\\temp"}"
    temp_png = f"{temp_folder}\\temp.png"
    create_dir(temp_folder)
    pdf_final_folder = output_dir
    font = "programs\\FiraCode-Light.ttf"
    absatz_abstand = 150
    auflösung = 150
    counter = 0

    for pdf in pdf_liste:
        counter += 1
        komm_id = pdf.split("\\")[-1][:-4][1:]

        print(f"[{counter}] F{komm_id} wird bearbeitet...")

        output_pdf = f"{output_dir}\\F{komm_id}.pdf"
        pdf_erste_seite_zu_png(pdf, temp_png)
        insert_white_stripe(temp_png, absatz_abstand)
        remove_bottom_pixels(temp_png, absatz_abstand)
        write_id_to_corner(temp_png, komm_id, font_path=font, font_size=20)
        convert_png_to_pdf(temp_png, output_pdf)
        append_pdf_without_first_page(output_pdf,pdf,output_pdf)


    input("\nDrücke Enter, um fortzufahren...")
