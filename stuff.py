from dice import Dice, Dices


class Stuff:
    __id = None
    is_equipped = False
    slot = None
    __class = None

    def __init__(self, stuff_obj):
        self.__id = stuff_obj['id']
        self.__name = stuff_obj['name']
        if 'class' in stuff_obj.keys():
            self.__class = stuff_obj['class']

        if 'damage' in stuff_obj.keys():
            self.__damage = Dices[stuff_obj['damage']]

    def get_id(self):
        return self.__id

    def get_class(self):
        return self.__class

    def get_name(self):
        return self.__name

    def is_weapon(self):
        return self._damage is not None

    def get_damage(self):
        return self.__damage
