"""
File: Rig.py
Description: A class that represents a rig object, containing name,
            damage counters, broken state, and storage for assets (class contained in asset.py).
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage_counter = 0
        self.broken_state = False
        self.storage = []
        self.upgrade_level = 0

    def repair(self, crypto_token):
        if self.damage_counter > 0:
            self.damage_counter = 0
            self.broken_state = False
            print(f'{self.name} has been repaired.')
        else:
            print('No repair is needed.')

    def upgrade(self, hardware_patch):
        self.upgrade_level += 1
        print(f'{self.name} has been upgraded to {self.upgrade_level}.')

    def take_damage(self):
        self.damage_counter += 1
        if self.upgrade_level = 0 and self.damage_counter >= 2:
            self.broken_state = True
            print(f'{self.name} has been broken.')

    def condition(self):
        if self.broken_state:
            print(f'{self.name} condition is: Broken (Level 0)')
        else:
            print(f'{self.name} condition is: Pristine (Level {self.upgrade_level})')


