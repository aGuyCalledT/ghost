from lib.dice import würfeln
from lib.dnd_utils import get_user_input
import random
from math import floor

class Angriff():
    def __init__(self, npc, ziel) -> None:
        self.npc = npc
        self.ziel = ziel
        self.trefferwurf = würfeln("1D20")
        

class Nahkampf(Angriff):
    def __init__(self, npc, ziel, haupt_attribut) -> None:
        super().__init__(npc, ziel)
        if haupt_attribut == "stärke":
            self.angriff_bonus = npc.stärke_mod + npc.übungsbonus
        elif haupt_attribut == "geschicklichkeit":
            self.angriff_bonus = npc.geschicklichkeit_mod + npc.übungsbonus

        print(f"{npc.name} greift {ziel.name} an und würfelt eine {self.trefferwurf + self.angriff_bonus} ({self.trefferwurf}+{self.angriff_bonus})")

        self.hit = False
        if ziel.rüstungsklasse <= (self.trefferwurf + self.angriff_bonus):
            self.hit = True


class Lanze(Nahkampf):
    def __init__(self, npc, ziel, haupt_attribut = "stärke") -> None:
        super().__init__(npc, ziel, haupt_attribut)
        if self.hit:
            self.schaden = würfeln("1D12")
            self.schadensart = "Stich"
            display_text = [
                f"{npc.name} sticht mit seiner Lanze nach {ziel.name} und verursacht {self.schaden} {self.schadensart}schaden.",
                f"{npc.name} rammt mit einer schnellen bewegung seine Lanze in {ziel.name}s Schulter und versursacht {self.schaden} {self.schadensart}schaden.",
                f"{npc.name} bohrt seinen Speer in {ziel.name}s Oberschenkel und verursacht {self.schaden} {self.schadensart}schaden."
            ]
            print(random.choice(display_text))
        else:
            display_text = [
            f"{npc.name} sticht mit seiner Lanze nach {ziel.name}, aber verfehlt ihn.",
            f"{npc.name} sticht mit seiner Lanze nach {ziel.name}, aber der Angriff gleitet an {ziel.name}s Rüstung ab."
            ]
            print(random.choice(display_text))


class Lanzenwurf(Nahkampf):
    def __init__(self, npc, ziel, haupt_attribut = "geschicklichkeit") -> None:
        super().__init__(npc, ziel, haupt_attribut)
        if self.hit:
            self.schaden = würfeln("1D12")
            self.schadensart = "Stich"
            display_text = [
            print(f"{npc.name} wirft seine Lanze nach {ziel.name} und verursacht {self.schaden} {self.schadensart}schaden."),
            print(f"{npc.name} schleudert seine Lanze auf {ziel.name} und verursacht {self.schaden} {self.schadensart}schaden.")
            ]
            print(random.choice(display_text))
        else:
            display_text = [
            print(f"{npc.name} wirft seine Lanze nach {ziel.name} und verfehlt ihn."),
            print(f"{npc.name} wirft seine Lanze nach {ziel.name}, doch sie prallt von {ziel.name}s Rüstung ab."),
            ]
            print(random.choice(display_text))

class Magie(Angriff):
    def __init__(self, npc, ziel, haupt_attribut, rettungswurf = None) -> None:
        super().__init__(npc, ziel)

        self.rettungswurf = rettungswurf

        if haupt_attribut == "intelligenz":
            self.angriff_bonus = npc.intelligenz_mod + npc.ünungsbonus
        elif haupt_attribut == "weisheit":
            self.angriff_bonus = npc.weisheit_mod + npc.ünungsbonus
        elif haupt_attribut == "charisma":
            self.angriff_bonus = npc.charisma_mod + npc.ünungsbonus
        if rettungswurf is not None:
            print(f"{npc.name} wirkt einen Flächenzauber")
            print(f"Alle Ziele legen einen Rettungswurf auf '{rettungswurf.capitalize()}' ab.")
        else:
            print(f"{npc.name} greift {ziel.name} an und würfelt eine {self.trefferwurf + self.angriff_bonus} ({self.trefferwurf}+{self.angriff_bonus})")

class Feuerball(Magie):
    def __init__(self, npc, ziel, haupt_attribut, rettungswurf = "geschicklichkeit") -> None:
        super().__init__(npc, ziel, haupt_attribut, rettungswurf)

        self.schwierigkeitsgrad = 8 + npc.zauberwirkungsbonus + npc.get_mod(haupt_attribut)
        self.schaden = würfeln("8D6")

        print(f"Alle Ziele, deren Rettungswurf fehlgeschlagen ist erhalten {self.schaden} Schaden.")
        print(f"Alle anderen erhalten {floor(self.schaden/2)} Schaden")
        
