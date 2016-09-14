from characters import Hero, Enemy
from weapons_and_spells import Weapon, Spell


def main():
    my_hero = Hero(name='Wencakisa', title='Kingslayer', health=100, mana=100, mana_regeneration_rate=2)
    my_enemy = Enemy(health=100, mana=100, damage=10)
    my_weapon = Weapon(name='Windcutter', damage=10)
    my_spell = Spell(name='Fireball', damage=7, mana_cost=4, cast_range=1)
    my_hero.equip(my_weapon)
    my_hero.learn(my_spell)

    while my_hero.is_alive() and my_enemy.is_alive():
        print(my_enemy.attack(enemy=my_hero))
        my_enemy.take_healing(healing_points=40)
        print(my_hero.attack(by='spell', enemy=my_enemy))
        print(my_hero.attack(by='weapon', enemy=my_enemy))


if __name__ == '__main__':
    main()
