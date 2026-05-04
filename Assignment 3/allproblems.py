import random


# ==========================================
# PROBLEM 3: Association Class
# ==========================================

class MagicPotion:
    """
    Association: This class exists independently of the Creature class.
    It represents an object that a Creature can 'have' or 'know'.
    """

    def __init__(self, name, effect, potency):
        self.name = name
        self.effect = effect
        self.potency = potency

    def use(self):
        print(f"✨ The {self.name} is consumed! Effect: {self.effect}")


# ==========================================
# PROBLEM 1 & 2: Inheritance & Polymorphism
# ==========================================

class Creature:
    """
    Parent Class: Demonstrates Inheritance.
    Common attributes (name, health) and methods (take_damage, is_alive)
    are defined here once so all child classes can reuse them.
    """

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        # Association: Creature starts with no potion
        self.potion = None

    def take_damage(self, damage):
        """Standard damage logic used by most creatures."""
        self.health -= damage
        print(f"💥 {self.name} takes {damage} damage! HP: {self.health}")

    def is_alive(self):
        """Check if creature is still in the game."""
        return self.health > 0

    def drink_potion(self, potion):
        """
        Association: Method that interacts with a MagicPotion object.
        It uses the potency of the potion to update the creature's state.
        """
        if potion:
            self.health += potion.potency
            print(f"🧪 {self.name} drinks {potion.name} and heals for {potion.potency}!")
            potion.use()
            self.potion = None  # Potion is consumed
        else:
            print(f"{self.name} has no potion to drink!")

    def attack(self):
        """
        Polymorphism: This is a placeholder method.
        Subclasses MUST override this with their own behavior[cite: 2].
        """
        raise NotImplementedError("Subclasses must implement attack()")


class Dragon(Creature):
    """
    Inheritance: Inherits from Creature[cite: 2].
    """

    def __init__(self, name, fire_power):
        super().__init__(name)
        self.fire_power = fire_power

    def take_damage(self, damage):
        """
        Method Overriding: Customizes the parent's take_damage method.
        Reduces damage by 10 if fire_power > 30[cite: 2].
        """
        if self.fire_power > 30:
            damage = max(0, damage - 10)
            print(f"🛡️ {self.name}'s scales absorbed 10 damage!")
        super().take_damage(damage)

    def attack(self):
        """
        Polymorphism: Unique attack logic based on fire_power[cite: 2].
        """
        damage = self.fire_power // 2
        print(f"🔥 {self.name} breathes a torrent of fire!")
        return damage


class Unicorn(Creature):
    """
    Inheritance: Inherits from Creature[cite: 2].
    """

    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

    def attack(self):
        """
        Polymorphism: Unique fixed gentle damage[cite: 2].
        """
        damage = 15
        print(f"🦄 {self.name} charges with a magical horn strike!")
        return damage

    def heal(self):
        """Unique child-class method."""
        self.health += self.heal_amount
        print(f"💖 {self.name} glows, healing for {self.heal_amount}!")


class Phoenix(Creature):
    """
    Polymorphism & Inheritance: A new type of creature with
    a revival mechanic and randomized attack[cite: 2].
    """

    def __init__(self, name, flame_health):
        super().__init__(name)
        self.flame_health = flame_health

    def attack(self):
        """
        Polymorphism: Random damage element[cite: 2].
        """
        damage = 10 + random.randint(5, 15)
        print(f"🐦 {self.name} lashes out with wings of fire!")
        return damage

    def take_damage(self, damage):
        super().take_damage(damage)
        # Revival mechanic: Resets health if it hits 0
        if self.health <= 0 and self.flame_health > 0:
            self.health = 50
            self.flame_health = 0  # Can only revive once
            print(f"🌅 {self.name} died but was reborn from the ashes!")


# ==========================================
# BONUS: Goblin — steals potions mid-battle
# ==========================================

