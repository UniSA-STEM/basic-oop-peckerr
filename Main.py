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
from Rig import Rig
from Asset import Asset


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
# def test3():
#     attacker = Hacker('Phil')
#     attacker.get_rig()
#
#     attacker.inventory.append(Asset('Hardware Patch','- Used to upgrade rigs.')) #Gives player item
#
#     print('\nBefore upgrade:')
#     print('\n'.join(str(asset) for asset in attacker.inventory))
#     print('Upgrade Level:', attacker.rig.upgrade_level)
#
#     attacker.upgrade_rig()
#
#     print('\nAfter upgrade:')
#     print('\n'.join(str(asset) for asset in attacker.inventory))
#     print('Upgrade Level:', attacker.rig.upgrade_level)
# test3()

# TEST 4: Encryption and storage testing
# def test4():
#     attacker = Hacker('Hacker')
#     attacker.get_rig(rig_name= 'Hack222')
#
#     attacker.inventory.append(Asset.security_chip) #add items to inv for testing
#     attacker.inventory.append(Asset.data_spike)
#
#     print(attacker) # Hacker should have a rig, and two items.
#
#     attacker.encrypt_decrypt_asset('Data Spike') #(Encrypt the data spike asset that is now in attacker inventory)
#
#     print(attacker) # Hacker should have a rig, and only an encrypted data spike
#     print(attacker.rig) # Rig should only have default items
#
#     attacker.store_asset('Data Spike') #Attempt to store newly encrypted asset (SHOULD FAIL AND RETURN A MESSAGE)
#
#     print(attacker) # Nothing should change for both rig/hacker
#     print(attacker.rig)
# test4()

# TEST 5: Upgrade levels, influencing damage taken
def test5():
    attacker = Hacker('Attacker')
    defender = Hacker('Defender')

    attacker.get_rig('Attacker Rig')
    defender.get_rig('Defender Rig')

    print(defender.rig)

    attacker.attack(defender)
    attacker.attack(defender) # Should break the rig (lvl 0 has 2 hp)

    print(defender.rig) # Shows broken rig values

    attacker.attack(defender)  # Will not attack as target is broken

    defender.rig.repair(defender) # Cannot repair as defender has no token
    defender.inventory.append(Asset.crypto_token)
    defender.rig.repair(defender) # Will repair
    defender.rig.upgrade()
    defender.rig.upgrade() # Upgrade x2
    print(defender.rig) # Will display rig is now repaired and is upgraded x2

    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.rig.storage.append(Asset.data_spike)
    attacker.inventory.append(Asset.removable_drive) # Give attacker means to break defender and extract

    attacker.attack(defender)
    attacker.attack(defender)
    attacker.attack(defender)
    print(attacker)
    print(defender.rig)
    attacker.attack(defender)

    print(attacker)


test5()
