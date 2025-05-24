ALPHABET = (
    '0123456789' +
    'abcdefghijklmnopqrstuvwxyz' +
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~><' # Alle druckbaren Sonderzeichen
)

BASE = len(ALPHABET)

def encode(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError("Die Eingabe muss eine ganze Zahl sein.")
    if number < 0:
        raise ValueError("Die Zahl muss nicht-negativ sein, um komprimiert zu werden.")

    # Wenn die Zahl 0 ist, gib das erste Zeichen des Alphabets zurück.
    if number == 0:
        return ALPHABET[0]

    result = []
    # Schleife, solange die Zahl größer als 0 ist
    while number > 0:
        # Berechne den Rest der Division durch die Basis
        remainder = number % BASE
        # Füge das entsprechende Zeichen aus dem Alphabet zur Ergebnisliste hinzu
        result.append(ALPHABET[remainder])
        # Teile die Zahl ganzzahlig durch die Basis
        number //= BASE

    # Die Zeichen wurden in umgekehrter Reihenfolge gesammelt,
    # daher muss die Liste umgekehrt und zu einer Zeichenkette verbunden werden.
    return ''.join(reversed(result))

def decode(encoded_string: str) -> int:
    if not isinstance(encoded_string, str):
        raise TypeError("Die Eingabe muss eine Zeichenkette sein.")
    if not encoded_string:
        raise ValueError("Die Zeichenkette darf nicht leer sein.")

    number = 0
    # Iteriere über jedes Zeichen in der Zeichenkette
    for char in encoded_string:
        # Finde den Index (Wert) des Zeichens im Alphabet
        try:
            index = ALPHABET.index(char)
        except ValueError:
            # Wenn das Zeichen nicht im Alphabet gefunden wird, ist es ungültig
            raise ValueError(f"Ungültiges Zeichen in der Zeichenkette: '{char}'")

        # Aktualisiere die Zahl: (aktuelle Zahl * Basis) + Index des Zeichens
        number = number * BASE + index
    return number

# --- MAIN CODE ---

while True:
    print("\nDo you want to encode or decode?")
    init_user_input = input("(e/d) >")

    if init_user_input == "e":
        while True:
            print("\nEnter a random long number:")
        
            user_input = input("> ")

            try:
                user_input = int(user_input)
            except ValueError:
                print("This is not a number!")
                continue


            encoded_input = encode(user_input)
            print("\nThis is your encoded number:")
            print(encoded_input)
            break

    elif init_user_input == "d":
            while True:
                print("Enter an encoded number:")
        
                user_input = input("> ")


                decoded_input = decode(user_input)
                print("This is your decoded number:")
                print(decoded_input)
                break

    else:
        print(f"Invalid input '{init_user_input}'")















