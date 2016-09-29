import random
from RPG.classes.enemy import Enemy

class Goblin_Boss(Enemy):
    '''Monster class ability checks and damage'''

    # npc abilities
    book = {
        'slash': {'low_damage': 5, 'high_damage': 10},
        'bite': {'low_damage': 10, 'high_damage': 15}}

    def __init__(self, *args, **kwargs):  # collect all arguments and keyword arguments
        super().__init__(*args, **kwargs)  # call the super class __init__ and pass all the arguments and keyword arguments to it
        self.name = 'Goblin Boss'

    def yield_choice(self):
        ability = random.choice(list(self.book.keys()))
        return ability

    def damage(self, ability):
        ability_damage = random.randint(
            self.book[ability]['low_damage'],
            self.book[ability]['high_damage'])
        return ability_damage

    # calculate damage recieved
    def rec_damage(self, amount, attacker):
        self.hp -= amount
        self.damage_received += amount
        attacker.damage_dealt += amount
        # to do: add in armor/defense/evasion/ect
        return amount