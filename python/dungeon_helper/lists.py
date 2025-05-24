species_attr_bonus_dict = {# S  D  C  I  W  C
    "hill_dwarf":           [0, 0, 2, 0, 1, 0], 
    "mountain_dwarf":       [2, 0, 2, 0, 0, 0],
    "high_elf":             [0, 2, 0, 1, 0, 0],
    "wood_elf":             [0, 2, 0, 0, 1, 0],
    "drow_elf":             [0, 2, 0, 0, 0, 1],
    "lightfoot_halfling":   [0, 2, 0, 0, 0, 1],
    "stout_halfling":       [0, 2, 1, 0, 0, 0],
    "human":                [1, 1, 1, 1, 1, 1],
    "dragonborn":           [2, 0, 0, 0, 0, 1],
    "forest_gnome":         [0, 1, 0, 2, 0, 0],
    "rock_gnome":           [0, 0, 1, 2, 0, 0],
    "half_elf":             [0, 0, 0, 0, 0, 2],
    "half_orc":             [2, 0, 1, 0, 0, 0],
    "tiefling":             [0, 0, 0, 1, 0, 2],
    "aasimar":              [0, 0, 0, 0, 1, 2],
    "eladrin_elf":          [0, 2, 0, 1, 0, 0],
    "aarakocra":            [0, 2, 0, 0, 1, 0],
    "deep_gnome":           [0, 1, 0, 2, 0, 0],
    "air_genasi":           [1, 2, 0, 0, 0, 0],
    "earth_genasi":         [1, 0, 2, 0, 0, 0],
    "fire_genasi":          [0, 0, 2, 0, 1, 0],
    "water_genasi":         [0, 0, 2, 0, 0, 1],
    "goliath":              [2, 0, 1, 0, 0, 0],
    "duergar_dwarf":        [1, 0, 2, 0, 0, 0],
    "ghostwise_halfling":   [0, 2, 0, 0, 1, 0],
    "svirfneblin_gnome":    [0, 1, 0, 2, 0, 0],
    "feral_tiefling":       [2, 0, 1, 0, 0, 0],
    "protector_aasimar":    [0, 0, 0, 0, 1, 2],
    "scourge_aasimar":      [0, 1, 0, 0, 0, 2],
    "fallen_aasimar":       [1, 0, 0, 0, 0, 2],
    "firbolg":              [0, 1, 0, 0, 2, 0],
    "kenku":                [0, 2, 0, 0, 1, 0],
    "lizardfolk":           [0, 0, 2, 0, 1, 0],
    "tabaxi":               [0, 2, 0, 0, 0, 1],
    "triton":               [1, 1, 0, 0, 1, 0],
    "bugbear":              [2, 1, 0, 0, 0, 0],
    "goblin":               [0, 2, 1, 0, 0, 0],
    "hobgoblin":            [0, 0, 2, 1, 0, 0],
    "kobold":               [0, 2, 0, 0, 0, 0],
    "orc":                  [2, 0, 1, 0, 0, 0],
    "yuan_ti_pureblood":    [0, 0, 0, 1, 0, 2],
    "sea_elf":              [2, 1, 0, 0, 0, 0],
    "shadar_kai_elf":       [2, 1, 0, 0, 0, 0],
    "githyanki":            [2, 0, 0, 0, 1, 0],
    "githzerai":            [0, 0, 0, 1, 2, 0],
    "tortle":               [0, 0, 2, 0, 1, 0],
    "verdan":               [0, 1, 0, 0, 0, 2],
    "changeling":           [0, 0, 0, 0, 0, 0],
    "kalashtar":            [0, 0, 0, 0, 2, 1],
    "beasthide_shifter":    [1, 0, 2, 0, 0, 0],
    "longtooth_shifter":    [2, 1, 0, 0, 0, 0],
    "swiftstride_shifter":  [0, 2, 0, 0, 0, 1],
    "wildhunt_shifter":     [1, 0, 0, 0, 2, 0],
    "warforged":            [0, 0, 2, 0, 0, 0], 
    "centaur":              [2, 0, 0, 0, 1, 0],
    "loxodon":              [0, 0, 2, 0, 1, 0],
    "minotaur":             [2, 0, 1, 0, 0, 0],
    "simic_hybrid":         [0, 0, 2, 0, 0, 0],
    "vedalken":             [0, 0, 0, 2, 1, 0],
    "leonin":               [1, 0, 2, 0, 0, 0],
    "satyr":                [0, 1, 0, 0, 0, 2]
}

