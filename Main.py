"""
File: Main.py
Description: Module used to test Asset.py, Rig.py, and Hacker.py
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

'''
Please scroll to bottom of this file and instantiate either 'edge_cases()', 'battle()', or 'encrypt_test()' by commenting in or out as you wish.
Feel free test more cases.
'''


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

    print('\n== TEST 1 ==')
    attacker.attack(defender)
    defender.attack(attacker)
    attacker.attack(defender)

    print('\n== The defending hacker is now retrieving their rig for repairs, but do they have the resources? ==\n')
    defender.rig.repair(defender)
    print('\n== Let\'s give the defender a hand (A CryptoToken). ==')
    defender.rig.storage.append(Asset.crypto_token)
    defender.rig.repair(defender)
    print('\n== Oh no! We gave the asset to the rig and not the hacker, they better retrieve it to perform repairs. ==\n')
    defender.retrieve_asset('CryptoToken')
    defender.rig.repair(defender)
    defender.inventory.append(Asset.hardware_patch)   # Comment this out to test upgrading without asset.
    print('\n== It seems the defender found a Hardware Patch while retrieving their rig, they should upgrade. ==')
    defender.upgrade_rig()
    print(f'\n== Great job {defender.name}, you repaired and upgraded your rig: {defender.rig.name}. ==')
    print('\n== Let\'s see how the rest of the battle plays out. ==')

    attacker.inventory.append(Asset.removable_drive)
    attacker.inventory.append(Asset.hardware_patch)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)

    print('== Oh no, the attacker has a brilliant vantage point and has ambushed the defender. ==')
    defender.rig.upgrade_level = 5
    attacker.attack(defender)
    attacker.attack(defender)
    attacker.attack(defender)
    attacker.attack(defender)
    attacker.attack(defender)

    print(f'\n== {attacker.name} managed to get some good attacks off, but now they\'re exposed! ==')
    print('== They better find a safe spot to run some diagnostics... ==')
    attacker.rig.generate_asset(attacker)
    attacker.upgrade_rig()
    print('\n== That was quick! And they managed to upgrade and generate an extra asset wow! ==')
    attacker.attack(defender)

    print(f'\n== And the winner is... {attacker.name} with their rig {attacker.rig.name}! ==')
    print('== Let\'s see what they ended up looking like')

    print(attacker)
    print(attacker.rig)

    print(defender)
    print(defender.rig)

def encrypt_test():
    hacker = Hacker('Joe Blogs')
    hacker.get_rig('Evil Jeff')
    hacker.inventory.append(Asset.security_chip)
    hacker.inventory.append(Asset.security_chip)

    print(hacker)
    print(hacker.rig)

    hacker.retrieve_asset('Data Spike')

    print(hacker)
    print(hacker.rig)

    hacker.encrypt_decrypt_asset('Data Spike')
    hacker.store_asset('Data Spike')
    print(hacker)
    hacker.encrypt_decrypt_asset('Data Spike')
    hacker.store_asset('Data Spike')

    print(hacker)
    print(hacker.rig)

########################## TESTS HERE ################################
#edge_cases()
#encrypt_test()
#battle()