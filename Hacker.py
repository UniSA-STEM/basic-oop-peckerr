"""
File: Hacker.py
Description: A class that represents a hacker (user/player), containing name,
            inventory, rig, and trace level. Methods for using rigs, attacking, encrypting, upgrading, transferring.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self, name):
        self.name = name
        self.inventory = ['CryptoToken']
        self.rig = False
        self.trace_level = 0

    def get_rig(self):
        for asset in self.inventory:
            if assets.name == 'CryptoToken':
                self.rig = True
                self.inventory.remove(asset)
                print(f'{self.name} activated a rig.')
                return
        print('You are broke buddy, no sweet sweet rig for you.')   # Change this to be professional :)

    def attack(self, target):
        for asset in self.rig.storage:
            if asset.name == 'Data Spike':
                target.damage_counter += 1
                if target.broken_state:
                    print('insert asset extraction method here')     # METHOD NOT IMPLEMENTED
                self.rig.storage.remove(asset)
                print(f'{self.name} launched a data spike at {target.name}')
                return
        print('You need a \'Data Spike\' to launch an attack.')

    def encrypt_decrypt_asset(self, item):
        for asset in self.inventory:
            if asset.name == 'Security Chip':
                if item.encrypted:
                    item.encrypted = False
                    print(f'{item.name} has been decrypted.')
                elif not item.encrypted:
                    item.encrypted = True
                    print(f'{item.name} has been encrypted.')
                return

    def upgrade_rig(self):
        for asset in self.inventory:
            if asset.name == 'Hardware Patch' and self.rig:
                rig.upgrade_level += 1
                self.inventory.remove(asset)
                print(f'{self.name} upgraded their rig.')
                return
            print('You need a \'Hardware Patch\' to upgrade your rig.')

    def store_asset(self, asset_name = None):
        if not self.rig:                                            # Validation
            print('You need a rig to store things in first choom')
            return
        if asset_name:
            for asset in self.inventory:
                if asset == asset_name:
                    self.rig.storage.append(asset) #Clone item to Rig class storage list
                    self.inventory.remove(asset)
                    print(f'{asset_name} is now stored in the rig.')
                    return
            print(f'You actually need to own a {asset_name} to store it bucko.') # make appropriate
        else:
            for asset in self.inventory:          # For loop iterates over inventory and adds copy to rig storage, then removes from inventory
                self.rig.storage.append(asset)
                self.inventory.remove(asset)
            print('All assets are now in rig storage.')

    def retrieve_asset(self, asset_name = None):
        if not self.rig:
            print('You need a rig to retrieve things in first choom')
            return
        if asset_name:
            for asset in self.inventory:
                if asset == asset_name:
                    self.inventory.append(asset)
                    self.rig.storage.remove(asset)
                    print(f'{asset_name} has been retrieved from the rig.')
            print(f'You actually need to own a {asset_name} to retrieve it bucko.')
        else:
            for asset in self.rig.storage:
                self.inventory.append(asset)
                self.rig.storage.remove(asset)
            print('All assets are now in inventory.')

    def scan_inventory(self, asset_name):
        for asset in self.inventory:
            if asset == asset_name:
                self.inventory.remove(asset)
                print(f'{asset_name} removed from inventory, don\'t know why you did that things aren\'t free :)')
                return asset # Instructions unclear, is this what was meant by 'return and remove'?
            print(f'You do not own {asset_name}')
            return None # see above comment?

