species__random_attr_bonus_dict = {
    "half_elf" : 2,
    "warforged": 1,
    "simic_hybrid": 1
}

species_skill_bonus_dict = {
    "high_elf":             ["perception"],
    "wood_elf":             ["perception"],
    "drow_elf":             ["perception"],
    "eladrin_elf":          ["perception"],
    "sea_elf" :             ["perception"],
    "shadar_kai_elf":       ["perception"],
    "human" :               ["random"],
    "half_elf":             ["random", "random"],
    "half_orc":             ["intimidation"],
    "changeling":           ["random", ["deception", "intimidation", "insight", "persuasion"]],
    "beasthide_shifter":    ["perception"],
    "longtooth_shifter":    ["perception"],
    "swiftstride_shifter":  ["perception"],
    "wildhunt_shifter":     ["perception"],
    "goliath" :             ["athletics"],
    "bugbear" :             ["stealth"],
    "lizardfolk" :          [["animal_handling", "nature", "perception", "stealth", "survival"], ["animal_handling", "nature", "perception", "stealth", "survival"]],
    "orc" :                 ["intimidation"],
    "tabaxi" :              ["perception", "stealth"],
    "centaur":              [["animal_handling", "medicine", "nature", "survival"]],
    "leonin" :              [["athletics", "intimidation", "perception", "survival"]],
    "minotaur":             ["intimidation"],
    "satyr" :               ["performance", "persuation"]


}



attr_index_dict= {
    "str" : 0,
    "dex" : 1,
    "con" : 2,
    "int" : 3,
    "wis" : 4,
    "cha" : 5}

proficiency_bonus_dict= {
    1 : 2, 2 : 2, 3 : 2, 4 : 2, 5 : 3,
    6 : 3, 7 : 3, 8 : 3, 9 : 4, 10: 4,
    11: 4, 12: 4, 13: 5, 14: 5, 15: 5,
    16: 5, 17: 6, 18: 6, 19: 6, 20: 6}

skills_index_dict= {
    "acrobatics" : 0,
    "animal_handling" : 1,
    "arcana" : 2,
    "athletics" : 3,
    "deception" : 4,
    "history" : 5,
    "insight" : 6,
    "intimidation" : 7,
    "investigation" : 8,
    "medicine" : 9,
    "nature" : 10,
    "perception" : 11,
    "performance" : 12,
    "persuation" : 13,
    "religion" : 14,
    "sleight_of_hand" : 15,
    "stealth" : 16,
    "survival" : 17,}

mod_dict = {
    0:-5,
    1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 
    11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5, 
    21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10}

dice_sides = [1, 4, 6, 8, 10, 12, 20, 100]

main_attr_dict= {
    "barbarian" : ["str", "con"], "bard" : ["cha", "dex"], "cleric" : ["cha", "wis"], "druid" : ["int", "wis"], 
    "fighter" : ["str", "con"], "monk" : ["str", "dex"], "paladin" : ["cha", "wis"], "ranger" : ["dex", "str"], 
    "rogue" : ["dex", "int"], "sorcerer" : ["cha", "con"], "warlock" : ["cha", "wis"], "wizard" : ["int", "wis"], 
    "artificer" : ["int", "con"]}

