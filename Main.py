"""
File: Main.py
Description: Module used to test Asset.py, Rig.py, and Hacker.py
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# NEED TO DO LIST
# Rig generate assets
# Expand on trace level, action blocking, exposing etc
# Rig upgrade storage size (?)
# Rig upgrade damage and tankiness
# rig condition logic is wrong, it needs to check both upgrade lvl and damage(wear and tear)

# Import classes
from Hacker import Hacker

# def main():
#     #hacker = Hacker(input('Enter your elite hacker name: '))
#     attacker = Hacker('Phil')
#     defender = Hacker('Bad Phil')
#     print(attacker)
#
#     attacker.get_rig()
#     defender.get_rig(rig_name = 'Bad Phil\'s Bad Rig')
#
#     attacker.attack(defender)
#     attacker.attack(defender)
#     attacker.attack(defender)
#
#     print(attacker)
#     attacker.store_asset()
#     print(attacker.rig)
#     print(attacker)
#
#     attacker.retrieve_asset('Removable Drive')
#     print(attacker)
#
#     print(attacker.rig)
#     attacker.rig.generate_asset()
#     print(attacker.rig)

# def extract_test():
#     attacker = Hacker('Phil')
#     defender = Hacker('Bad Phil')
#
#     print(attacker)
#
#     attacker.get_rig()
#     defender.get_rig(rig_name='Bad Phil\'s Bad Rig')
#
#     attacker.attack(defender)
#     print(attacker)
#     attacker.attack(defender)
#
#
#     #attacker.extract_asset(defender.rig)
#     print(attacker)

#extract_test()
#main()

# TESTING

# TEST 1: Initialise hacker and display inventory
# def test1():
#     attacker = Hacker('Phil')
#     print(attacker)
# test1() # Success

# TEST 2: Get rig, display hacker and rig inventory
# def test2():
#     attacker = Hacker('Phil')
#     attacker.get_rig()
#     print(attacker)
#     print(attacker.rig)
# test2()

# TEST 3: Upgrade testing - consume asset and influence upgrade level
def test3():
    attacker = Hacker('Phil')
    attacker.get_rig()

    attacker.inventory.append(Asset('Hardware Patch')) #Gives player item

    print('Before upgrade:')
    print(attacker.rig)

    attacker.upgrade_rig()

    print('After upgrade:')
    print(attacker.rig)
test3()

