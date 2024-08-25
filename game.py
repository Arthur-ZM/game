# game.py
from player import Player
from enemy import Enemy

class Game():
    def __init__(self, player):
        self.player = player
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def start(self):
        print("Choose an enemy to fight:")
        for i, enemy in enumerate(self.enemies):
            print(f"{i+1}. {enemy.name} (Health: {enemy.health}, Armor: {enemy.armor}, Level: {enemy.level})")

        while True:
            choice = input("Enter the number of the enemy you want to fight: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.enemies):
                chosen_enemy = self.enemies[int(choice) - 1]
                self.player.fight(chosen_enemy)
                break
            else:
                print("Invalid choice. Please try again.")

arthur = Player("Arthur", health=50, armor=5, level=1)
goblin = Enemy("Goblin", health=50, armor=1, level=1)
orc = Enemy("Orc", health=70, armor=3, level=2)
troll = Enemy("Troll", health=100, armor=5, level=3)

game = Game(arthur)
game.add_enemy(goblin)
game.add_enemy(orc)
game.add_enemy(troll)

game.start()