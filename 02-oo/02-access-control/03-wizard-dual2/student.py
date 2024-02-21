class Wizard:
    def cast_fireball(self, target):
        casting_cost = 20
        if self.__mana >= casting_cost:
            self.__mana -= casting_cost
            target.get_fireballed()
            return f"{self.name} casts fireball at {target.name}"
        else:
            raise Exception(f"{self.name} cannot cast fireball")



    # don't touch below this line

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball_damage = 30
        self.__health -= fireball_damage
        if self.__health <= 0:
            print(f"{self.name} is dead")

    def drink_mana_potion(self):
        self.__mana += 40
