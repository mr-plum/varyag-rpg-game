import random


class Dice:
    def __init__(self, _count, _edges):
        self.count = _count
        self.edges = _edges

    def throw(self):
        return random.randint(1 * self.count, self.edges * self.count)

    def get_max(self):
        return self.edges * self.count

    def get_min(self):
        return 1 * self.count

Dices = {
    '1d4': Dice(1, 4),
    '1d6': Dice(1, 6),
    '2d6': Dice(2, 6),
    '1d20': Dice(1, 20)
}

random.seed()
