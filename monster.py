from character import Character
import random

class Monster(Character):
    def __init__(self, name="Monster"):
        super().__init__(name)
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(10, 20)

    def monster_attacks(self, hero):
        print(f"The monster attacks {hero.name}!")
        if self.combat_strength >= hero.health_points:
            print(f"The monster has defeated {hero.name}!")
            hero.health_points = 0
        else:
            hero.health_points -= self.combat_strength
            print(f"{hero.name}'s health is now {hero.health_points}.")

    def __del__(self):
        print("The Monster object is being destroyed.")
        super().__del__()
