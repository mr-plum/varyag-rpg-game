from character import Character
from constants import Constants


class Player(Character):
    current_zone = 1
    current_location = 10
    quest = {}
    npc = {}

    def __init__(self, _name, _game):
        super().__init__(_game, _name)
        self.default_weapon = _game.get_stuff(9)

    def get_quest_last_step(self, quest_id):
        if quest_id not in self.quest.keys():
            self.quest[quest_id] = 0
        return self.quest.get(quest_id)

    def get_npc_last_say_id(self, npc_id):
        if npc_id not in self.npc.keys():
            self.npc[npc_id] = 0
        return self.npc.get(npc_id)

