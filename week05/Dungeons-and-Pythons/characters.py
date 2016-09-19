from weapons_and_spells import Weapon, Spell


class Hero:
    def __init__(self, name: str, title: str, health: float, mana: float, mana_regeneration_rate: int):
        self._name = name
        self._title = title
        self._health = self.validate_stat(health)
        self._max_health = self._health
        self._mana = self.validate_stat(mana)
        self._mana_regeneration_rate = mana_regeneration_rate
        self._weapon = None
        self._spell = None

    @staticmethod
    def validate_stat(stat: float):
        if stat < 0 or stat > 100:
            raise ValueError('Stats must be in the range 0-100!')

        return float(stat)

    def known_as(self):
        return '{} the {}'.format(self._name, self._title)

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        return self._health > 0

    def can_cast(self):
        return self._mana > 0 and self._mana >= self._spell.mana_cost

    def take_damage(self, damage_points: float) -> bool:
        if self._health - damage_points > 0:
            self._health -= damage_points
            return True

        self._health = 0
        return False

    def take_healing(self, healing_points: float) -> bool:
        if not self.is_alive() or self.get_health() + healing_points > self._max_health:
            return False

        self._health += healing_points
        return True

    def take_mana(self, mana_points: float) -> bool:
        self._mana += mana_points

    def equip(self, weapon: Weapon):
        self._weapon = weapon

    def learn(self, spell: Spell):
        self._spell = spell

    def attack(self, by: str, enemy) -> str:
        if self.is_alive():
            if by == 'weapon':
                if self._weapon is None:
                    return "You haven't equipped a weapon yet."

                attack_phrase = 'hits with {} for {:.2f} dmg'.format(self._weapon, self._weapon.damage)
                health_loss = self._weapon.damage
            elif by == 'spell':
                if self._spell is None:
                    return "You haven't learned a spell yet."

                attack_phrase = 'casts a {} for {:.2f} dmg'.format(self._spell, self._spell.damage)
                health_loss = self._spell.damage
                self._mana -= self._spell.mana_cost
            else:
                return "You can't attack by {}".format(by)

            enemy._health -= health_loss
            self._mana += self._mana_regeneration_rate

            return '{} {}. Enemy health is {:.2f}'.format(
                str(self),
                attack_phrase,
                enemy.get_health() if enemy.get_health() >= 0 else 0
            )

        return '{} is dead and can not attack!'.format(self.known_as())

    def __str__(self):
        return self.known_as()

    def __repr__(self):
        return self.__str__()


class Enemy(Hero):
    def __init__(self, health: float, mana: float, damage: float):
        super().__init__(name='', title='', health=health, mana=mana, mana_regeneration_rate=0)
        self._damage = damage

    def take_mana(self, mana_points: float):
        pass

    def attack(self, enemy: Hero, by='weapon') -> str:
        if self.is_alive():
            enemy._health -= self._damage

            return 'Enemy hits {} for {:.2f} dmg. {} health is {:.2f}'.format(
                enemy.known_as(),
                self._damage,
                enemy.known_as(),
                enemy.get_health() if enemy.get_health() >= 0 else 0
            )

        return 'Enemy is dead and can not attack!'
