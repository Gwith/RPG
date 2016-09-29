from RPG.classes.rogue import Rogue
from RPG.classes.warrior import Warrior
from RPG.classes.wizard import Wizard
import sys
import time

def statistics(character):
    '''View character stats'''
    print('\n+-+-+Character Statistics+-+-+')
    print('Character Name: {}, Class: {}'.format(character.name, character.class_type))
    print('Health: {}'.format(character.hp))
    if isinstance(character, Wizard):
        print('Mana: {}'.format(character.mana))
    elif isinstance(character, Warrior):
        print('Rage: {}'.format(character.rage))
    elif isinstance(character, Rogue):
        print('Energy: {}'.format(character.energy))
    # to do: add in other stats

def class_select_menu(character_name):
    answer = 0

    print('\nSelect a class: ')
    print('1) Wizard')
    print('2) Warrior')
    print('3) Rogue')

    while answer not in (1, 2):
        try:
            answer = int(input('\nSelect your choice: '))
            if answer == 1:
                print('You have selected Wizard!')
                return Wizard(character_name)
            elif answer == 2:
                print('You have selected Warrior!')
                return Warrior(character_name)
            elif answer == 3:
                print('You have selected Rogue!')
                return Rogue(character_name)
        except ValueError:
            print('Return a valid answer (1 or 2)')

def statistics_menu(character):
    answer = 0
    print('\n1) Start battle.')
    print('2) Show character statistics.')
    print('3) Show character abilities.')
    print('3) Quit')

    while answer not in (1, 2, 3, 4):
        try:
            answer = int(input('\nSelect your choice: '))
            if answer == 1:  # print ouput and move on to next part of program
                print('\nYour battle begins.\n')
            elif answer == 2:  # show character statistics
                statistics(character)
                time.sleep(2)
                statistics_menu(character)
            elif answer == 3:  # show character abilities/spells
                # list character spells/abilities
                print('\n'.join('{}{}'.format(key, val) for key, val in character.book.items()))
                # to do: make menu cleaner
                time.sleep(2)
                statistics_menu(character)
            elif answer == 4:  # exit program
                sys.exit()
        except ValueError:
            print('Return a valid answer (1, 2, or 3)')

def battle_menu(character):
    answer = 0
    print('1) Attack')
    print('2) HP Potion')
    print('3) Mana Potion')

    while answer not in (1, 2, 3):
        try:
            answer = int(input('\nSelect your choice: '))
            if answer == 1:
                return
            elif answer == 2:
                character.hp = character.fullhp
                print('You gulp down a HP potion.')
            elif answer == 3:
                character.mana = character.fullmana
                print('You gulp down a Mana potion.')
        except ValueError:
            print('return (1, 2, or 3)')

def game_end_menu(player, enemy):
    answer = 0
    print('\n1) Play again')
    print('2) Show battle statistics.')
    print('3) Quit')

    while answer not in (1, 2, 3):
        try:
            answer = int(input('\nSelect your choice: '))
            if answer == 1:  # restart game
                break
            elif answer == 2:  # show character and enemy damage and damage received
                print(player.name)
                print('Damage Dealt: {}'.format(player.damage_dealt))
                print('Damage Received: {}\n'.format(player.damage_received))

                print(enemy.name)
                print('Damage Dealt: {}'.format(enemy.damage_dealt))
                print('Damage Received: {}'.format(enemy.damage_received))
            elif answer == 3:  # exit program
                sys.exit()
        except ValueError:
            print('Return a valid answer (1, 2, or 3)')