def validate_stat(stat: float):
    if stat < 0 or stat > 100:
        raise ValueError('Stats should be in the range 0-100')

    return float(stat)


class Weapon:
    def __init__(self, name: str, damage: float):
        self.name = name
        self.damage = validate_stat(damage)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Spell:
    def __init__(self, name: str, damage: float, mana_cost: float, cast_range: float):
        self.name = name
        self.damage = validate_stat(damage)
        self.mana_cost = validate_stat(mana_cost)
        self.cast_range = validate_stat(cast_range)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
