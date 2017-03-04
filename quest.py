class Quest:
    __id = None
    __steps = None
    __game = None

    def __init__(self, quest_obj, game):
        self.__game = game
        self.__id = quest_obj['id']
        self.__steps = quest_obj['steps']

    def process(self, cur_step):
        for step in self.__steps:
            if cur_step == step['id']:
                print(step['welcome'])
