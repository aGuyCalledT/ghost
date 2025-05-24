import attacks
import lists
import random, roll
from collections import defaultdict

class Char:
    def __init__(self,
        strength : int= 0,
        dexterity : int= 0,
        constitution : int= 0,
        intelligence : int= 0,
        wisdom : int= 0,
        charisma : int= 0,

        name = None,
        alignment = None,
        level : int= 1,
        armor_class : int= 10,
        health_points = 0,
        temp_health_points = 0,
        pronouns= None,
        species= None,
        char_class= "None",
        background= None,
        proficient : list= [],
        random_proficient : int= 0,
        tags : list= []) -> None:

        self.strength= strength
        self.constitution= constitution
        self.dexterity= dexterity
        self.charisma= charisma
        self.wisdom= wisdom
        self.intelligence= intelligence

        self.name= name
        self.alignment = alignment
        self.level= level
        self.proficiency_bonus= lists.proficiency_bonus_dict[self.level]
        self.armor_class= armor_class
        self.health_points= health_points
        self.pronouns= pronouns
        self.species= species
        self.char_class= char_class
        self.background= background
        self.proficient= proficient
        self.inventory= {}
        self.equipped_items= []
        self.tags= tags

        self.equipment = {
            "main_hand" : None,
            "off_hand" : None,
            "armor" : None
        }

        if self.species is None:
            self.species= random.choice(list(lists.species_skill_bonus_dict.keys()))

        if self.char_class == "None":
            self.char_class= random.choice(list(lists.class_skill_dict.keys()))

        if self.background is None:
            self.background= random.choice(list(lists.background_skill_dict.keys()))

        if self.alignment is None:
            self.alignment= random.choice(lists.alignment)
        
        if self.name is None:
            self.name = random.choice(lists.names)

        self.inventory = self.get_starting_items()

        attributes = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma]
        if any(attr == 0 for attr in attributes):
            self.randomize(attributes)

        self.strength_mod= lists.mod_dict[self.strength]
        self.constitution_mod= lists.mod_dict[self.constitution]
        self.dexterity_mod= lists.mod_dict[self.dexterity]
        self.charisma_mod= lists.mod_dict[self.charisma]
        self.wisdom_mod= lists.mod_dict[self.wisdom]
        self.intelligence_mod= lists.mod_dict[self.intelligence]

        self.acrobatics = 0
        self.animal_handling = 0
        self.arcana = 0
        self.athletics = 0
        self.deception = 0
        self.history = 0
        self.insight = 0
        self.intimidation = 0
        self.investigation = 0
        self.medicine = 0
        self.nature = 0
        self.perception = 0
        self.persuation = 0
        self.sleight_of_hand = 0
        self.stealth = 0
        self.survival = 0

        self.initialize_skills(proficient, random_proficient)

        self.strength_saving = 0
        self.constitution_saving = 0
        self.dexterity_saving = 0
        self.charisma_saving = 0
        self.wisdom_saving = 0
        self.intelligence_saving = 0

        saving_throws= {
            "strength_saving": self.strength_mod,
            "constitution_saving": self.constitution_mod,
            "dexterity_saving": self.dexterity_mod,
            "charisma_saving": self.charisma_mod,
            "wisdom_saving": self.wisdom_mod,
            "intelligence_saving": self.intelligence_mod
        }
        
        prof_saving_throws= lists.main_attr_dict[self.char_class]

        for saving_name, saving_value in saving_throws.items():
            setattr(self, saving_name, saving_value)
            if saving_name in prof_saving_throws:
                setattr(self, saving_name, saving_value + self.proficiency_bonus)
        
        self.equip_armor()

        if health_points == 0:
            hit_die = lists.hit_dice[self.char_class]
            self.health_points = hit_die + self.constitution_mod

            for x in range(self.level - 1):
                self.health_points += sum(roll.roll(1, hit_die)) + self.constitution_mod

        if temp_health_points == 0:
            self.temp_health_points = self.health_points
        else:
            self.temp_health_points = temp_health_points


    def initialize_skills(self, proficient= [], random_proficient= 0) -> None:
        skills = {
            "acrobatics": self.dexterity_mod,
            "animal_handling": self.wisdom_mod,
            "arcana": self.intelligence_mod,
            "athletics": self.strength_mod,
            "deception": self.charisma_mod,
            "history": self.intelligence_mod,
            "insight": self.wisdom_mod,
            "intimidation": self.charisma_mod,
            "investigation": self.intelligence_mod,
            "medicine": self.wisdom_mod,
            "nature": self.intelligence_mod,
            "perception": self.wisdom_mod,
            "performance": self.charisma_mod,
            "persuation": self.charisma_mod,
            "religion": self.intelligence_mod,
            "sleight_of_hand": self.dexterity_mod,
            "stealth": self.dexterity_mod,
            "survival": self.wisdom_mod,
        }

        if self.species is not None:
            species_skills = []
            try:
                for skill in lists.species_skill_bonus_dict[self.species]:
                    if isinstance(skill, str):
                        species_skills.append(skill)
                    elif isinstance(skill, list):
                        random_skill= roll.limited_random(skill)
                        for skill in random_skill:
                            species_skills.append(skill)
                    else:
                        raise ValueError(f"'{skill}' is not a valid skill in 'species'")
            except KeyError: pass

            for skill_prof in species_skills:
                if skill_prof in self.proficient or skill_prof == "random":
                    random_proficient += 1
                elif skill_prof not in self.proficient:
                    self.proficient.append(skill_prof)

        if self.char_class is not None:
            class_input = lists.class_skill_dict[self.char_class]
            class_skills= roll.limited_random(class_input[0], class_input[1])
            for skill_prof in class_skills:
                if skill_prof in self.proficient or skill_prof == "random":
                    random_proficient += 1
                elif skill_prof not in self.proficient:
                    self.proficient.append(skill_prof)

        if self.background is not None:
            for skill_prof in lists.background_skill_dict[self.background]:
                if skill_prof in self.proficient or skill_prof == "random":
                    random_proficient += 1
                elif skill_prof not in self.proficient:
                    self.proficient.append(skill_prof)

        if random_proficient > 0:
            temp_skill_list = [x for x in list(skills.keys()) if x not in self.proficient]
            for x in range(random_proficient):
                if temp_skill_list == []: break
                random_skill= random.choice(temp_skill_list)
                temp_skill_list.remove(random_skill)
                self.proficient.append(random_skill)

        for skill_name, skill_value in skills.items():
            setattr(self, skill_name, skill_value)
            if skill_name in proficient:
                setattr(self, skill_name, skill_value + self.proficiency_bonus)

    def equip_armor(self) -> None:
        # ARMOR
        armors = []
        possible_armors = []
        unusable = False
        if self.inventory:
            for key in lists.armor_data.keys():
                if key in self.inventory.keys():
                    armors.append(key)


        for armor in armors:
            if lists.armor_data[armor]["strength_requirement"] <= self.strength:
                ac = lists.armor_data[armor]["ac"]
                if isinstance(ac, int):
                    self.armor_class = ac
                elif isinstance(ac, list):
                    temp_armor_class = ac[0]
                    temp_armor_class += self.dexterity_mod

                    if len(ac) > 2:
                        if ac[2] < temp_armor_class:
                            temp_armor_class = ac[2]
                    possible_armors.append([armor, temp_armor_class])
            else: unusable = True
            
        if armors == [] or unusable:
            self.armor_class = 10 + self.dexterity_mod

        else:
            best_armor = max(possible_armors, key=lambda x: x[1])
            self.armor_class = best_armor[1]
            self.equipped_items.append(best_armor[0])

        # WEAPONS
        weapons = []
        best_weapon = lists.get_weapon("unarmed")
        best_weapon_name = "unarmed"

        for item in self.inventory:
            if item in lists.all_weapons:
                weapons.append(item)
        
        for weapon in weapons:
            if lists.get_weapon(weapon)["damage"] > best_weapon["damage"]:
                best_weapon = lists.get_weapon(weapon)
                best_weapon_name = weapon

        self.equipped_items.append(best_weapon_name)
        


    def randomize(self, attributes) -> None:
        if self.char_class is not None:
            main_attributes = lists.main_attr_dict[self.char_class]
            random_attributes = roll.roll_attributes(main_attributes)
            for x in range(6):
                if attributes[x] == 0:
                    attributes[x] = random_attributes[x]

        self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma = attributes

        if self.species in lists.species_attr_bonus_dict.keys() and self.species is not None:
            species_attr = lists.species_attr_bonus_dict[self.species]

            self.strength += species_attr[0]
            self.dexterity += species_attr[1]
            self.constitution += species_attr[2]
            self.intelligence += species_attr[3]
            self.wisdom += species_attr[4]
            self.charisma += species_attr[5]

    def get_starting_items(self):
        inventory = roll.add_starting_gear(self.inventory, lists.starting_items[self.char_class])
        return inventory

    def equip(self, item : str, unequip = True):
        item_type = None
        if item in lists.all_weapons: item_type = "weapon"
        if item in lists.armor_data.keys(): item_type = "armor"
        if item == "shield": item_type = "shield"

        if item_type == "weapon":
            two_handed = False
            if self.equipment["main_hand"] != None:
                if not unequip:
                    return None
                if "two-handed" in lists.get_weapon(item)["properties"]:
                    two_handed = True

            if not unequip:
                if self.equipment["off_hand"] not in [False, None]: return None
            self.equipment["main_hand"] = item

            if two_handed:
                self.equipment["off_hand"] = False

        elif item_type == "armor":
            if not unequip:
                if self.equipment["armor"] != None:
                    return None
            self.equipment["armor"] = item

        elif item_type == "shield":
            if not unequip:
                if self.equipment["off_hand"] != None:
                    return None
            self.equipment["off_hand"] = item

    def display(self, item = "char"):
        end = '\033[0m'
        underline = '\033[4m'

        if item == "char":
            middle_line= f" │ '{self.name}' - {self.species} - {self.char_class} {self.level} - {self.background} │"
            width = len(middle_line)
            print(f" ┌{"─"*(width-3)}┐")
            print(middle_line)
            print(f" └{"─"*(width-3)}┘")

        elif item == "stats":
            print (" ┌───┬───┬───┬───┬───┬───┬──────────┐")
            print(f" │{underline}STR{end}│{underline}DEX{end}│{underline}CON{end}│{underline}INT{end}│{underline}WIS{end}│{underline}CHA{end}│          │")
            print(f" │{lists.mod_dict[self.strength]:+3d}│{lists.mod_dict[self.dexterity]:+3d}│{lists.mod_dict[self.constitution]:+3d}│{lists.mod_dict[self.intelligence]:+3d}│{lists.mod_dict[self.wisdom]:+3d}│{lists.mod_dict[self.charisma]:+3d}│ HP: {self.health_points:3d}  │")
            print(f" │{self.strength:3d}│{self.dexterity:3d}│{self.constitution:3d}│{self.intelligence:3d}│{self.wisdom:3d}│{self.charisma:3d}│ AC:  {self.armor_class}  │")
            print (" └───┴───┴───┴───┴───┴───┴──────────┘") 
        
        elif item == "skills":
            print(" ┌──┬─────────────────┐") 
            for skill_name in lists.skill_names:
                if skill_name in self.proficient:
                    marker = "x"
                else:
                    marker = " "
                skill_value = getattr(self, skill_name, 0) # 0 falls das Attribut nicht existiert
                margin = 16 - len(skill_name)
                skill_name = skill_name.replace("_", " ")
                print(f"{marker}│{skill_value:+}│ {skill_name}{margin*" "}│")
            print(" └──┴─────────────────┘")
        
        elif item == "inventory":
            inventory_list = []
            max_width = 0

            if self.inventory:
                for key in self.inventory.keys():
                    item_line = [self.inventory[key], key]
                    inventory_list.append(item_line)
                    current_width = len(item_line[1])
                    if max_width < current_width: max_width = current_width
            
            print(f" ┌─{"─"*(max_width + 5)}─┐")
            for line in inventory_list:
                print(f" │ {line[0]:3d}x {line[1]}{" " * (max_width - len(line[1]))} │")
            print(f" └─{"─"*(max_width + 5)}─┘")

        else:
            print(f"ERROR: Cannot display '{item}'")


# │ ─ └ ┘ ┌ ┐ ├ ┤ ┬ ┴ ┼ 
# MAIN CODE

random_guy = Char()
random_other_guy = Char()

random_guy.display("inventory")
random_other_guy.display("inventory")

attacks.weapon_attack(random_guy, random_other_guy, None)