class_skill_dict= {
    "barbarian" : [["animal_handling", "athletics", "intimidation", "nature", "perception", "survival"], 2], 
    "bard" : [["acrobatics", "animal_handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuation", "religion", "sleight_of_hand", "stealth", "survival"], 3], 
    "cleric" : [["history", "insight", "medicine", "persuasion", "religion"], 2], 
    "druid" : [["arcana", "animal_handling", "insight", "medicine", "nature", "perception", "religion", "survival"], 2], 
    "fighter" : [["acrobatics", "animal_handling", "athletics", "history", "insight", "intimidation", "perception", "survival"], 2], 
    "monk" : [["acrobatics", "athletics", "history", "insight", "religion", "stealth"], 2], 
    "paladin" : [["athletics", "insight", "intimidation", "medicine", "persuasion", "religion"], 2], 
    "ranger" : [["animal_handling", "athletics", "insight", "investigation", "nature", "perception", "stealth", "survival"], 3], 
    "rogue" : [["acrobatics", "athletics", "deception", "insight", "intimidation", "investigation", "perception", "performance", "persuasion", "sleight_of_hand", "stealth"], 4], 
    "sorcerer" : [["arcana", "deception", "insight", "intimidation", "persuasion", "religion"], 2], 
    "warlock" : [["arcana", "deception", "history", "intimidation", "investigation", "nature", "religion"], 2], 
    "wizard" : [["arcana", "history", "insight", "investigation", "medicine", "religion"], 2], 
    "artificer" : [["arcana", "history", "investigation", "medicine", "nature", "perception", "sleight_of_hand"], 2]}

skill_names = [
            "acrobatics", "animal_handling", "arcana", "athletics",
            "deception", "history", "insight", "intimidation",
            "investigation", "medicine", "nature", "perception",
            "performance", "persuation", "religion", "sleight_of_hand",
            "stealth", "survival"
        ]

background_skill_dict = {
    "acolyte": ["insight", "religion"],
    "anthropologist": ["insight", "religion"],
    "archaeologist": ["history", "survival"],
    "artisan": ["investigation", "persuasion"],
    "astral_drifter": ["insight", "religion"],
    "athlete": ["athletics", "acrobatics"],
    "azorius_functionary": ["insight", "intimidation"],
    "boros_legionnaire": ["athletics", "intimidation"],
    "celebrity_adventurer’s_scion": ["perception", "performance"],
    "charlatan": ["deception", "sleight_of_hand"],
    "city_watch": ["athletics", "investigation", "insight"],
    "clan_crafter": ["history", "insight"],
    "cloistered scholar": ["history", "arcana", "nature", "religion"],
    "courtier": ["insight", "persuasion"],
    "criminal": ["stealth", "sleight_of_hand"],
    "spy": ["deception", "stealth"],
    "dimir_operative": ["deception", "stealth"],
    "entertainer": ["acrobatics", "performance"],
    "faceless": ["deception", "intimidation"],
    "failed_merchant": ["investigation", "persuasion"],
    "far_traveler": ["insight", "perception"],
    "farmer": ["animal_handling", "nature"],
    "feylost": ["deception", "survival"],
    "fisher": ["history", "survival"],
    "folk_hero": ["animal_handling", "survival"],
    "noble": ["insight", "persuasion"],
}

alignment = ["lawful/good", "lawful/neutral", "lawful/evil",
             "neutral/good", "true neutral", "neutral/evil",
             "chaotic/good", "chaotic/neutral", "chaotic/evil"]

