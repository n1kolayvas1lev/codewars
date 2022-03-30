# Something is wrong with our Warrior class.
# All variables should initialize properly and the attack method is not working as expected.
# If properly set, it should correctly calculate the damage after an attack
# (if the attacker position is == to the block position of the defender: no damage;
# otherwise, the defender gets 10 damage if hit "high" or 5 damage if hit "low".
# If no block is set, the defender takes 5 extra damage.
# For some reason, the health value is not being properly set.
# The following shows an example of this code being used:
# ninja = Warrior('Hanzo Hattori')
# samurai = Warrior('Ryōma Sakamoto')
# samurai.block = 'l'
# ninja.attack(samurai, 'h')
# samurai.health should be 90 now
# The warriors must be able to fight to the bitter end, and good luck to the most skilled!
# Notice that health can't be below 0: once hit to 0 health, a warrior attribute deceased becomes true;
# if hit again, the zombie attribute becomes true too!

import random
Position = {'high': 'h', 'low': 'l'}  # don't change this!


class Warrior:
    def __init__(self, name):
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        self.deceased = False
        self.zombie = False
        # default guard is "", that is unguarded
        self.block = ""

    @staticmethod
    def attack(enemy, position):
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        # if enemy.block != position: damage += 10 if position == Position['high'] else 5
        # and even more damage if the enemy is not blocking at all
        # if enemy.block == "": damage += 5
        # enemy.set_health(enemy.health - damage)
        damage = 0
        if enemy.block != position and position == Position['high']:
            damage += 10
        elif enemy.block == position:
            damage += 0
        else:
            damage += 5
        if enemy.block == "":
            damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):  # health cannot have negative values
        self.health = new_health
    # if a warrior is set to 0 health he is dead
        if self.health == 0:
            self.deceased = True
            self.zombie = False
    # he would be a zombie only if he was already dead
        if self.health < 0:
            self.zombie = True

    def __repr__(self) -> str:
        return f'Name {self.name}, Health = {self.health}, Status of deceasing = {self.deceased}, Zombie status = {self.zombie}'


if __name__ == '__main__':
    ninja = Warrior('Hanzo Hattori')
    samurai = Warrior('Ryōma Sakamoto')
    iteration = 0
    while ninja.health >= 0 or samurai.health >= 0:
        iteration += 1
        damage = 0
        attack = random.randint(0, 1)
        attack_status = None
        block = random.randint(0, 2)
        block_status = None
        if attack == 0:
            attack_status = 'h'
            damage = 10
        else:
            attack_status = 'l'
            damage = 5
        if block == 0:
            block_status = 'h'
        elif block == 1:
            block_status = 'l'
        else:
            block_status = ''
            damage += 5
        if attack_status == block_status:
            damage = 0
        samurai.block = block_status
        ninja.attack(samurai, attack_status)
        print(iteration)
        print(f'Attack = {attack_status}, block = {block_status}, damage = {damage}')
        print(samurai)
        print('=' * 30)
        damage = 0
        attack = random.randint(0, 1)
        attack_status = None
        block = random.randint(0, 2)
        block_status = None
        if attack == 0:
            attack_status = 'h'
            damage = 10
        else:
            attack_status = 'l'
            damage = 5
        if block == 0:
            block_status = 'h'
        elif block == 1:
            block_status = 'l'
        else:
            block_status = ''
            damage += 5
        if attack_status == block_status:
            damage = 0
        ninja.block = block_status
        samurai.attack(ninja, attack_status)
        print(iteration)
        print(f'Attack = {attack_status}, block = {block_status}, damage = {damage}')
        print(ninja)
        print('=' * 30)
