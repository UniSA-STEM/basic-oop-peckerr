"""
File: Main.py
Description: Module used to test Asset.py, Rig.py, and Hacker.py
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Import classes
from Hacker import Hacker
from Rig import Rig
from Asset import Asset

def edge_cases():
    print('\n--------------------------------- Welcome to my OOP Basic Programming Assignment ---------------------------------')
    print('This function will run through various tests, focusing on edge cases and error handling as listed in assignment PDF.')

    print('\nTest 1: Initialise hacker, upgrade without a rig.')
    hacker1 = Hacker('Joe Blogs')
    hacker1.inventory.append(Asset.hardware_patch)  # Give hacker required item
    print(hacker1)
    print('\nThere will now be an error in upgrading due to no rig.\n')
    hacker1.upgrade_rig()
    print('Test 1 concluded.\n')

    print('\nTest 2: Encrypting without required asset.\n')
    print('This will fail and display an error message.\n')
    hacker1.encrypt_decrypt_asset('Hardware Patch')
    print('Test 2 concluded.\n')

    print('\nTest 3: High trace handling and attacking when exposed.')
    hacker1.get_rig('Jeff')   # I allowed the player to choose their own rig name via input, for testing you can specify name when calling the method.
    defender1 = Hacker('Evil Joe')
    defender1.get_rig('Evil Jeff')
    hacker1.trace_level = 6
    print('Joe Blogs trace level has been set above the trace threshold, any attempt to attack will now fail.\n')
    hacker1.attack(defender1)

edge_cases()

def battle():
    print('\n------------------------------------- Welcome to my OOP Basic Programming Assignment -------------------------------------')
    print('This function will simulate a battle between an attacking and defending hacker/rig. You may decide to extract assets or not.\n')

    print('| ------------------------------------- |')
    print('|        Today\'s combatants:            |')
    print('| Attacking Hacker: FiredUp             |')
    print('| Attacking Rig:    Fire Blaster 6000   |')
    print('| ------------------------------------- |')
    print('| Defending Hacker: Hopeful             |')
    print('| Defending Rig:    No Talent           |')
    print('| ------------------------------------- |')

    attacker = Hacker('FiredUp')
    defender = Hacker('Hopeful')
    attacker.get_rig('Fire Blaster 6000')
    defender.get_rig('No Talent')

    print('\nTEST 1')
    print('Si')
    attacker.attack(defender)
    defender.attack(attacker)
    attacker.attack(defender)

    print('\nThe defending hacker is now retrieving their rig for repairs, but do they have the resources?\n')
    defender.rig.repair(defender)

battle()
