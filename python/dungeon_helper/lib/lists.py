zauberklassen = ["barde", "kleriker", "druide", "hexenmeister", "magier", "paladin", "waldläufer", "zauberer", "artifizient"]

klassen = zauberklassen + ["barbar", "kämpfer", "mönch", "schurke", "keine klasse"]

fertigkeiten = ['akrobatik', 'arkane_kunde', 'athletik', 'auftreten', 'einschüchtern', 'fingerfertigkeit', 'geschichte', 'heilkunde', 'heimlichkeit', 'mit_tieren_umgehen', 'motiv_erkennen', 'nachforschungen', 'naturkunde', 'religion', 'täuschen', 'überlebenskunst', 'überzeugen', 'wahrnehmung']

status_effekt = ["blind", "bezaubert", "taub", "verängstigt", "gepackt", "kampfunfähig", "unsichtbar", "gelähmt", "versteinert", "vergiftet", "liegend", "festgesetzt", "betäubt", "bewusstlos", "tot"]

elf_präfix = [
    "hoch",
    "wald",
    "dunkel"
]

halbling_präfix = [
    "leichtfuß ",
    "stämmiger "
]

mensch_präfix = [
    "calishiter ",
    "chondathaner ",
    "damaraner ",
    "illuskaner ",
    "mulaner ",
    "rashemier ",
    "shouer ",
    "tethyrianer ",
    "turamier "
]

zwerg_präfix = [
    "hügel",
    "gebirgs",
    "dunkel"
]

drachenblütiger_präfix = [
    "schwarzer ",
    "blauer ",
    "messinger ",
    "bronzener ",
    "kupferner ",
    "goldener ",
    "grüner ",
    "roter ",
    "silberner ",
    "weißer "
]

gnom_präfix = [
    "fels",
    "wald",
]

andere_völker = [
    "Halbork",
    "Tiefling"
]

volk_chance = [
    ["elf" , 19],
    ["halbling", 2],
    ["mensch", 64],
    ["zwerg", 10],
    ["drachenblütiger", 0.5],
    ["gnom", 2],
    ["halbork", 1],
    ["tiefling", 1.5]
]

gender_chance = [
    ["männlich", 48],
    ["weiblich", 48],
    ["divers", 4]
]

trans_chance = [
    ["cis", 94],
    ["trans", 6],
]

sexualität_chance = [
    ["heterosexuell", 73],
    ["homosexuell", 10],
    ["pansexuell", 15],
    ["asexuell", 2]
]

allignment_lawfulness = [
    ["Rechtschaffend", 30],
    ["Neutral", 50],
    ["Chaotisch", 20]
]

allignment_goodness = [
    ["Gut", 30],
    ["Neutral", 50],
    ["Böse", 20]
]

pronomen = [
    ["er", 15],
    ["sie", 15],
    ["es", 20],
    ["they", 30],
    ["xer", 10],
    ["xie", 10],

]

größe = [
    "winzig",
    "klein",
    "normal",
    "groß",
    "riesig",
    "gewaltig"
]

elf_silben = [
    "a", "ae", "aer", "ah", "ai", "al", "ala", "an", "ana", "ar", "ara", 
    "as", "atha", "au", "e", "ea", "el", "ela", "en", "ena", "er", "era", 
    "es", "eth", "ev", "eya", "fa", "fae", "fal", "far", "fe", "fi", "fin", 
    "fir", "ga", "gae", "gal", "gar", "ge", "gil", "gla", "ha", "hae", "hal", 
    "har", "he", "hi", "ia", "iel", "il", "ila", "in", "ina", "ir", "ira", 
    "is", "ith", "iv", "iya", "ka", "kae", "kal", "kar", "ke", "ki", "la", 
    "lae", "lan", "lar", "le", "li", "lin", "lir", "lo", "lor", "lu", "lya", 
    "ma", "mae", "mal", "mar", "me", "mi", "min", "mir", "na", "nae", "nal", 
    "nar", "ne", "ni", "nin", "nir", "no", "nor", "nu", "nya", "o", "or", 
    "ra", "rae", "ral", "ran", "re", "ri", "rin", "ro", "ror", "ru", "rya", 
    "sa", "sae", "sal", "sar", "se", "si", "sil", "ta", "tae", "tal", "tar", 
    "te", "tha", "thi", "ti", "va", "vae", "val", "var", "ve", "vi", "vin", 
    "ya", "yel", "yra", "ys"
]

