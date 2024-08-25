import player
import random

class Enemy():
    def __init__(self, name, health, armor, level):
        self.name = name
        self.health = health
        self.armor = armor
        self.level = level
        self.attack_power = level * 5

    def attack(self, player):
        roll = random.randint(1, 20)
        if roll >= player.armor:
            if roll == 20:
                print("Enemy landed a critical hit")
                damage = self.attack_power * self.attack_power
                print(f"Enemy landed a critical hit to {player.name} dealing {damage} points of damage")
                player.health -= damage
                return damage
            elif roll >= 2:
                damage = (self.attack_power * 1) - player.armor
                print(f"Enemy hit {player.name} dealing {damage} points of damage")
                player.health -= damage
                return damage
        else:
            print(f"Enemy missed {player.name}")
            return 0