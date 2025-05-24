from datetime import date
import datetime

greeting_text = []

def is_ramadan(date_to_check):
    ramadan_dates = {
        2024: (date(2024, 3, 11), date(2024, 4, 9)),
        2025: (date(2025, 3, 1), date(2025, 3, 29)),
        2026: (date(2026, 2, 18), date(2026, 3, 18)),
        2027: (date(2027, 2, 8), date(2027, 3, 7)),
        2028: (date(2028, 1, 28), date(2028, 2, 26)),
        2029: (date(2029, 1, 17), date(2029, 2, 15)),
        2030: (date(2030, 1, 6), date(2030, 2, 4)),
        2031: (date(2031, 12, 26), date(2031, 1, 24)),
        2032: (date(2032, 12, 14), date(2032, 1, 12)),
        2033: (date(2033, 12, 4), date(2033, 1, 2)),
        2034: (date(2034, 11, 24), date(2034, 12, 23)),
        2035: (date(2035, 11, 14), date(2035, 12, 12)),
    }

    year = date_to_check.year

    if year not in ramadan_dates: return False
    else:
        greeting_text.append("تقبل الله منا ومنكم\n")
        greeting_text.append("عيد مبارك وتقبل الله صيامكم\n")
        greeting_text.append("اللهم تقبل منا صالح الأعمال\n")
        greeting_text.append("Taqabbal Allahu minna wa minkum\n")
        greeting_text.append("Eid Mubarak wa taqabbal Allahu siyamakum\n")
        greeting_text.append("Allahumma taqabbal minna salih al-a'mal\n")

        start_ramadan, end_ramadan = ramadan_dates[year]
        return start_ramadan <= date_to_check <= end_ramadan

def print_greeting():
    for line in greeting_text:
        print(line)

# MAIN CODE
today = datetime.date.today()
today = date(2025, 3, 10)

is_ramadan(today)
print_greeting()
