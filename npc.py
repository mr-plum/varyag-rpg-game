from constants import Constants


class Npc:
    __id = None
    __game = None

    def __init__(self, npc_obj, game):
        self.__game = game
        self.__id = npc_obj['id']
        self.__speak = npc_obj['speak']

    def say(self, last_id):
        for say in self.__speak:
            if say['id'] == last_id:
                for item in say['text']:
                    print(item)

                if 'get' in say.keys():
                    for stuff_id in say['get']:
                        self.__game.add_stuff_to_player(stuff_id)

                #если не предполагается ответ, то выходим
                if 'answers' not in say.keys():
                    return -1

                your_answers = []
                for ans in say['answers']:
                    your_answers.append(ans['text'])
                playerAnswer = self.__game.choose_action(Constants.YOUR_ANSWER, your_answers)

                for ans in say['answers']:
                    if ans['text'] == playerAnswer:
                        return self.say(ans['toId'])