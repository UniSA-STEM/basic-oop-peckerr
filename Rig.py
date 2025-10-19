"""
File: Rig.py
Description: A class that represents a rig object, containing name,
            damage counters, broken state, and storage for assets (class contained in asset.py).
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Import needed classes
from Asset import Asset
import random          # Needed to generate asset randomly (easily)

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage_counter = 0
        self.broken_state = False
        self.upgrade_level = 0
        self.storage = [
            Asset('Data Spike', 'Used in battles'),
            Asset('Data Spike', 'Used in battles'),
            Asset('Removable Drive', 'Found in rigs and used for extraction')
        ]

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

    def broken(self):
        max_hp = 2 + self.upgrade_level
        if self.damage_counter >= max_hp:
            self.broken_state = True
            print(f'{self.name} has been broken.')
        return self.broken_state

    def condition(self):
        if self.broken_state:
            return f'Broken (Level {self.upgrade_level})'
        else:
            return f'Pristine (Level {self.upgrade_level})'

    def generate_asset(self):
        asset_list = [
            ('Data Spike', '- Used in battles.'),
            ('Crypto Token', '-  to acquire or repair rigs.'),
            ('Removable Drive', '- Found in rigs and used for extraction.'),
            ('Security Chip', '- Used to encrypt of decrypt assets.'),
            ('Hardware Patch', '- Used to upgrade rigs.')
        ]

        choice = random.choice(asset_list)
        generated_asset = Asset(choice[0], choice[1])
        self.storage.append(generated_asset)
        print('\nGenerating asset... 0%'
              '\nGenerating asset... 13%'
              '\nGenerating asset... 21%'
              '\nGenerating asset... 40%'
              '\nGenerating asset... 78%'
              '\nGenerating asset... 100%')
        print(f'\n{generated_asset.name} has been generated.')
        return generated_asset

    def __str__(self):
        if self.storage:
            rig_inv = '\n'.join(str(asset) for asset in self.storage)
        else:
            rig_inv = 'No assets.'
        return (f'----------\n'
                f'Rig Name: {self.name}\n'
                f'Condition: {self.condition()}\n'
                f'Upgrade Level: {self.upgrade_level}\n'
                f'Assets: {rig_inv}\n'
                f'---------')
