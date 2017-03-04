class Location:
    __id = None
    __start_quest = None
    __start_npc = None

    def __init__(self, loc_obj):
        self.__id = loc_obj['id']
        self.__start_quest = loc_obj['startQuest']
        self.__start_npc = loc_obj['startNpc']

    def has_start_quest(self):
        return self.__start_quest is not None

    def get_start_quest(self):
        return self.__start_quest

    def has_start_npc(self):
        return self.__start_npc is not None

    def get_start_npc(self):
        return self.__start_npc