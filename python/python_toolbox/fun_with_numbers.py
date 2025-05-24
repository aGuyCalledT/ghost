from programs.utils import get_user_input
from time import time, sleep
import locale, os, sys
def print_all_numbers(input_number : int):
    current_numb = 1
    current_line = ""
    while current_numb <= input_number +1:
        if len(current_line) >= 50 or current_numb == input_number:
            print(current_line)
            current_line = ""

        current_line += f"{current_numb:,} ".replace(",", ".")
        current_numb += 1


def clear_last_line():
    sys.stdout.write('\033[F')  # Gehe zur vorherigen Zeile
    sys.stdout.write('\033[K')  # Lösche die aktuelle Zeile


def fun_with_numbs():
    while True:
        user_input = get_user_input("int", "Gib eine Zahl ein!")
        start_time = time()
        print_all_numbers(user_input)
        processing_time = round(time() - start_time, 3)
        print(f"Das hat {processing_time} Sekunden gedauert")
        print("********************************************************")


def banner_roll(banner_text : str, next_line : str = None):
    print(banner_text)
    print(next_line)
    for x in range(len(banner_text)):
        if next_line is not None:
            clear_last_line()
        clear_last_line()
        print(banner_text)
        if next_line is not None: print(next_line)
        sleep(0.01)
        roll_char = banner_text[0]
        banner_text = banner_text[1:]+roll_char
    if next_line is not None:
            clear_last_line()
    clear_last_line()
    print(banner_text)
    if next_line is not None: print(next_line)
        



#MAIN CODE
print      ("*************************************************************************")
banner_roll("***************************Python Toolbox********************************",
            "*************************************************************************")

    