item_group_dict = {
    "martial_weapon" : ["battleaxe", "flail", "glaive", "greataxe", "greatsword", "halberd", "lance", "longsword", "maul", "morningstar", "pike", "rapier", "scimitar", "shortsword", "trident", "war_pick", "warhammer", "whip"],
    "simple_weapon" : ["crossbow_light", "dart", "shortbow", "sling"],
    "weapon" : ["club", "dagger", "greatclub", "handaxe", "javelin", "light_hammer", "mace", "quarterstaff", "sickle", "spear"],
    
    "musical_instrument": ["bagpipes", "drum", "dulcimer", "flute", "lute", "lyre", "horn", "pan_flute", "shawm", "viol"],

    "priest's_pack": [[1, "backpack"], [1, "blanket"], [10, "candle"], [1, "tinderbox"], [1, "alms_box"], [2, "block_of_incense"], [1, "censer"], [1, "vestments"], [2, "ration"], [1, "waterskin"]],
    "burglar's_pack": [[1, "backpack"], [1, "bag_of_ball_bearings"], [10, "string"], [1, "bell"], [5, "candle"], [1, "crowbar"], [1, "hammer"], [10, "piton"], [1, "hooded_lantern"], [2, "flask_of_oil"], [5, "ration"], [1, "tinderbox"], [1, "waterskin"], [50, "hemp_rope"]],
    "scholar's_pack" : [[1, "backpack"], [1, "book_of_lore"], [1, "bottle_of_ink"], [1, "ink_pen"], [10, "sheet_of_parchment"], [1, "bag_of_sand"], [1, "knife"]],
    "diplomat's_pack": [[1, "chest"], [2, "case_for_maps_and_scrolls"], [1, "set_of_fine_clothes"], [1, "bottle_of_ink"], [1, "ink_pen"], [1, "lamp"], [2, "flask_of_oil"], [5, "sheet_of_parchment"], [1, "vial_of_perfume"], [1, "sealing_wax"], [1, "soap"]],
    "explorers_pack" : [[1, "backpack"], [1, "bedroll"], [1, "mess_kit"], [1, "tinderbox"], [10, "torch"], [10, "ration"], [1, "waterskin"], [50, "hemp_rope"]],
    "dungeoneer's_pack": [[1, "backpack"], [1, "crowbar"], [1, "hammer"], [10, "piton"], [10, "torch"], [1, "tinderbox"], [10, "ration"], [1, "waterskin"], [50, "hemp_rope"]],
    "entertainer's_pack": [[1, "backpack"], [1, "bedroll"], [2, "costume"], [5, "candle"], [5, "ration"], [1, "waterskin"], [1, "disguise_kit"]],
}

