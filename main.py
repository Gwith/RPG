from RPG.menus.game_menus import class_select_menu
from RPG.menus.game_menus import statistics_menu
from RPG.menus.game_menus import battle_menu
from RPG.menus.game_menus import game_end_menu

from RPG.classes.goblin_boss import Goblin_Boss

from RPG.combat.combat_dependencies import attacking
from RPG.combat.combat import combat

def main():
    print('Welcome to Gwith\'s RPG')
    character_name = input('What is your character name? ')
    character = class_select_menu(character_name) # contains player name and attributes
    enemy_boss = Goblin_Boss() # contains boss attributes

    statistics_menu(character)
    combatround = 1
    while character.hp > 0 and enemy_boss.hp > 0: # combat till one character dies
        battle_menu(character)
        print('\n+-+-+ Combatround {} +-+-+\n'.format(combatround))
        combatround += 1
        attacker, defender = attacking(character, enemy_boss) # return randomly selected attacker, defender
        combat(attacker, defender) # run combat function with randomly selected attacker, defender
    game_end_menu(character, enemy_boss)

if __name__ == "__main__":
        main()

