from lib import dicts, lists

class Waffe:
    def __init__(self, name, schaden, schadensart, wurfwaffe=False, finesse=False, leicht=False, schwer=False, vielseitig=False, zweihändig=False, geschosse=False, weitreichend=False, laden=False, waffen_gend = "er"):
        self.name = name
        self.schaden = schaden
        self.schadensart = schadensart
        self.wurfwaffe = wurfwaffe
        self.finesse = finesse
        self.leicht = leicht
        self.schwer = schwer
        self.vielseitig = vielseitig
        self.zweihändig = zweihändig
        self.geschosse = geschosse
        self.weitreichend = weitreichend
        self.laden = laden
        self.waffen_gend = waffen_gend

    def __str__(self):
        return f"{self.name} ({self.schaden})"

class Speer(Waffe):
    def __init__(self):
        super().__init__(name="Speer", schaden="1D6", schadensart="stich", wurfwaffe=True, vielseitig=True, waffen_gend="er")

class Benu_Speer(Waffe):
    def __init__(self):
        super().__init__(name="Speer", schaden="1D6", schadensart="stich", wurfwaffe=True, vielseitig=True, waffen_gend="er", finesse=True)

class Beil(Waffe):
    def __init__(self):
        super().__init__(name="Beil", schaden="1D6", schadensart="hieb", wurfwaffe=True, leicht=True, waffen_gend="es")

class Streitkolben(Waffe):
    def __init__(self):
        super().__init__(name="Streitkolben", schaden="1D6", schadensart="wucht", waffen_gend="er")

class Flegel(Waffe):
    def __init__(self):
        super().__init__(name="Flegel", schaden="1D8", schadensart="wucht", waffen_gend="er")

class Morgenstern(Waffe):
    def __init__(self):
        super().__init__(name="Morgenstern", schaden="1D8", schadensart="wucht", waffen_gend="er")

class Kurzschwert(Waffe):
    def __init__(self):
        super().__init__(name="Kurzschwert", schaden="1D6", schadensart="stich", finesse=True, leicht=True, waffen_gend="es")

class Langschwert(Waffe):
    def __init__(self):
        super().__init__(name="Langschwert", schaden="1D8", schadensart="hieb", vielseitig=True, waffen_gend="es")

class Zweihänder(Waffe):
    def __init__(self):
        super().__init__(name="Zweihänder", schaden="2D6", schadensart="hieb", schwer=True, zweihändig=True, waffen_gend="er")

class Rapier(Waffe):
    def __init__(self):
        super().__init__(name="Rapier", schaden="1D8", schadensart="stich", finesse=True, waffen_gend="er")

class Krummsäbel(Waffe):
    def __init__(self):
        super().__init__(name="Krummsäbel", schaden="1D6", schadensart="hieb", finesse=True, leicht=True, waffen_gend="er")

class Dolch(Waffe):
    def __init__(self):
        super().__init__(name="Dolch", schaden="1D4", schadensart="stich", finesse=True, leicht=True, wurfwaffe=True, waffen_gend="er")

class Handarmbrust(Waffe):
    def __init__(self):
        super().__init__(name="Handarmbrust", schaden="1D6", schadensart="stich", geschosse=True, laden=True, leicht=True, waffen_gend="sie")

class Armbrust(Waffe):
    def __init__(self):
        super().__init__(name="Armbrust", schaden="1D8", schadensart="stich", geschosse=True, laden=True, zweihändig=True, waffen_gend="sie")

class Kurzbogen(Waffe):
    def __init__(self):
        super().__init__(name="Kurzbogen", schaden="1D6", schadensart="stich", geschosse=True, zweihändig=True, waffen_gend="er")

class Langbogen(Waffe):
    def __init__(self):
        super().__init__(name="Langbogen", schaden="1D8", schadensart="stich", geschosse=True, schwer=True, zweihändig=True, waffen_gend="er")

class Keule(Waffe):
    def __init__(self):
        super().__init__(name="Keule", schaden="1D6", schadensart="wucht", leicht=True, waffen_gend="sie")

class Handbeil(Waffe):
    def __init__(self):
        super().__init__(name="Handbeil", schaden="1D6", schadensart="hieb", leicht=True, wurfwaffe=True, waffen_gend="es")

class Knüppel(Waffe):
    def __init__(self):
        super().__init__(name="Knüppel", schaden="1D4", schadensart="wucht", leicht=True, waffen_gend="er")

class Hammer(Waffe):
    def __init__(self):
        super().__init__(name="Hammer", schaden="1D4", schadensart="wucht", leicht=True, wurfwaffe=True, waffen_gend="er")

class Sichel(Waffe):
    def __init__(self):
        super().__init__(name="Sichel", schaden="1D4", schadensart="hieb", leicht=True, waffen_gend="sie")

