from character import Character


class Enemy(Character):
    id = None

    def __init__(self, enemy_obj, game):
        super().__init__(game, char_obj=enemy_obj)
        for field in ['id']:
            if field in enemy_obj.keys():
                setattr(self, field, enemy_obj[field])
