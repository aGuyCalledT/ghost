from lib import lists
attribut_mod = {
    1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1,
    13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7,
    25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10
}
xp = {
    0: 10, 0.125: 25, 0.25: 50, 0.5: 100, 1: 200, 2: 450, 3: 700, 4: 1100, 5: 1800, 6: 2300,
    7: 2900, 8: 3900, 9: 5000, 10: 5900, 11: 7200, 12: 8400, 13: 10000, 14: 11500, 15: 13000,
    16: 15000, 17: 18000, 18: 20000, 19: 22000, 20: 25000, 21: 33000, 22: 41000, 23: 50000,
    24: 62000, 30: 155000,
}

zauberwirkungsbonus = {
    "barde": {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 4, 7: 4, 8: 4, 9: 5, 10: 5, 11: 5, 12: 5, 13: 6, 14: 6, 15: 6, 16: 6, 17: 7, 18: 7, 19: 7, 20: 7},
    "kleriker": {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 4, 7: 4, 8: 4, 9: 5, 10: 5, 11: 5, 12: 6, 13: 6, 14: 6, 15: 6, 16: 7, 17: 7, 18: 7, 19: 7, 20: 8},
    "druide": {1: 2, 2: 2, 3: 3, 4: 3, 5: 3, 6: 4, 7: 4, 8: 4, 9: 5, 10: 5, 11: 5, 12: 6, 13: 6, 14: 6, 15: 6, 16: 7, 17: 7, 18: 7, 19: 7, 20: 8},
    "hexenmeister": {1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 4, 8: 5, 9: 5, 10: 5, 11: 6, 12: 6, 13: 6, 14: 7, 15: 7, 16: 7, 17: 8, 18: 8, 19: 8, 20: 9},
    "magier": {1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 4, 8: 5, 9: 5, 10: 5, 11: 6, 12: 6, 13: 6, 14: 7, 15: 7, 16: 7, 17: 8, 18: 8, 19: 8, 20: 9},
    "paladin": {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 3, 13: 4, 14: 4, 15: 4, 16: 4, 17: 4, 18: 5, 19: 5, 20: 5},
    "waldläufer": {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 3, 13: 3, 14: 3, 15: 4, 16: 4, 17: 4, 18: 4, 19: 5, 20: 5},
    "zauberer": {1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4, 7: 4, 8: 5, 9: 5, 10: 5, 11: 6, 12: 6, 13: 6, 14: 7, 15: 7, 16: 7, 17: 8, 18: 8, 19: 8, 20: 9},
}

zauber_attribut = {
    "barde" : "charisma",
    "kleriker" : "weisheit",
    "druide" : "weisheit",
    "hexenmeister" : "charisma",
    "magier" : "intelligenz",
    "paladin" : "charisma",
    "waldläufer" : "weisheit",
    "zauberer" : "charisma"
}

gender_symbol = {
      "männlich": "M",
      "weiblich": "W",
      "divers": "D"
  }

sexualität_symbol = {
    "lesbisch" : "⚢",
    "schwul" : "⚣",
    "pansexuell" : "⚤",
    "asexuell" : "⚲",
    "heterosexuell" : "",
    "homosexuell" : "⚤"
}

namens_kultur = {
    "benu" : lists.benu_silben,
    "elf" : lists.elf_silben,
    "halbling" : lists.halbling_silben,
    "calishiter" : [lists.römische_silben_anfang, lists.römische_silben_ende_männlich, lists.römische_silben_ende_weiblich],
    "chondathaner" : [lists.deutsche_silben_anfang, lists.deutsche_silben_ende_männlich, lists.deutsche_silben_ende_weiblich],
    "damaraner": [lists.deutsche_silben_anfang, lists.deutsche_silben_ende_männlich, lists.deutsche_silben_ende_weiblich],
    "illuskaner" : lists.skandinavische_silben,
    "mulaner" : lists.japanische_silben,
    "rashemier" : lists.afrikanische_silben,
    "shouer" : lists.japanische_silben,
    "tethyrianer" : [lists.römische_silben_anfang, lists.römische_silben_ende_männlich, lists.römische_silben_ende_weiblich],
    "turamier" : lists.afrikanische_silben,
    "zwerg" : lists.zwerg_silben,
    "drachenblütiger" : lists.benu_silben,
    "gnom" : lists.zwerg_silben,
    "tiefling" : lists.tiefling_silben,
    "halbork" : [lists.römische_silben_anfang, lists.römische_silben_ende_männlich, lists.römische_silben_ende_weiblich],

}

pron = {
    "er"  :{"nom" : "er", "gen" : "seine", "dat" : "ihm", "akk" : "ihn", "art" : "der", "pos" : "seinen"},
    "sie" :{"nom" : "sie", "gen" : "ihre", "dat" : "ihr", "akk" : "sie", "art" : "die", "pos" : "ihren"},
    "es"  :{"nom" : "es", "gen" : "dessen", "dat" : "ihm", "akk" : "es", "art" : "das", "pos" : "seinen"},
    "they":{"nom" : "they", "gen" : "their", "dat" : "their", "akk" : "them", "art" : "the", "pos" : "their"},
    "xie" :{"nom" : "xie", "gen" : "xiere", "dat" : "xier", "akk" : "xie", "art" : "xie", "pos" :"xieren"},
    "xer" :{"nom" : "xer", "gen" : "xeine", "dat" : "xim", "akk" : "xin", "art" : "xer", "pos" : "xeinen"}, 
    "pl"  :{"nom" : "sie", "gen" : "ihre", "dat" : "ihnen", "akk" : "sie", "art" : "die", "pos" : "ihren"},
}

pos_pron = {
    "er" : {
    "nom": ["sein", "seine", "sein"],
    "gen": ["seines", "seiner", "seines"],
    "dat": ["seinem", "seiner", "seinem"],
    "akk": ["seinen", "seine", "sein"]},

    "sie" : {
    "nom": ["ihr", "ihre", "ihr"],
    "gen": ["ihres", "ihrer", "ihres"],
    "dat": ["ihrem", "ihrer", "ihrem"],
    "akk": ["ihren", "ihre", "ihr"]},

    "es" : {
    "nom": ["sein", "seine", "sein"],
    "gen": ["seines", "seiner", "seines"],
    "dat": ["seinem", "seiner", "seinem"],
    "akk": ["seinen", "seine", "sein"]},

}