class Schleuder(Waffe):
    def __init__(self):
        super().__init__(name="Schleuder", schaden="1D4", schadensart="wucht", geschosse=True, waffen_gend="sie")

class Streitaxt(Waffe):
    def __init__(self):
        super().__init__(name="Streitaxt", schaden="1D8", schadensart="hieb", vielseitig=True, waffen_gend="sie")

class Kriegshammer(Waffe):
    def __init__(self):
        super().__init__(name="Kriegshammer", schaden="1D8", schadensart="wucht", vielseitig=True, waffen_gend="er")

class Hellebarde(Waffe):
    def __init__(self):
        super().__init__(name="Hellebarde", schaden="1D10", schadensart="hieb", schwer=True, zweihändig=True, waffen_gend="sie")

class Schild(Waffe):
    def __init__(self):
        super().__init__(name="Schild", schaden="1D4", schadensart="wucht", waffen_gend="er")

class Dreizack(Waffe):
    def __init__(self):
        super().__init__(name="Dreizack", schaden="1D6", schadensart="stich", wurfwaffe=True, vielseitig=True, waffen_gend="er")

class Kriegslanze(Waffe):
    def __init__(self):
        super().__init__(name="Kriegslanze", schaden="1D12", schadensart="stich", weitreichend=True, schwer=True, zweihändig=True, waffen_gend="sie")

class Blasrohr(Waffe):
    def __init__(self):
        super().__init__(name="Blasrohr", schaden="1", schadensart="stich", geschosse=True, laden=True, waffen_gend="es")

class Peitsche(Waffe):
    def __init__(self):
        super().__init__(name="Peitsche", schaden="1D4", schadensart="hieb", finesse=True, weitreichend=True, waffen_gend="sie")

class Netz(Waffe):
    def __init__(self):
        super().__init__(name="Netz", schaden="1D4", schadensart="hieb", wurfwaffe=True, special=True, waffen_gend="es")  # special=True für besondere Funktion im Kampf

class Lanze(Waffe):
    def __init__(self):
        super().__init__(name="Lanze", schaden="1D12", schadensart="stich", weitreichend=True, schwer=True, zweihändig=True, waffen_gend="sie")

class Netzspeer(Waffe):
    def __init__(self):
        super().__init__(name="Netzspeer", schaden="1D6", schadensart="stich", wurfwaffe=True, vielseitig=True, special=True, waffen_gend="er")  # special=True für besondere Funktion im Kampf

class Kampfstab(Waffe):
    def __init__(self):
        super().__init__(name="Kampfstab", schaden="1D8", schadensart="wucht", vielseitig=True, waffen_gend="er")

class Wurfspeer(Waffe):
    def __init__(self):
        super().__init__(name="Wurfspeer", schaden="1D6", schadensart="stich", wurfwaffe=True, waffen_gend="er")

class Zweihandknüppel(Waffe):
    def __init__(self):
        super().__init__(name="Zweihandknüppel", schaden="1D8", schadensart="wucht", zweihändig=True, waffen_gend="er")

class SchwereArmbrust(Waffe):
    def __init__(self):
        super().__init__(name="Armbrust", schaden="1D10", schadensart="stich", geschosse=True, laden=True, schwer=True, zweihändig=True, waffen_gend="sie")

class Wurfpfeil(Waffe):
    def __init__(self):
        super().__init__(name="Wurfpfeil", schaden="1D4", schadensart="stich", wurfwaffe=True, waffen_gend="er")

class Glefe(Waffe):
    def __init__(self):
        super().__init__(name="Glefe", schaden="1D10", schadensart="hieb", weitreichend=True, schwer=True, zweihändig=True, waffen_gend="sie")

class Kriegshacke(Waffe):
    def __init__(self):
        super().__init__(name="Kriegshacke", schaden="1D8", schadensart="hieb", schwer=True, zweihändig=True, waffen_gend="sie")

class Pike(Waffe):
    def __init__(self):
        super().__init__(name="Pike", schaden="1D10", schadensart="stich", schwer=True, zweihändig=True, waffen_gend="sie")

class Zweihandaxt(Waffe):
    def __init__(self):
        super().__init__(name="Zweihandaxt", schaden="1D12", schadensart="hieb", schwer=True, zweihändig=True, waffen_gend="sie")

class Zweihandhammer(Waffe):
    def __init__(self):
        super().__init__(name="Zweihandhammer", schaden="1D12", schadensart="wucht", schwer=True, zweihändig=True, waffen_gend="er")

class Zweihandschwert(Waffe):
    def __init__(self):
        super().__init__(name="Zweihandschwert", schaden="2D6", schadensart="hieb", schwer=True, zweihändig=True, waffen_gend="es")