goblin_silben = [
    "ag", "ak", "arg", "ark", "az", "bag", "bak", "barg", "bark", "baz", 
    "blag", "brak", "brag", "brark", "bug", "buk", "burg", "burk", "buz", 
    "dag", "dak", "darg", "dark", "daz", "drag", "drak", "dreg", "dre", 
    "dro", "dug", "duk", "dur", "durk", "fag", "fak", "farg", "fark", 
    "faz", "frag", "frak", "freg", "frek", "frog", "fruk", "gag", "gak", 
    "garg", "gark", "gaz", "grag", "grak", "greg", "grek", "grog", "grok", 
    "grub", "guk", "gur", "gurk", "hag", "hak", "harg", "hark", "haz", 
    "hrag", "hrak", "hreg", "hrek", "hrug", "huk", "hur", "hurk", "jag", 
    "jak", "jarg", "jark", "jaz", "krag", "krak", "kreg", "krek", "krog", 
    "krok", "kug", "kuk", "kur", "kurk", "lag", "lak", "larg", "lark", 
    "laz", "mag", "mak", "marg", "mark", "maz", "nag", "nak", "narg", 
    "nark", "naz", "og", "ok", "org", "ork", "oz", "rag", "rak", "rarg", 
    "rark", "raz", "reg", "rek", "rog", "rok", "rug", "ruk", "sag", "sak", 
    "sarg", "sark", "ska", "sna", "snik", "snu", "snuk", "stag", "stak", 
    "streg", "strek", "surg", "surk", "tag", "tak", "targ", "tark", "taz", 
    "trag", "trak", "treg", "trek", "tro", "trok", "tug", "tuk", "tur", "urk",
    "zag", "zak", "zarg", "zark", "zog", "zok", "zug", "zuk", "zur", "zurk"
]

benu_silben = [
    "a", "ac", "ah", "al", "an", "atl", "ax", "ay", "ca", "cal", "can", "catl", "caz", "ce", "cel", "cen", "cetl",
    "cha", "chal", "chan", "chatl", "che", "chel", "chen", "chetl", "chi", "chil", "chin", "chitl", "ci", "cil", "cin",
    "citl", "co", "coy", "cu", "cua", "cue", "cui", "e", "ec", "eh", "el", "en", "etl", "ex", "ey", "ha", "hal",
    "han", "hatl", "he", "hel", "hen", "hetl", "hi", "hil", "hin", "hitl", "hu", "hua", "hue", "hui", "i", "ic",
    "ih", "il", "in", "itl", "ix", "iy", "ja", "jal", "jan", "jatl", "je", "jel", "jen", "jetl", "ji", "jil", "jin",
    "jitl", "ju", "jua", "jue", "jui", "la", "lal", "lan", "latl", "le", "lel", "len", "letl", "li", "lil", "lin",
    "litl", "lo", "loy", "lu", "lua", "lue", "lui", "na", "nal", "nan", "natl", "ne", "nel", "nen", "netl", "ni",
    "nil", "nin", "nitl", "no", "noy", "nu", "nua", "nue", "nui", "qua", "que", "qui", "sa", "sal", "san", "satl",
    "se", "sel", "sen", "setl", "si", "sil", "sin", "sitl", "so", "soy", "su", "sua", "sue", "sui", "ta", "tal",
    "tan", "tatl", "te", "tel", "ten", "tetl", "ti", "til", "tin", "titl", "to", "toy", "tu", "tua", "tue", "tui",
    "tza", "tze", "tzi", "xa", "xal", "xan", "xatl", "xe", "xel", "xen", "xetl", "xi", "xil", "xin", "xitl", "xo",
    "xoy", "xu", "xua", "xue", "xui", "ya", "yal", "yan", "yatl", "ye", "yel", "yen", "yetl", "yi", "yil", "yin",
    "yitl", "yo", "yoy", "yu", "yua", "yue", "yui", "za", "zal", "zan", "zatl", "ze", "zel", "zen", "zetl", "zi",
    "zil", "zin", "zitl", "zo", "zoy", "zu", "zua", "zue", "zui"
]