weapons = {
    "simple_melee_weapons": {
        "club": {"cost": 1, "damage": [4, 1], "damage_type": "bludgeoning", "weight": 2, "properties": ["light"]},
        "dagger": {"cost": 2, "damage": [4, 1], "damage_type": "piercing", "weight": 1, "properties": ["finesse", "light", "thrown"]},
        "greatclub": {"cost": 2, "damage": [8, 1], "damage_type": "bludgeoning", "weight": 10, "properties": ["two-handed"]},
        "handaxe": {"cost": 5, "damage": [6, 1], "damage_type": "slashing", "weight": 2, "properties": ["light", "thrown"]},
        "javelin": {"cost": 5, "damage": [6, 1], "damage_type": "piercing", "weight": 2, "properties": ["thrown"]},
        "light_hammer": {"cost": 2, "damage": [4, 1], "damage_type": "bludgeoning", "weight": 2, "properties": ["light", "thrown"]},
        "mace": {"cost": 5, "damage": [6, 1], "damage_type": "bludgeoning", "weight": 4, "properties": ["-"]},
        "quarterstaff": {"cost": 2, "damage": [6, 1], "damage_type": "bludgeoning", "weight": 4, "properties": ["versatile"]},
        "sickle": {"cost": 1, "damage": [4, 1], "damage_type": "slashing", "weight": 2, "properties": ["light"]},
        "spear": {"cost": 1, "damage": [6, 1], "damage_type": "piercing", "weight": 3, "properties": ["thrown", "versatile"]},
        "unarmed": {"cost": 0, "damage": [1, 1], "damage_type": "bludgeoning", "weight": 0, "properties": ["light"]},
    },
    "simple_ranged_weapons": {
        "crossbow_light": {"cost": 25, "damage": [8, 1], "damage_type": "piercing", "weight": 5, "properties": ["ammunition", "loading", "two-handed"]},
        "dart": {"cost": 0.05, "damage": [4, 1], "damage_type": "piercing", "weight": 0.25, "properties": ["finesse", "thrown"]},
        "shortbow": {"cost": 25, "damage": [6, 1], "damage_type": "piercing", "weight": 2, "properties": ["ammunition", "two-handed"]},
        "sling": {"cost": 1, "damage": [4, 1], "damage_type": "bludgeoning", "weight": 0, "properties": ["ammunition"]},
    },
    "martial_melee_weapons": {
        "battleaxe": {"cost": 10, "damage": [8, 1], "damage_type": "slashing", "weight": 4, "properties": ["versatile"]},
        "flail": {"cost": 10, "damage": [8, 1], "damage_type": "bludgeoning", "weight": 2, "properties": ["-"]},
        "glaive": {"cost": 20, "damage": [10, 1], "damage_type": "slashing", "weight": 6, "properties": ["heavy", "reach", "two-handed"]},
        "greataxe": {"cost": 30, "damage": [12, 1], "damage_type": "slashing", "weight": 7, "properties": ["heavy", "two-handed"]},
        "greatsword": {"cost": 50, "damage": [6, 2], "damage_type": "slashing", "weight": 6, "properties": ["heavy", "two-handed"]},
        "halberd": {"cost": 20, "damage": [10, 1], "damage_type": "slashing", "weight": 6, "properties": ["heavy", "reach", "two-handed"]},
        "lance": {"cost": 10, "damage": [12, 1], "damage_type": "piercing", "weight": 6, "properties": ["reach", "special"]},
        "longsword": {"cost": 15, "damage": [8, 1], "damage_type": "slashing", "weight": 3, "properties": ["versatile"]},
        "maul": {"cost": 10, "damage": [6, 2], "damage_type": "bludgeoning", "weight": 10, "properties": ["heavy", "two-handed"]},
        "morningstar": {"cost": 15, "damage": [8, 1], "damage_type": "piercing", "weight": 4, "properties": ["-"]},
        "pike": {"cost": 5, "damage": [10, 1], "damage_type": "piercing", "weight": 18, "properties": ["heavy", "reach", "two-handed"]},
        "rapier": {"cost": 25, "damage": [8, 1], "damage_type": "piercing", "weight": 2, "properties": ["finesse"]},
        "scimitar": {"cost": 25, "damage": [6, 1], "damage_type": "slashing", "weight": 3, "properties": ["finesse", "light"]},
        "shortsword": {"cost": 10, "damage": [6, 1], "damage_type": "piercing", "weight": 2, "properties": ["finesse", "light"]},
        "trident": {"cost": 5, "damage": [6, 1], "damage_type": "piercing", "weight": 4, "properties": ["thrown", "versatile"]},
        "war_pick": {"cost": 5, "damage": [8, 1], "damage_type": "piercing", "weight": 2, "properties": ["-"]},
        "warhammer": {"cost": 15, "damage": [8, 1], "damage_type": "bludgeoning", "weight": 2, "properties": ["versatile"]},
        "whip": {"cost": 2, "damage": [4, 1], "damage_type": "slashing", "weight": 3, "properties": ["finesse", "reach"]},
    },
    "martial_ranged_weapons": {
        "blowgun": {"cost": 10, "damage": [1, 1], "damage_type": "piercing", "weight": 1, "properties": ["ammunition", "loading"]},
        "crossbow_hand": {"cost": 75, "damage": [6, 1], "damage_type": "piercing", "weight": 3, "properties": ["ammunition", "light", "loading"]},
        "crossbow_heavy": {"cost": 50, "damage": [10, 1], "damage_type": "piercing", "weight": 18, "properties": ["ammunition", "heavy", "loading", "two-handed"]},
        "longbow": {"cost": 50, "damage": [8, 1], "damage_type": "piercing", "weight": 2, "properties": ["ammunition", "heavy", "two-handed"]},
        "net": {"cost": 1, "damage": [0, 0], "damage_type": "-", "weight": 3, "properties": ["special", "thrown"]},
    },
}

def get_weapon(weapon_name : str) -> dict:
    return_weapon = weapons["simple_melee_weapons"]["unarmed"]
    for key in weapons:
        if weapon_name in weapons[key].keys():
            return_weapon = weapons[key][weapon_name]
            break
    return return_weapon
    

all_weapons = []
for weapon_type in weapons.values():
    all_weapons.extend(weapon_type.keys())

