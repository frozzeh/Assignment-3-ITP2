class Creature:
    """
    Parent Class: Demonstrates Inheritance by storing shared attributes.
    All creatures will have a name and health starting at 100 by default.
    """

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        """Reduces health and prints the status."""
        self.health -= damage
        print(f"{self.name} took {damage} damage. Current HP: {self.health}")

    def is_alive(self):
        """Returns True if health is above 0, demonstrating basic logic encapsulation."""
        return self.health > 0


class Dragon(Creature):
    """
    Child Class: Inherits from Creature.
    Demonstrates Method Overriding to implement a unique defense mechanic.
    """

    def __init__(self, name, fire_power):
        super().__init__(name)  # Inherit name and default health (100)
        self.fire_power = fire_power

    def take_damage(self, damage):
        """
        Polymorphism/Overriding: If fire_power is high (> 30),
        the dragon reduces incoming damage by 10.
        """
        if self.fire_power > 30:
            final_damage = max(0, damage - 10)
            print(f"{self.name}'s dragon scales absorbed some damage!")
        else:
            final_damage = damage

        # Call the parent method to apply the actual health reduction
        super().take_damage(final_damage)


class Unicorn(Creature):
    """
    Child Class: Inherits from Creature.
    Demonstrates class-specific functionality by adding a unique heal method.
    """

    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

    def heal(self):
        """Unique method only available to Unicorn instances."""
        self.health += self.heal_amount
        print(f"{self.name} used magic to heal for {self.heal_amount} HP!")


# --- Testing Problem 1 ---
if __name__ == "__main__":
    print("--- Problem 1 Test ---")

    # Testing Dragon with fire_power > 30 (should reduce damage)
    drogo = Dragon("Drogo", fire_power=40)
    drogo.take_damage(25)

    # Testing Unicorn healing
    celestia = Unicorn("Celestia", heal_amount=20)
    celestia.take_damage(30)
    celestia.heal()

    print(f"Is {drogo.name} alive? {drogo.is_alive()}")
    print(f"Is {celestia.name} alive? {celestia.is_alive()}")