from constants import Constants
from dice import Dices
from equipment import Equipment


class Character:
    name = None
    level = 1
    health = 100
    max_health = 100
    strength = 3
    dexterity = 3
    default_weapon = None
    selected_weapon = None
    experience = 0
    inventory = []
    equipment = Equipment()

    def __init__(self, game, _name=None, char_obj=None):
        self.name = _name
        if char_obj is not None:
            for field in ['name', 'strength', 'dexterity', 'health', 'max_health']:
                if field in char_obj.keys():
                    setattr(self, field, char_obj[field])
            if 'equip' in char_obj.keys():
                for stuff_id in char_obj['equip']:
                    stuff = game.get_stuff(stuff_id)
                    self.inventory.append(stuff)
                    self.equip(stuff)

    # бросок на величину атаки
    def attack(self):
        return self.selected_weapon.get_damage().throw() + self.strength

    # бросок на вероятность попадания
    def attack_chance(self):
        dice = Dices['1d20']
        val = dice.throw()
        # добавить к значению "владение оружием"
        return {
            'chance': val + self.level // 2 + self.dexterity,
            'crit-hit': val == dice.get_max(),
            'crit-fail': val == dice.get_min()
        }

    def hurt(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

    def add_stuff(self, stuff):
        self.inventory[stuff.get_id()] = stuff
        print(Constants.NEW_STUFF_GAINED.format(stuff.get_name()))

    def equip(self, stuff):
        if stuff.slot is not None:
            self.equipment.add(stuff)

