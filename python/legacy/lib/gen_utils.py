import os

def check_int_within_bounds(value, min_int=None, max_int=None):
  if min_int is not None and value < min_int:
    return False

  if max_int is not None and value > max_int:
    return False

  return True


def get_user_input(input_type, input_message=None, valid_strings=None, min_int=None, max_int=None):
    while True:
        if input_message is None:
            user_input = input(f"\n> ")
        else:
            user_input = input(f"\n{input_message}\n> ")

        if input_type == 'str':
            if valid_strings is None:
                return user_input
            elif user_input in valid_strings:
                return user_input
            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine der folgenden Optionen:\n", valid_strings)

        elif input_type == 'int':
            try:
                user_input_valid_int = int(user_input)
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
            else:
                if check_int_within_bounds(user_input_valid_int, min_int, max_int):
                    return user_input_valid_int
                else:
                    print(f"Ungültiger Wert. Der Wert muss zwischen {min_int} und {max_int} liegen.")
                    continue  # Hier fordern wir einen neuen Input an

        elif input_type == 'path':
            if os.path.exists(user_input):
                return user_input
            else:
                print("Ungültiger Dateipfad. Bitte geben Sie einen existierenden Pfad ein.")

        elif input_type == 'bool':
            if user_input.lower() in ['y', 'yes', 'j', 'ja', 't', 'true']:
                return True
            elif user_input.lower() in ['n', 'no', 'nein', 'f', 'false']:
                return False
            else:
                print("Ungültige Eingabe. Die Eingabe muss 'ja' oder 'nein' sein.")
        

        else:
            raise ValueError(f"Ungültige Eingabe. Die Eingabe muss {input_type} sein")
        

