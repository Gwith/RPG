from RPG.classes.hero import Hero

import random

class Rogue(Hero):
    '''Rogue class data'''
    class_type = 'Rogue'
    # rogue abilities
    book = {
        'eviscerate': {'low_damage': 100, 'high_damage': 100, 'cost': 10},
        'backstab': {'low_damage': 5, 'high_damage': 10, 'cost': 5}}

    def __init__(self, *args, **kwargs):  # collect all arguments and keyword arguments
        super().__init__(*args, **kwargs)  # call the super class __init__ and pass all the arguments and keyword arguments to it
        self.energy = 100
        self.fullenergy = self.energy

    def damage(self, spell):
        spell_damage = random.randint(
            self.book[spell]['low_damage'],
            self.book[spell]['high_damage'])
        self.energy -= self.book[spell]['cost']
        return spell_damage