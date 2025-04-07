from character import Character
import random

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(10, 20)

    def hero_attacks(self, monster):
        print(f"{self.name} attacks the monster!")
        if self.combat_strength >= monster.health_points:
            print("The hero has slain the monster!")
            monster.health_points = 0
        else:
            monster.health_points -= self.combat_strength
            print(f"The monster's health is now {monster.health_points}.")

    def __del__(self):
        print("The Hero object is being destroyed.")
        super().__del__()
