# ---------------  Main Code  ---------------
import os, sys, platform
import interface_support as interface
from programs import utils
from datetime import datetime
from fuzzywuzzy import fuzz

version_date = "2025-03-27"
exp_date     = "2030-01-01"
current_date = datetime.now().strftime('%Y-%m-%d')

if interface.is_expired(exp_date, current_date):
    pass

packages= [
        "utils",
        "leere_seite",
        'sortieren_nach_dateiname',
        'fensteradressev2',
        'f_numb_checker',
    ]
setup(packages)
display_title()
display_greeting()
display_contact()
display_program_list(packages)

user_input = utils.get_user_input("str", "Gib 'start <Programm Name>' ein, um ein Programm auszuführen. Wenn du Hilfe brauchst, gib 'hilfe', oder 'hilfe <Programm Name>' ein.")
user_input = standardize_user_input(user_input, packages)
