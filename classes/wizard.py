from RPG.classes.hero import Hero

import random

class Wizard(Hero):
    '''Wizard class data'''
    class_type = 'Wizard'
    # mage spells
    book = {
        'fireball': {'low_damage': 100, 'high_damage': 100, 'cost': 10},
        'frostbolt': {'low_damage': 5, 'high_damage': 10, 'cost': 5}}

    def __init__(self, *args, **kwargs):  # collect all arguments and keyword arguments
        super().__init__(*args, **kwargs)  # call the super class __init__ and pass all the arguments and keyword arguments to it
        self.mana = 100
        self.fullmana = self.mana

    def damage(self, spell):
        spell_damage = random.randint(
            self.book[spell]['low_damage'],
            self.book[spell]['high_damage'])
        self.mana -= self.book[spell]['cost']
        return spell_damage

    # used to restore mana
    def mana_potion(self):
        self.mana = self.fullmana