halbling_silben = [
    "ad", "al", "an", "ar", "bar", "ben", "ber", "brad", "bri", "ca", 
    "char", "chris", "clar", "clif", "da", "dan", "der", "ed", "el", "eli", 
    "em", "er", "fre", "ga", "geo", "gil", "gra", "gre", "ham", "har", 
    "hen", "hugh", "ian", "jack", "jam", "jas", "je", "jer", "jo", "john", 
    "jon", "jos", "ke", "ken", "kit", "lau", "leo", "li", "lou", "lu", 
    "mar", "mat", "mi", "ni", "no", "ol", "os", "ow", "pe", "per", 
    "phil", "re", "ri", "ro", "ru", "sam", "si", "stan", "ste", "te", 
    "thom", "ti", "tim", "to", "wa", "wal", "wil", "a", "ard", "bert", 
    "by", "don", "dy", "er", "ford", "frey", "ham", "ie", "is", "ley", 
    "ly", "ma", "mond", "na", "nel", "ney", "on", "ry", "son", "ter", 
    "ton", "ty", "ver", "ward", "well", "win"
]

zwerg_silben = [
    "ad", "al", "an", "ar", "bal", "bar", "bel", "ben", "ber", "bil",
    "bor", "bram", "bran", "bron", "dar", "del", "din", "dor", "dral", "dran",
    "drom", "eb", "el", "er", "far", "fen", "fin", "flint", "for", "fram",
    "fran", "gar", "gim", "glan", "glor", "gor", "grim", "grom", "grun", "hild",
    "holm", "ing", "jarl", "kad", "kar", "keld", "kil", "kor", "lind", "lor",
    "lund", "mal", "mord", "mor", "nal", "nar", "nor", "nur", "od", "og",
    "ol", "olf", "or", "ork", "os", "otr", "rag", "rak", "ran", "reg",
    "rik", "rim", "rolf", "ron", "rund", "skar", "snor", "stein", "stor", "svar",
    "tal", "tar", "thad", "thal", "than", "thar", "thor", "thran", "thror", "thur",
    "tor", "trak", "trom", "ulf", "ung", "val", "var", "vek", "vil", "yorn"
]

tiefling_silben = [
    "ab", "ad", "al", "am", "an", "ar", "as", "ash", "ath", "az",
    "ba", "bal", "bar", "bel", "bez", "buz", "da", "dal", "dar", "del",
    "dem", "dez", "di", "dis", "do", "dom", "dra", "dul", "e", "el",
    "em", "er", "esh", "ez", "fa", "faz", "fi", "fo", "fur", "ga",
    "gal", "gar", "goth", "gul", "ha", "im", "in", "ir", "is", "ith",
    "iz", "ka", "kaz", "ki", "ko", "kor", "kuth", "la", "lak", "lam",
    "laz", "le", "les", "li", "lith", "lo", "lor", "luz", "ma", "mal",
    "mar", "maz", "me", "mel", "mes", "mi", "mo", "mol", "mor", "moth",
    "muz", "na", "nal", "nar", "nash", "naz", "ne", "ni", "nil", "noth",
    "nu", "or", "os", "oth", "ra", "rak", "ras", "raz", "ri", "roth",
    "sa", "sal", "sar", "sha", "shal", "tan", "tar", "th", "ul", "um",
    "ur", "uz", "va", "val", "var", "vek", "ver", "vil", "x", "xan",
    "zar", "ze", "zel", "zes", "zu"
]

