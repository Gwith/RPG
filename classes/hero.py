import random

class Hero:
    '''Create common creature class'''
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.fullhp = self.hp
        self.damage_dealt = 0
        self.damage_received = 0
        # to do: add other stats

    def input_choice(self, msg, choices):
        '''prompt user for spell input and check if valid'''
        prompt = "{} [ {} ]: ".format(msg, " | ".join(choices))
        while True:
            resp = input(prompt).lower()
            if resp in choices:
                return resp
            else:
                print('Return a valid spell or ability')

    def yield_choice(self):
        return self.input_choice("Select", self.book.keys())

    # calculate damage recieved
    def rec_damage(self, amount, attacker):
        self.hp -= amount
        self.damage_received += amount
        attacker.damage_dealt += amount
        # to do: add in armor/defense/evasion/ect
        return amount

    # used to restore hp
    def hp_potion(self):
        self.hp = self.fullhp