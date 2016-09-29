import time
import random

def attacking(a, d):
    '''randomly select attacker and defender from character and boss'''
    attacker = random.choice([a, d])
    if attacker == a:
        return a, d
    else:
        return d, a

def combat(attacker, defender):
    '''combat between attacker and defender'''
    using = attacker.yield_choice() # select ability/spell
    damage = attacker.damage(using)  # calculate damage

    print('{} is attacking!'.format(attacker.name))
    time.sleep(2)
    print('{} did {} damage with {}!'.format(attacker.name, defender.rec_damage(damage, attacker), using))
    print()

    if attacker.hp <= 0 or defender.hp <= 0:
        print('{} has been slain by {}!'.format(defender.name, attacker.name))
        print('Arrrgh, I will be avenged!\n')