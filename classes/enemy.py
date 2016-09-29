import random

class Enemy:
    '''Create common creature class'''
    def __init__(self):
        self.hp = 100
        self.fullhp = self.hp
        self.damage_dealt = 0
        self.damage_received = 0
        # to do: add other stats