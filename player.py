import random
import enemy

class Player():
    def __init__(self, name, health, armor, level):
        self.name = name
        self.health = health
        self.armor = armor
        self.level = level
        self.attack_power = level * 5
        self.evade_chance = 0.5  # 50% chance to evade

    def attack(self, enemy):
        roll = random.randint(1, 20)
        if roll >= enemy.armor:
            if roll == 20:
                print("Player landed a critical hit")
                damage = self.attack_power * self.attack_power
                print(f"Player landed a critical hit to {enemy.name} dealing {damage} points of damage")
                enemy.health -= damage
            elif roll >= 2:
                damage = self.attack_power * 1 - enemy.armor
                print(f"Player hit the {enemy.name} dealing {damage} points of damage")
                enemy.health -= damage
        else:
            print(f"Player missed {enemy.name}")

    def evade(self, enemy):
        roll = random.randint(1, 20)
        against_roll = random.randint(1, 20)
        if roll >= against_roll:
            print(f"Player successfully evaded {enemy.name}'s attack!")
            return True
        else:
            print(f"Player failed to evade {enemy.name}'s attack!")
            return False

    def fight(self, enemy):
        while enemy.health > 0 and self.health > 0:
            print("Choose an action:")
            print("1. Attack")
            print("2. Evade")
            print("3. Status")
            choice = input("Enter the number of your chosen action: ")
            if choice == "1":
                self.attack(enemy)
                if enemy.health > 0:
                    enemy_attack = enemy.attack(self)
                    self.health -= enemy_attack
                    print(f"{enemy.name} hit the player dealing {enemy_attack} points of damage")
            elif choice == "2":
                if self.evade(enemy):
                    print("Player gets to attack twice!")
                    self.attack(enemy)
                    if enemy.health > 0:
                        self.attack(enemy)
                else:
                    enemy_attack = enemy.attack(self)
                    self.health -= enemy_attack
                    print(f"{enemy.name} hit the player dealing {enemy_attack} points of damage")
            elif choice == "3":
                print(f"\nName = {self.name} \nHealth = {self.health} \nArmor = {self.armor} \nLevel = {self.level} \nAttack = {self.attack_power} \n")

            else:
                print("Invalid choice. Please try again.")
        self.level_up(enemy)

    def level_up(self, enemy):
        self.level += (enemy.exp * 0.1)

