from numpy.random import choice

def random_choice_from_dict(choice_dict):
    choice = list(choice_dict.key())
    chance = list(choice_dict.values())

    decimal_chance = [chance / sum(chance) for chance in chances]

    return choice(choices, p=decimal_chances)

def from_dungeon_level(table, dungeon_level):
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value
    return 0
