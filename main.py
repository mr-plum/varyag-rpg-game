from json import load

from enemy import Enemy
from feint import Feint
from stuff import Stuff
from zone import Zone
from quest import Quest
from npc import Npc
from location import Location
from player import Player
import pickle
import glob
import logging
from constants import Constants


class Game:
    __player = None
    __actions = None
    __zones = None
    __locations = None
    __npcs = None
    __enemies = None
    __feints = None

    def __init__(self):
        self.__actions = load(open("script/actions.vtg", encoding="utf-8"))
        self.__npc = load(open("script/npc.vtg", encoding="utf-8"))
        self.__stuff = load(open("script/stuff.vtg", encoding="utf-8"))
        self.__zones = load(open("script/zones.vtg", encoding="utf-8"))
        self.__locations = load(open("script/locations.vtg", encoding="utf-8"))
        self.__npcs = load(open("script/npc.vtg", encoding="utf-8"))
        self.__enemies = load(open("script/enemies.vtg", encoding="utf-8"))
        self.__feints = load(open("script/feints.vtg", encoding="utf-8"))

    def start(self):
        print(Constants.WELCOME)
        self.load()
        loc = self.get_location(self.__player.current_location)
        self.action(loc)

    def get_stuff(self, stuff_id):
        for stuff in self.__stuff:
            if stuff_id == stuff['id']:
                return Stuff(stuff)
        return None

    def get_zone(self, zone_id):
        for zone in self.__zones:
            if zone_id == zone['id']:
                return Zone(zone)
        return None

    def get_location(self, location_id):
        for loc in self.__locations:
            if location_id == loc['id']:
                return Location(loc)
        return None

    def get_npc(self, npc_id):
        for npc in self.__npcs:
            if npc_id == npc['id']:
                return Npc(npc, self)
        return None

    def get_enemy(self, enemy_id):
        for en in self.__enemies:
            if enemy_id == en['id']:
                return Enemy(en, self)
        return None

    def get_feints(self, char):
        res = []
        for f in self.__feints:
            if char.selected_weapon.get_class() == f['class'] and f['level'] <= char.level:
                res.append(Feint(f))
        return res

    def get_quest(self, quest_id):
        return Quest(load(open("script/quests/{0}.vtg".format(quest_id), encoding="utf-8")), self)

    #save players data to file
    def save(self):
        f = open("{0}/{1}.vtg".format(Constants.SAVE_DIRECTORY, self.__player.name), 'wb')
        pickle.dump(self.__player, f)
        f.close()

    #load players data
    def load(self):
        files = glob.glob1(Constants.SAVE_DIRECTORY, "*.vtg")
        if len(files) > 0:
            commands = []
            for item in files:
                commands.append(item.replace(".vtg", ""))
            commands.append(Constants.CREATE_NEW_PLAYER)
            cmd = self.choose_action(Constants.CREATE_NEW_OR_LOAD_HERO, commands)
            if cmd + ".vtg" in files:
                self.load_player(cmd)
            elif cmd == Constants.CREATE_NEW_PLAYER:
                self.create_player()
        else:
            self.create_player()

    def set_player(self, _player):
        self.__player = _player

    #loads player data from file
    def load_player(self, _name):
        self.set_player(pickle.load(open("{0}/{1}.vtg".format(Constants.SAVE_DIRECTORY, _name), 'rb')))
        print(Constants.HERO_IS_LOADED.format(self.__player.name))

    #creates new player
    def create_player(self):
        self.set_player(Player(input(Constants.ENTER_HERO_NAME), self))
        self.save()
        print(Constants.HERO_CREATED.format(self.__player.name))

    #choose action from list
    def choose_action(self, prompt, commands):
        print(prompt)
        ind = 0
        for cmd in commands:
            ind += 1
            print(Constants.COMMAND_TEMPLATE.format(ind, cmd))
        ind = self.read_command_index()
        while ind not in range(1, len(commands) + 1):
            ind = self.read_command_index()
        return commands[ind - 1]

    #read commands index from console
    def read_command_index(self):
        res = input(Constants.PROMPT)
        while not res.isdigit():
            print(Constants.ENTER_COMMAND_NUMBER)
            res = input(Constants.PROMPT)
        return int(res)

    #main game method
    def action(self, location):
        if location.has_start_quest():
            self.do_quest(location.get_start_quest(), self.__player.get_quest_last_step(location.get_start_quest()))
        if location.has_start_npc():
            npc = self.get_npc(location.get_start_npc())
            npc.say(self.__player.get_npc_last_say_id(location.get_start_npc()))

    def do_quest(self, quest_id, cur_step):
        quest = self.get_quest(quest_id)
        quest.process(cur_step)

    def add_stuff_to_player(self, stuff_id):
        self.__player.add_stuff(self.get_stuff(stuff_id))

    def add_stuff_to_character(self, character, stuff_id):
        character.add_stuff(self.get_stuff(stuff_id))


# Run the game
logging.basicConfig(level=logging.DEBUG)
if __name__ == "__main__":
    Game().start()
