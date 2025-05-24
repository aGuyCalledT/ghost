from char import Char

class Spieler(Char):
    def __init__(self, is_player=True, stufe=1, klasse="keine_klasse", trefferpunkte=10, rüstungsklasse=None, bewegungsrate=9, hg=0.25, status=[], größe="Mittelgroß", allignment=None, volk=None, name="Bürger", eigenname=None, gender=None, trans=None, sexualität=None, pronomen=None, bewegungsart=..., geübt=..., random_geübt=3, stärke=10, konstitution=10, geschicklichkeit=10, charisma=10, weisheit=10, intelligenz=10):
        super().__init__(is_player, stufe, klasse, trefferpunkte, rüstungsklasse, bewegungsrate, hg, status, größe, allignment, volk, name, eigenname, gender, trans, sexualität, pronomen, bewegungsart, geübt, random_geübt, stärke, konstitution, geschicklichkeit, charisma, weisheit, intelligenz)

atrophaea = Spieler(
    stufe= 4,
    klasse= "artifizient",
    rüstungsklasse = 16,
    bewegungsrate = 10.5,
    allignment="True Neutral",
    volk="waldelfe",
    name= "Abenteurerin",
    eigenname="Atrophaea",
    gender = "weiblich",
    sexualität= "lesbisch",
    trans= "cis",
    pronomen="sie",
    stärke=5,
    geschicklichkeit=20,
    konstitution=8,
    intelligenz=18,
    weisheit=14,
    charisma=10,

    geübt=["fingerfertigkeit", "motiv_erkennen", "naturkunde", "überzeugen", "wahrnehmung"] 
)

ragelion = Spieler(
    stufe= 4,
    klasse= "paladin",
    rüstungsklasse = 18,
    bewegungsrate = 9,
    allignment="Rechtschaffend Gut",
    volk="halbhochelf",
    name= "Abenteurer",
    eigenname="Ragelion",
    gender = "männlich",
    sexualität= "pansexuell",
    trans= "cis",
    pronomen="er",
    stärke=17,
    geschicklichkeit=9,
    konstitution=18,
    intelligenz=11,
    weisheit=12,
    charisma=20,

    geübt=["athletik", "einschüchtern", "motiv_erkennen", "nachforschen", "überzeugen", "wahrnehmung"] 
)

cornelius = Spieler(
    stufe= 4,
    klasse= "magier",
    rüstungsklasse = 15,
    bewegungsrate = 9,
    allignment="Neutral Gut",
    volk="halbhochelf",
    name= "Abenteurer",
    eigenname="Cornelius",
    gender = "männlich",
    sexualität= "homosexuell",
    trans= "cis",
    pronomen="er",
    stärke=10,
    geschicklichkeit=14,
    konstitution=13,
    intelligenz=18,
    weisheit=16,
    charisma=18,

    geübt=["arkane_kunde", "geschichte", "motiv_erkennen", "nachforschen", "religion", "überzeugen"] 
)

llolfaen = Spieler(
    stufe= 4,
    klasse= "druide",
    rüstungsklasse = 14,
    bewegungsrate = 9,
    allignment="Chaotisch Gut",
    volk="dunkelelfe",
    name= "Abenteurerin",
    eigenname="Llolfaen",
    gender = "divers",
    sexualität= "asexuell",
    trans= "cis",
    pronomen="xie",
    stärke=12,
    geschicklichkeit=15,
    konstitution=14,
    intelligenz=16,
    weisheit=19,
    charisma=16,

    geübt=["geschichte", "heilkunde", "mit_tieren_umgehen", "überzeugen", "wahrnehmung"] 
)

ryu = Spieler(
    stufe= 4,
    klasse= "hexenmeister",
    rüstungsklasse = 13,
    bewegungsrate = 9,
    allignment="Chaotisch Gut",
    volk="drachenblut",
    name= "Abenteurer",
    eigenname="Ryu",
    gender = "männlich",
    sexualität= "heterosexuell",
    trans= "cis",
    pronomen="er",
    stärke=16,
    geschicklichkeit=9,
    konstitution=15,
    intelligenz=10,
    weisheit=12,
    charisma=18,

    geübt=["arkane_kunde", "einschüchtern", "heilkunde", "religion"] 
)

franky = Spieler(
    stufe= 4,
    klasse= "barde",
    rüstungsklasse = 10,
    bewegungsrate = 9,
    allignment="Neutral Gut",
    volk="halbhochelf",
    name= "Abenteurer",
    eigenname="Franky",
    gender = "männlich",
    sexualität= "homosexuell",
    trans= "cis",
    pronomen="er",
    stärke=10,
    geschicklichkeit=14,
    konstitution=13,
    intelligenz=18,
    weisheit=16,
    charisma=18,

    geübt=["arkane_kunde", "geschichte", "motiv_erkennen", "nachforschen", "religion", "überzeugen"] 
)