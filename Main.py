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

def main():
    #hacker = Hacker(input('Enter your elite hacker name: '))
    attacker = Hacker('Phil')
    defender = Hacker('Bad Phil')
    print(attacker)

    attacker.get_rig()
    defender.get_rig(rig_name = 'Bad Phil\'s Bad Rig')

    attacker.attack(defender)
    attacker.attack(defender)
    #attacker.attack(defender)






main()