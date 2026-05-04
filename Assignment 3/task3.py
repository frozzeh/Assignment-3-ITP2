class MagicPotion:
    """
    This class represents a separate entity that can be
    associated with any Creature object.
    """

    def __init__(self, name, effect, potency):
        self.name = name
        self.effect = effect
        self.potency = potency

    def use(self):
        """Prints a message when the potion is consumed."""
        print(f"The {self.name} is glowing! Effect: {self.effect}")


# Updating the Creature class (Base class remains the same, but adding potion logic)
class Creature:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        # Association: The creature can 'have' a potion object
        self.potion = None

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. HP: {self.health}")

    def is_alive(self):
        return self.health > 0

    def drink_potion(self, potion):
        """
        Demonstrates Association: This method takes an instance
        of MagicPotion as an argument.
        """
        if potion:
            self.health += potion.potency
            print(f"{self.name} drinks {potion.name} and recovers {potion.potency} HP!")
            potion.use()
            self.potion = None  # The potion is now used up
        else:
            print(f"{self.name} has no potion to drink!")

    def attack(self):
        raise NotImplementedError("Subclasses must implement attack()")


# (Dragon and Phoenix classes remain the same, inheriting the new drink_potion method)
class Dragon(Creature):
    def __init__(self, name, fire_power):
        super().__init__(name)
        self.fire_power = fire_power

    def take_damage(self, damage):
        if self.fire_power > 30:
            damage = max(0, damage - 10)
        super().take_damage(damage)

    def attack(self):
        return self.fire_power // 2


# --- Testing Problem 3 ---
if __name__ == "__main__":
    print("--- Problem 3 Test ---")

    # Create instances
    my_dragon = Dragon("Smaug", 50)
    healing_brew = MagicPotion("Elixir of Life", "Healing", 25)

    # Assign the potion to the dragon (Association)
    my_dragon.potion = healing_brew

    # Test the association logic
    print(f"Health before: {my_dragon.health}")
    my_dragon.drink_potion(my_dragon.potion)
    print(f"Health after: {my_dragon.health}")