armor_data = {
    "padded_armor": {
        "ac": [11, "dex_mod"],
        "strength_requirement": 0,
        "stealth": "dis",
        "weight": 8,
        "cost": 5
    },
    "leather_armor": {
        "ac": [11, "dex_mod"],
        "strength_requirement": 0,
        "stealth": None,
        "weight": 10,
        "cost": 10
    },
    "studded_leather_armor": {
        "ac": [12, "dex_mod"],
        "strength_requirement": 0,
        "stealth": None,
        "weight": 13,
        "cost": 45
    },
    "hide_armor": {
        "ac": [12, "dex_mod", 14],
        "strength_requirement": 0,
        "stealth": None,
        "weight": 12,
        "cost": 10
    },
    "chain_shirt_armor": {
        "ac": [13, "dex_mod", 15],
        "strength_requirement": 0,
        "stealth": None,
        "weight": 20,
        "cost": 50
    },
    "scale_mail": {
        "ac": [14, "dex_mod", 16],
        "strength_requirement": 0,
        "stealth": "dis",
        "weight": 45,
        "cost": 50
    },
    "spiked_armor": {
        "ac": [14, "dex_mod", 16],
        "strength_requirement": 0,
        "stealth": "dis",
        "weight": 45,
        "cost": 75
    },
    "breastplate": {
        "ac": [14, "dex_mod", 16],
        "strength_requirement": 0,
        "stealth": None,
        "weight": 20,
        "cost": 400
    },
    "halfplate": {
        "ac": [15, "dex_mod", 17],
        "strength_requirement": 0,
        "stealth": "dis",
        "weight": 40,
        "cost": 750
    },
    "ring_mail": {
        "ac": [14],
        "strength_requirement": 0,
        "stealth": "dis",
        "weight": 40,
        "cost": 30
    },
    "chain_mail": {
        "ac": [16],
        "strength_requirement": 13,
        "stealth": "dis",
        "weight": 55,
        "cost": 75
    },
    "splint_armor": {
        "ac": [17],
        "strength_requirement": 15,
        "stealth": "dis",
        "weight": 60,
        "cost": 200
    },
    "plate_armor": {
        "ac": [18],
        "strength_requirement": 15,
        "stealth": "dis",
        "weight": 65,
        "cost": 1500
    }
}

