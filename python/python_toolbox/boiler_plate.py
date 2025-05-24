from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

optionen = ["Apfel", "Banane", "Kirsche"]
wort_completer = WordCompleter(optionen)

eingabe = prompt("Geben Sie eine Frucht ein: ", completer=wort_completer)
print("Sie haben eingegeben:", eingabe)