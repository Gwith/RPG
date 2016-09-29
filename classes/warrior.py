from RPG.classes.hero import Hero

import random

class Warrior(Hero):
    '''Wizard class data'''
    class_type = 'Warrior'
    # warrior abilities
    book = {
        'execute': {'low_damage': 100, 'high_damage': 100, 'cost': 10},
        'mortal strike': {'low_damage': 5, 'high_damage': 10, 'cost': 5}}

    def __init__(self, *args, **kwargs):  # collect all arguments and keyword arguments
        super().__init__(*args, **kwargs)  # call the super class __init__ and pass all the arguments and keyword arguments to it
        self.rage = 100
        self.fullrage = self.rage

    def damage(self, spell):
        spell_damage = random.randint(
            self.book[spell]['low_damage'],
            self.book[spell]['high_damage'])
        self.rage -= self.book[spell]['cost']
        return spell_damage