import random

class Creature:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.potion = None  # Placeholder for Problem 3

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. HP: {self.health}")

    def is_alive(self):
        return self.health > 0

    def attack(self):
        """
        Polymorphism: This base method ensures that if a subclass
        forgets to implement attack(), it raises an error.
        """
        raise NotImplementedError("Subclasses must implement attack()")


class Dragon(Creature):
    def __init__(self, name, fire_power):
        super().__init__(name)
        self.fire_power = fire_power

    def take_damage(self, damage):
        # Shield logic from Problem 1
        if self.fire_power > 30:
            damage = max(0, damage - 10)
        super().take_damage(damage)

    def attack(self):
        """
        Polymorphism: Dragon damage is calculated based on fire_power.
        """
        damage = self.fire_power // 2
        print(f"{self.name} breathes fire!")
        return damage


class Unicorn(Creature):
    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

    def attack(self):
        """
        Polymorphism: Unicorn deals a fixed amount of 'gentle' damage.
        """
        damage = 15
        print(f"{self.name} strikes with its horn!")
        return damage

    def heal(self):
        self.health += self.heal_amount


class Phoenix(Creature):
    """
    New child class for Problem 2.
    Demonstrates unique behavior (Revival) and randomized attack.
    """

    def __init__(self, name, flame_health):
        super().__init__(name)
        self.flame_health = flame_health

    def attack(self):
        """
        Polymorphism: Phoenix has a random element in its attack.
        """
        damage = 10 + random.randint(5, 15)
        print(f"{self.name} attacks with mystical flames!")
        return damage

    def take_damage(self, damage):
        super().take_damage(damage)
        # Revival logic: if health hits 0, it revives once using flame_health
        if self.health <= 0 and self.flame_health > 0:
            self.health = 50
            self.flame_health = 0  # Used up revival
            print(f"--- {self.name} died but rose from the ashes! ---")


# --- Testing Problem 2 ---
if __name__ == "__main__":
    print("--- Problem 2 Test ---")

    # Testing Polymorphism by putting different objects in a list
    army = [
        Dragon("Balerion", 60),
        Unicorn("Star", 10),
        Phoenix("Fawkes", 1)
    ]

    for beast in army:
        # Each beast calls the SAME method name, but results are DIFFERENT
        dmg = beast.attack()
        print(f"Resulting Damage: {dmg}\n")