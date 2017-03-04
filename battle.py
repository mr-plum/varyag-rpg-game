from constants import Constants
from player import Player


class Battle:
    __winner = None
    __game = None

    def __init__(self, _attacker, _defender, game):
        self.attacker = _attacker
        self.defender = _defender
        self.__game = game

    def fight(self):
        a = self.attacker
        d = self.defender
        self.hit(a, d)
        while d.is_dead() is False:
            # меняем местами атакующего и обороняющегося
            a, d = d, a
            self.hit(a, d)

    def get_winner(self):
        return self.__winner

    def hit(self, _attacker, _defender):
        if type(_attacker) is Player:
            self.choose_feint(_attacker)
        attacker_res = _attacker.attack_chance()
        defender_res = _defender.attack_chance()

        damage = None
        # критический удар
        if attacker_res['crit-hit']:
            damage = _attacker.attack() * 2
        # критический промах
        elif attacker_res['crit-fail']:
            print(Constants.CHARACTER_CRITICAL_FAIL.format(_attacker.name))
        # попадание
        elif attacker_res['chance'] >= defender_res['chance']:
            damage = _attacker.attack()
        # промах
        else:
            print(Constants.CHARACTER_MISS.format(_attacker.name))

        if damage is not None:
            _defender.hurt(damage)
            print(Constants.CHARACTER_HIT.format(_attacker.name, _defender.name, damage, max(0, _defender.health)))
            if _defender.is_dead():
                print(Constants.CHARACTER_IS_DEAD.format(_defender.name))
                self.__winner = _attacker

    def choose_feint(self, _attacker):
        feints = self.__game.get_feints(_attacker)
        cmds = [x.desc for x in feints]
        return self.__game.choose_action(Constants.CHOOSE_BATTLE_ACTION, cmds)