römische_silben_anfang = [
    "aemili", "agripp", "antoni", "ap", "aur", "aul", "caecili", "calpurni", 
    "claudi", "corn", "deci", "domiti", "fab", "flavi", "fulvi", "gai", "gn", 
    "horati", "iul", "iuni", "livi", "luci", "lucreti", "manli", "marc", 
    "mari", "ner", "numeri", "octavi", "pomp", "popp", "properti", "publi", 
    "quinctili", "quinti", "salusti", "semproni", "serv", "sexti", "sul",
    "tertulli", "tiberi", "titi", "vali", "vet", "vipsani",
    "alexand", "ambr", "anni", "aquilli", "atri", "caes", "camill", "cassi",
    "cat", "cicer", "cinn", "clodi", "coeli", "cornel", "cost", "crass",
    "curi", "did", "dio", "drus", "duili", "egnati", "enni", "fabi", "falc",
    "fann", "furi", "gall", "gelli", "gracch", "helvi", "herenni", "hostili",
    "laeli", "laet", "lentul", "licini", "livi", "maec", "magi", "malli",
    "mamm", "marcell", "max", "messal", "min", "munati", "naevi", "nas",
    "nepoti", "nig", "non", "oppi", "ovali", "paet", "pal", "ped", "petroni",
    "pison", "plaut", "pler", "ploti", "polli", "postum", "rabiri", "rufi",
    "sab", "sallusti", "sc", "scaev", "scaur", "scriboni", "scur", "septim",
    "serg", "sertori", "sesti", "sil", "spuri", "stati", " Statili", "suetoni",
    "tacit", "terenti", "treboni", "tul", "turpil", "ull", "valeri", "varr",
    "vatini", "vel", "verg", "vespasi", "vinici", "voli", "volusi"
]

römische_silben_ende_männlich = [
    "us", "o", "anus", "ianus", "inus", "ius", "er", "es"
]

römische_silben_ende_weiblich = [
    "a", "ia", "ina", "ana", "ella", "illa"
]

deutsche_silben_anfang = [
    "adal", "alb", "arn", "bald", "bernh", "brun", "carl", "conr", "diet", "eber",
    "erich", "fried", "ger", "gottf", "gunth", "hans", "hein", "helm", "herm", "hild",
    "hug", "ing", "joh", "karl", "konr", "lud", "luise", "marg", "mart", "matth",
    "max", "mich", "ott", "paul", "pet", "rud", "sieg", "soph", "the", "thom",
    "ulf", "walt", "wilh", "wolf", "adalb", "agnes", "albr", "alexand", "amali",
    "annel", "august", "barbar", "beatr", "bened", "bridg", "casp", "christ", "christoph",
    "clara", "dor", "eb", "ed", "el", "elisab", "em", "er", "ern", "franz",
    "friedr", "georg", "gerh", "gertr", "gott", "greg", "gudr", "gust", "han", "hed",
    "heinr", "henr", "her", "hub", "jak", "johann", "josef", "j", "kath", "klaus",
    "konst", "leo", "leon", "lorenz", "ludw", "magd", "mann", "mar", "mar", "nik",
    "ol", "osw", "otto", "phil", "rach", "rein", "rob", "siegfr", "seb", "sim",
    "sus", "ther", "urs", "vict", "walt", "wen", "wolfg"
]

deutsche_silben_ende_männlich = [
    "o", "fried", "olf", "hart", "bert", "brecht", "mar", "win", "helm", "mut",
    "ram", "bold", "ger", "ther", "bald", "mund", "friedrich", "erich", "lothar", "bernd",
    "horst", "peter", "heinz", "jürgen", "werner", "helmut", "hans", "dieter", "klaus", "günther",
    "manfred", "herbert", "rolf", "gerhard", "karl", "heinrich", "walter", "wilhelm", "kurt", "horst"
]

deutsche_silben_ende_weiblich = [
    "a", "e", "i", "hild", "gard", "lind", "trud", "burg", "gund", "berta",
    "marie", "anne", "liese", "lore", "thea", "rike", "chen", "lein", "traud", "gitte",
    "ela", "linde", "hildis", "wig", "run", "hildgard", "mariechen", "annelene", "elisabeth", "emma"
]