class Goblin(Creature):
    """
    Bonus class: Inherits from Creature.
    Demonstrates Association — Goblin interacts with MagicPotion objects
    belonging to OTHER creatures by stealing them.
    steal_potion() is a unique method not found in other classes.
    """

    def __init__(self, name, steal_chance=0.5):
        super().__init__(name)
        # steal_chance: probability (0.0–1.0) of successfully stealing each round
        self.steal_chance = steal_chance

    def attack(self):
        """
        Polymorphism: Goblin deals small but consistent damage.
        """
        damage = random.randint(8, 18)
        print(f"🗡️ {self.name} stabs with a rusty dagger!")
        return damage

    def steal_potion(self, target):
        """
        Unique Goblin method — Association in action:
        The Goblin reaches into the target's inventory and takes their potion.
        If the steal succeeds and the target has a potion, Goblin claims it.
        If the Goblin already holds a potion, the stolen one is consumed instantly.
        """
        if target.potion is None:
            print(f"👜 {self.name} tries to steal but {target.name} has no potion!")
            return

        if random.random() < self.steal_chance:
            stolen = target.potion
            target.potion = None  # Remove potion from victim

            if self.potion is None:
                # Goblin keeps the potion for later
                self.potion = stolen
                print(f"💰 {self.name} sneakily steals {stolen.name} from {target.name}!")
            else:
                # Goblin's hands are full — drinks it on the spot
                self.health += stolen.potency
                print(f"💰 {self.name} steals {stolen.name} from {target.name} "
                      f"and gulps it down immediately! (+{stolen.potency} HP)")
        else:
            print(f"🙈 {self.name} tried to steal from {target.name} but got caught!")


# ==========================================
# PROBLEM 4: Battle Simulator
# ==========================================

class Battle:
    """
    Association: This class holds two Creature objects and manages
    their interaction during a fight.
    If one of the fighters is a Goblin, it will attempt to steal
    the opponent's potion at the start of each round.
    """

    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def fight_rounds(self, num_rounds):
        print(f"⚔️  BATTLE START: {self.c1.name} vs {self.c2.name} ⚔️")

        # Assign random potions to fighters
        potions_list = [
            MagicPotion("Ancient Brew", "Major Healing", 40),
            MagicPotion("Honey Dew", "Minor Healing", 15)
        ]
        self.c1.potion = random.choice(potions_list)
        self.c2.potion = random.choice(potions_list)

        for r in range(1, num_rounds + 1):
            if not self.c1.is_alive() or not self.c2.is_alive():
                break

            print(f"\n--- ROUND {r} ---")

            # Bonus: Goblin steal attempt at the start of each round
            # If c1 is a Goblin, it tries to steal from c2, and vice versa
            if isinstance(self.c1, Goblin):
                self.c1.steal_potion(self.c2)
            if isinstance(self.c2, Goblin):
                self.c2.steal_potion(self.c1)

            # C1 attacks C2
            dmg1 = self.c1.attack()
            self.c2.take_damage(dmg1)

            if not self.c2.is_alive():
                print(f"☠️ {self.c2.name} has fallen!")
                break

            # C2 attacks C1
            dmg2 = self.c2.attack()
            self.c1.take_damage(dmg2)

            if not self.c1.is_alive():
                print(f"☠️ {self.c1.name} has fallen!")
                break

            # Potion logic: Drink if health is low
            for fighter in [self.c1, self.c2]:
                if fighter.health < 35 and fighter.potion:
                    fighter.drink_potion(fighter.potion)

        print("\n" + "=" * 30)
        print("BATTLE FINISHED")
        if self.c1.health > self.c2.health:
            print(f"🏆 WINNER: {self.c1.name}!")
        elif self.c2.health > self.c1.health:
            print(f"🏆 WINNER: {self.c2.name}!")
        else:
            print("🤝 It's a Draw!")
        print("=" * 30)


# ==========================================
# TEST EXECUTION
# ==========================================

if __name__ == "__main__":
    # Initialize fighters
    smaug = Dragon("Smaug", fire_power=55)
    fawkes = Phoenix("Fawkes", flame_health=1)

    # Start simulation
    match = Battle(smaug, fawkes)
    match.fight_rounds(3)
    print("\n" + "=" * 40)
    print("BONUS TEST: Goblin vs Dragon")
    print("=" * 40)
    grix = Goblin("Grix", steal_chance=0.7)
    ember = Dragon("Ember", fire_power=40)
    match2 = Battle(grix, ember)
    match2.fight_rounds(5)