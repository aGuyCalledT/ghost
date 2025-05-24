import lists, roll
import random


def weapon_attack(attacker : 'Char', target : 'Char', weapon = None, advantage : int = 0) -> None:
    used_weapon = weapon
    if used_weapon is None:
        possible_weapons = []
        for item in attacker.equipped_items:
            if item in lists.all_weapons:
                possible_weapons.append(item)

        used_weapon = random.choice(possible_weapons)

    group = None
    for weapon_group in lists.weapons:
        if used_weapon in lists.weapons[weapon_group]:
            group = weapon_group
    if group is None: 
        return None

    damage_type = lists.weapons[group][used_weapon]["damage_type"]
    properties = lists.weapons[group][used_weapon]["properties"]

    attack_bonus = 0

    if "finesse" in properties:
        attack_bonus += max(attacker.strength_mod, attacker.dexterity_mod)
    else:
        attack_bonus += attacker.strength_mod

    if used_weapon in attacker.proficient: 
        attack_bonus += attacker.proficiency_bonus

    if "heavy" in properties:
        if "small" in attacker.tags:
            advantage -= 1
    
    if "light" in properties:
        # attack with the offhand weapon aswell
        pass

    if "loading" in properties:
        # can only attack once
        pass

    if "range" in properties:
        # check if ammunition is availiable and if target is in normal or long range
        pass

    if "reach" in properties:
        # add 1,5m range
        pass

    if "special" in properties:
        # define a list of 'special' characteristics and add them here somehow
        pass

    if "thrown" in properties:
        # check if target is in normal or long range
        pass

    if "two_handed" in properties:
        # unequip offhand items
        pass

    if "versitile" in properties:
        # use next highest die if no offhand weapon is used
        pass


    damage = lists.weapons[group][used_weapon]["damage"]
    damage = sum(roll.roll(rolls= damage[1], sides= damage[0]))
    
    advantage_bool = True
    hit_roll = 0
    if advantage < 0: 
        advantage = advantage * (-1)
        advantage_bool = False
    
    advantage += 1 
    temp_hit_roll = []
    for x in range(advantage):
        temp_hit_roll.append(sum(roll.roll(rolls= 1, sides= 20)) + attack_bonus)
    if advantage: hit_roll = max(temp_hit_roll)
    else:         hit_roll = min(temp_hit_roll)

    if target.armor_class > hit_roll:
        print(f"The attack with {attacker.name}'s {used_weapon} was blocked by {target.name}s armor. (hit roll: {hit_roll}, ac: {target.armor_class})")

    else:
        target.temp_health_points -= damage
        print(f"{attacker.name} landed a hit on {target.name} with their {used_weapon} causig {damage} {damage_type}-damage.")
        print(f"{target.name}s health is at {target.temp_health_points} HP")
    



# MAIN CODE