japanische_silben = [
    "kon", "ni", "chi", "wa", "fu", "ru", "mi", "yu", "ki", "ra",
    "so", "ha", "ku", "ma", "ta", "ka", "na", "su", "ko", "mo",
    "ri", "shi", "do", "yo", "mei", "lin", "chen", "wong", "lee", "kim",
    "chan", "nguyen", "singh", "khan", "rao", "patel", "yamada", "tanaka", "sato", "suzuki",
    "feng", "hua", "ming", "xiao", "yang", "zhou", "li", "wang", "zhang", "liu",
    "kimura", "nakamura", "watanabe", "ito", "kato", "park", "choi", "jung", "bae", "ahn",
    "jaya", "rama", "sita", "krishna", "indra", "vishnu", "shiva", "ganesh", "lakshmi", "saraswati",
    "bao", "dai", "gao", "jiang", "mao", "peng", "qin", "sun", "tang", "wen",
    "thai", "lao", "viet", "khmer", "burmese", "filipino", "indonesian", "malaysian", "singaporean", "bruneian",
    "sakura", "fuji", "kiku", "momo", "ume", "take", "matsu", "yuki", "umi", "sora"
]

afrikanische_silben = [
    "ba", "ntu", "ki", "swa", "zu", "lu", "mbo", "nga", "yo", "ru",
    "ma", "sha", "ka", "ndi", "so", "tho", "xa", "kho", "sa", "an",
    "zi", "m", "fu", "la", "wo", "lo", "fe", "be", "da", "ga",
    "nya", "se", "so", "to", "ko", "mo", "no", "bo", "ro", "go",
    "u", "bu", "ku", "mu", "nu", "gu", "du", "su", "tu", "vu",
    "a", "e", "i", "o", "ha", "he", "hi", "ho", "hu",
    "mba", "ndo", "ngo", "nya", "nza", "sha", "shi", "sho", "shu",
    "kwa", "kwe", "kwi", "kwo", "kwu", "gwa", "gwe", "gwi", "gwo", "gwu",
    "tsa", "tse", "tsi", "tso", "tsu", "dza", "dze", "dzi", "dzo", "dzu",
    "nwa", "nwe", "nwi", "nwo", "nwu"
]

skandinavische_silben = [
    "björn", "sven", "ing", "borg", "holm", "skog", "fjord", "vik", "berg", "dal",
    "ä", "ö", "ä", "ö", "lj", "sj", "sk", "st", "tr", "dr",
    "kn", "gn", "rn", "fn", "vr", "sv", "hv", "kv", "tv", "dv",
    "sol", "vind", "hav", "skog", "fjell", "elv", "snö", "is", "ild", "vann",
    "himmel", "jord", "lys", "mörke", "dag", "natt", "stern", "möhne", "regen", "torden",
    "kjärlighet", "vennskap", "familie", "hjem", "hygge", "ro", "fred", "glede", "sorg", "lengsel",
    "norr", "sör", "öst", "vest", "nord", "syd", "midt", "land", "öy", "hav",
    "gammel", "ny", "stor", "liten", "höy", "lav", "lang", "kurz", "breit", "schmal",
    "vakker", "stark", "modig", "vis", "gut", "ond", "hell", "dunkel", "warm", "kalt",
    "ulf", "björn", "rev", "elg", "örn", "fisch", "tre", "stein", "blum", "blatt"
]

poly_tabellarisch = [
    "calishiter", "chondathaner", "damaraner", "tethyrianer", "halbork"
]

verwendete_namen = []

waffenlos_flavor_text = [
    [ # crit_hit
        "{0} stürzt sich auf {1} und sticht mit {2} {3} zu. {0} verursacht {4} {5}schaden.",
        "Wütend packt {0} {2} {3} fester und greift damit {1} an. {0} verursacht {4} {5}schaden."
    ],
    [ # hit
        "{0} schlägt {1} mit {2} {3} und verursacht {4} {5}schaden",
        "{0} schlägt {1} mit {2} {3} und verursacht {4} {5}schaden"
    ],
    [ # crit_miss
        "{0} stellt sich bei {2} Angriff gegen {1} so ungeschickt an, dass {0} sich selbst verletzt und {4} {5}schaden verursacht",
        "{0} versucht {1} zu treffen, doch trifft stattdessen {2} eigenen Körper und verursacht bei sich selbst {4} {5}schaden"
        
    ],
    [ # miss
        "{0} versucht {1} mit {2} {3} zu schlagen, haut aber voll daneben",
        "{0} schlägt nach {1} mit {2} {3}, aber trifft nicht"
    ]
]