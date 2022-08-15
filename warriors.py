fightcount = 0


class Warrior:
    def __init__(self, name, health, attack, rase):
        self.name = name
        self.health = health
        self.attack = attack
        self.rase = rase

    def make_attack(self):
        if self.health > 0:
            return self.attack
        else:
            return 0

    def damage(self, attack):
        self.health -= attack
        return self.health

    def is_a_life(self):
        return self.health > 0

    def get_info(self):
        return (
            "name:" + self.name +
            "\nhealth " + str(self.health) +
            "\nattack " + str(self.attack) +
            "\nrase " + self.rase
        )

elf = Warrior("dobbi", 123, 13, "mistycal")
human = Warrior("robin", 100, 17, "human")

while elf.is_a_life() and human.is_a_life():
    elf.damage(human.make_attack())
    human.damage(elf.make_attack())
    print("Схватка окончена,но крови не достаточно!")
    fightcount += 1
print("===============================================")
if elf.is_a_life():
    print("Эльфы выиграли!")
    print(elf.get_info())
elif human.is_a_life():
    print("Люди выиграли!")
    print(human.get_info())
else:
    print("В поединке погибли оба!")
print("===============================================")
print(fightcount)