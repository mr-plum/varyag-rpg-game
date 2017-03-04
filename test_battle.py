from battle import Battle
from main import Game
from player import Player

game = Game()
player = Player('Викинг', game)
game.set_player(player)
player.selected_weapon = game.get_stuff(3)

enemy = game.get_enemy(1)
enemy.selected_weapon = game.get_stuff(3)

battle = Battle(player, enemy, game)
battle.fight()
winner = battle.get_winner()

print("Победил {0} ({1} ОЖ)".format(winner.name, winner.health))