starting_items = {
    "barbarian": {
        1: [
            [1, "greataxe"],
            [1, item_group_dict["martial_weapon"]]
        ],
        2: [
            [2, "handaxe"],
            [1, item_group_dict["simple_weapon"]]
        ],
        3: [
            [0, item_group_dict["explorers_pack"]]
        ],
        4: [
            [4, "javelin"]
        ]
    },

    "bard": {
        1: [
            [1, "rapier"],
            [1, "longsword"],
            [1, item_group_dict["simple_weapon"]]
        ],
        2: [
            [0, item_group_dict["diplomat's_pack"]],
            [0, item_group_dict["entertainer's_pack"]],
        ],
        3: [
            [1, "lute"],
            [1, item_group_dict["musical_instrument"]]
        ],
        4: [
            [1, "leather_armor"],
            [1, "dagger"]
        ],
    },

    "cleric": {
        1: [
            [1, "mace"],
            [1, "warhammer"]
        ],
        2: [
            [1, "scale_mail"],
            [1, "leather_armor"],
            [1, "chain_mail"]
        ],
        3: [
            [[1, "crossbow_light"], [20, "bolt"]],
            [1, item_group_dict["simple_weapon"]]
        ],
        4: [
            [0, item_group_dict["priest's_pack"]],
            [0, item_group_dict["explorers_pack"]]
        ],
        5: [
            [1, "shield"]
        ],
        6: [
            [1, "holy_symbol"]
        ]
    },
    
    "druid": {
    1: [
        [1, "wooden_shield"],
        [1, item_group_dict["simple_weapon"]]
    ],
    2: [
        [1, "scimitar"],
        [1, item_group_dict["weapon"]]
    ],
    3: [
        [[1, "leather_armor"], [1, "druidic_focus"]]
    ],
    4: [
        [0, item_group_dict["explorers_pack"]]
    ]
    },

    "fighter": {
    1: [
        [1, "chain_mail"],
        [[1, "leather_armor"], [1, "longbow"], [20, "arrow"]]
    ],
    2: [
        [1, item_group_dict["martial_weapon"]]
    ],
    3: [
        [1, "shield"],
        [1, item_group_dict["martial_weapon"]]
    ],
    4: [
        [[1, "crossbow_light"], [20, "bolt"]],
        [2, "handaxe"]
    ],
    5: [
        [0, item_group_dict["explorers_pack"]],
        [0, item_group_dict["dungeoneer's_pack"]]
    ]
    },

    "monk": {
    1: [
        [1, "shortsword"],
        [1, item_group_dict["simple_weapon"]]
    ],
    2: [
        [0, item_group_dict["dungeoneer's_pack"]],
        [0, item_group_dict["explorers_pack"]]
    ],
    3: [
        [10, "dart"]
    ]
    },
    "paladin": {
        1: [
            [1, item_group_dict["martial_weapon"]]
        ],
        2: [
            [1, "shield"],
            [1, item_group_dict["martial_weapon"]]
        ],
        3: [
            [5, "javelin"],
            [1, item_group_dict["simple_weapon"]]
        ],
        4: [
            [0, item_group_dict["priest's_pack"]],
            [0, item_group_dict["explorers_pack"]]
        ],
        5: [
            [[1, "chain_mail"], [1, "holy_symbol"]]
        ]
    },
    "ranger": {
        1: [
            [1, "scale_mail"],
            [1, "leather_armor"]
        ],
        2: [
            [2, "shortsword"],
            [2, item_group_dict["simple_weapon"]]
        ],
        3: [
            [0, item_group_dict["dungeoneer's_pack"]],
            [0, item_group_dict["explorers_pack"]]
        ],
        4: [
            [[1, "longbow"], [1, "quiver"], [20, "arrow"]]
        ]
    },
    "rogue": {
        1: [
            [1, "rapier"],
            [1, "shortsword"]
        ],
        2: [
            [[1, "shortbow"], [1, "quiver"], [20, "arrow"]],
            [1, "shortsword"]
        ],
        3: [
            [0, item_group_dict["burglar's_pack"]],
            [0, item_group_dict["dungeoneer's_pack"]],
            [0, item_group_dict["explorers_pack"]]
        ],
        4: [
            [[1, "leather_armor"], [2, "dagger"], [1, "thieves'_tools"]]
        ]
    },
    "sorcerer": {
        1: [
            [[1, "crossbow_light"], [20, "bolt"]],
            [1, item_group_dict["simple_weapon"]]
        ],
        2: [
            [1, "component_pouch"],
            [1, "arcane_focus"]
        ],
        3: [
            [0, item_group_dict["dungeoneer's_pack"]],
            [0, item_group_dict["explorers_pack"]]
        ],
        4: [
            [2, "dagger"]
        ]
    },
    "warlock": {
        1: [
            [[1, "crossbow_light"], [20, "bolt"]],
            [1, item_group_dict["simple_weapon"]]
        ],
        2: [
            [1, "component_pouch"],
            [1, "arcane_focus"]
        ],
        3: [
            [0, item_group_dict["scholar's_pack"]],
            [0, item_group_dict["dungeoneer's_pack"]]
        ],
        4: [
            [1, "leather_armor"],
            [2, "dagger"]
        ],
        5: [
            [1, item_group_dict["simple_weapon"]]
        ]
    },
    "wizard": {
        1: [
            [1, "quarterstaff"],
            [1, "dagger"]
        ],
        2: [
            [1, "component_pouch"],
            [1, "arcane_focus"]
        ],
        3: [
            [0, item_group_dict["scholar's_pack"]],
            [0, item_group_dict["explorers_pack"]]
        ],
        4: [
            [1, "spellbook"]
        ]
    },
    "artificer": {
        1: [
            [2, item_group_dict["simple_weapon"]]
        ],
        2: [
            [1, "crossbow_light"],
            [20, "bolt"]
        ],
        3: [
            [1, "studded_leather_armor"],
            [1, "scale_mail"]
        ],
        4: [
            [0, item_group_dict["dungeoneer's_pack"]]
        ],
        5: [
            [1, "thieves'_tools"]
        ]
    }
}

