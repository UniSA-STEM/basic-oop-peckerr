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
        self.storage_cap = 5
        self.storage = [
            Asset('Data Spike', '- Used in battles'),
            Asset('Data Spike', '- Used in battles'),
            Asset('Removable Drive', '- Found in rigs and used for extraction')]

    def take_hit(self, damage=1):
        self.damage_counter += damage
        self.broken()

    def repair(self, hacker):
        for asset in hacker.inventory:
            if asset.name == 'CryptoToken':
                if self.damage_counter > 0:
                    self.damage_counter = 0
                    self.broken_state = False
                    print(f'{self.name} has been repaired.')
                    hacker.inventory.remove(asset)
                else:
                    print('No repair is needed.')
                return
        print('Could not repair - No CryptoToken asset.')

    def upgrade(self, hardware_patch):
        self.upgrade_level += 1
        self.storage_cap += 2
        print(f'{self.name} has been upgraded to level: {self.upgrade_level}.')

    def storage_lvl(self, asset_amount=1):
        return len(self.storage) + asset_amount <= self.storage_cap

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

    def generate_asset(self, hacker):
        asset_list = [
            ('Data Spike', '- Used in battles.'),
            ('CryptoToken', '-  to acquire or repair rigs.'),
            ('Removable Drive', '- Found in rigs and used for extraction.'),
            ('Security Chip', '- Used to encrypt or decrypt assets.'),
            ('Hardware Patch', '- Used to upgrade rigs.')
        ]

        choice = random.choice(asset_list)
        generated_asset = Asset(choice[0], choice[1])
        self.storage.append(generated_asset)
        print('\nGenerating asset... 0%')
        print('Generating asset... 13%')
        print('Generating asset... 21%')
        print('Generating asset... 40%')
        print('Generating asset... 78%')
        print('Generating asset... 100%')
        print(f'\n{generated_asset.name} has been generated.')
        hacker.reduce_trace()
        return generated_asset

    def __str__(self):
        if self.storage:
            rig_inv = '\n'.join(str(asset) for asset in self.storage)
        else:
            rig_inv = 'No assets.'
        return (f'\n----- Rig Information -----\n'
                f'Rig Name: {self.name}\n'
                f'Condition: {self.condition()}\n'
                f'Upgrade Level: {self.upgrade_level}\n'
                f'Storage: {rig_inv}\n'
                f'---------------------------')