names = [
    "Aarion", "Aldric", "Aramis", "Baelor", "Barthos", "Caelen", "Caspian", "Darius", "Dorn", "Eldrin",
    "Eogan", "Faelan", "Fenris", "Gideon", "Grimm", "Hadrian", "Harlock", "Ignis", "Jareth", "Kael",
    "Kendar", "Lorian", "Magnus", "Merek", "Nael", "Oberon", "Orion", "Perrin", "Quillon", "Ragnar",
    "Rhys", "Sargon", "Silas", "Talos", "Thane", "Ulric", "Valerian", "Vesper", "Warrick", "Xander",
    "Zephyr", "Zorian", "Alaric", "Anselm", "Baldur", "Bran", "Cedric", "Corvin", "Draven", "Eamon",
    "Evander", "Falkor", "Gareth", "Goran", "Hakon", "Icarus", "Jorin", "Kaelan", "Kieran", "Leif",
    "Lukas", "Mael", "Neric", "Niall", "Odin", "Osric", "Phelan", "Quentin", "Raffael", "Riven",
    "Saber", "Sevren", "Talon", "Torin", "Uther", "Vaelen", "Viggo", "Wulfric", "Xylan", "Yorick",
    "Zaltar", "Zevran", "Alistair", "Arthus", "Balian", "Cador", "Cyril", "Dagon", "Eldar", "Erevan",
    "Faelron", "Galdor", "Garion", "Haelen", "Isidore", "Jarik", "Kaelor",

    "Aether", "Astra", "Azure", "Beryl", "Blaze", "Cinder", "Cypher", "Echo", "Ember", "Equinox",
    "Fable", "Flare", "Garnet", "Glyph", "Haven", "Horizon", "Indigo", "Jett", "Kindred", "Labyrinth",
    "Lyric", "Mirage", "Nebula", "Nimbus", "Nova", "Onyx", "Oracle", "Paradox", "Phoenix", "Quill",
    "Radiant", "Rune", "Sable", "Sage", "Seraph", "Shadow", "Solstice", "Specter", "Tempest", "Twilight",
    "Umbra", "Veridian", "Vortex", "Whisper", "Wilder", "Zeal", "Zephyr", "Arbor", "Aura", "Briar",
    "Cascade", "Celeste", "Cinder", "Cove", "Crescent", "Dawn", "Dream", "Dusk", "Elysia", "Ember",
    "Fable", "Frost", "Gale", "Glimmer", "Grove", "Haze", "Hearth", "Hollow", "Ivory", "Jade",
    "Lark", "Lumen", "Meridian", "Mesa", "Mist", "Moon", "North", "Oasis", "Peak", "Rain",
    "Reed", "Ridge", "River", "Rowan", "Skye", "Sparrow", "Stone", "Stream", "Thorn", "Vale",
    "Willow", "Wren", "Zenith",

    "Aeliana", "Anya", "Aralyn", "Astraea", "Brienne", "Calista", "Cerys", "Dahlia", "Elara", "Elowen",
    "Elysia", "Faelia", "Faylinn", "Gwendolyn", "Hespera", "Ilaria", "Isolde", "Jezebel", "Kaida", "Kyra",
    "Lilith", "Lyra", "Maeve", "Morgana", "Niamh", "Nyx", "Ophelia", "Oriana", "Persephone", "Rhiannon",
    "Rosalind", "Sabrina", "Seraphina", "Siora", "Sylvia", "Talitha", "Thalia", "Titania", "Ursula", "Valencia",
    "Vespera", "Vivienne", "Winifred", "Xylia", "Ylva", "Zara", "Zephyra", "Zora", "Aisling", "Althea",
    "Amara", "Anwen", "Bellatrix", "Calliope", "Cassia", "Cordelia", "Drusilla", "Eirwen", "Esmeralda", "Fiammetta",
    "Genevieve", "Guinevere", "Hecate", "Idril", "Iolanthe", "Juno", "Kallista", "Larissa", "Leilani", "Lunara",
    "Melisandre", "Mira", "Nerys", "Nuala", "Octavia", "Ondine", "Pandora", "Quintessa", "Ravenna", "Rowena",
    "Sapphira", "Selene", "Signy", "Solveig", "Sybil", "Tanis", "Theodora", "Thisbe", "Undine", "Valda",
    "Velvet", "Virelai", "Walburga", "Xanthe", "Yseult", "Zarina", "Zelda"
]

hit_dice = {
    "artificer": 8,
    "barbarian": 12,
    "bard": 8,
    "cleric": 8,
    "druid": 8,
    "fighter": 10,
    "monk": 8,
    "ranger": 10,
    "rogue": 8,
    "paladin": 10,
    "sorcerer": 6,
    "wizard": 6,
    "warlock": 8
}