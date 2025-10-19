"""
File: Hacker.py
Description: A class that represents a hacker (user/player), containing name,
            inventory, rig, and trace level. Methods for using rigs, attacking, encrypting, upgrading, transferring.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Import needed classes
from Asset import Asset
from Rig import Rig

class Hacker:
    TRACE_THRESHOLD = 5 # constant for trace level checks

    def __init__(self, name):
        self.name = name
        self.inventory = [Asset('CryptoToken', '- Used to acquire or repair rigs.')]
        self.rig = None
        self.trace_level = 0

    def exposed(self):
        return self.trace_level > self.TRACE_THRESHOLD # returns true if trace level exceeds threshold -> hacker is exposed

    def reduce_trace(self):
        self.trace_level = max(0, (self.trace_level - 1))
        print(f'Trace level reduced to {self.trace_level}')

    def get_rig(self, rig_name=None):
        for asset in self.inventory:
            if asset.name == 'CryptoToken':
                if rig_name is not None:
                    self.rig = Rig(rig_name)
                else:
                    self.rig = Rig(input(f'\n{self.name} has purchased a rig!'
                                         f'\nWhat should {self.name} name the rig? '))
                    print(f'{self.name} activated rig: {self.rig.name}.')
                self.inventory.remove(asset)
                return
        print('You are broke buddy, no sweet sweet rig for you.')   # Change this to be professional :)

    def attack(self, target):
        if self.exposed():
            print('You are exposed. Reduce trace level to attack')
            return
        if not target.rig.broken_state:
            for asset in self.rig.storage:
                if asset.name == 'Data Spike':
                    print(f'\n{self.name} launched a data spike at {target.name}\'s rig {target.rig.name}.')
                    self.trace_level += 1
                    print(f'Trace level increased to {self.trace_level}\n')
                    target.rig.damage_counter += 1
                    target.rig.broken()
                    if target.rig.broken_state:
                        self.reduce_trace()                                   # Potentially unwise to have that here, locked behind attacking - which is blocked if exposed
                        extract_check = input('Do you want to extract assets? (y/n) ')
                        if extract_check == 'y' or extract_check == 'Y':
                            self.extract_asset(target.rig)
                    self.rig.storage.remove(asset)
                    return
        print('You need a \'Data Spike\' to launch an attack.')

    def extract_asset(self, target):
        removable_drive = None
        for asset in self.inventory:                            # Checks if hacker has removable drive in inv, if so attributes it to obj
            if asset.name == 'Removable Drive':
                removable_drive = asset
                break

        if not removable_drive:
            print('You need a Removable Drive to extract assets.')
            return

        assets_extracted = 0
        for asset in target.storage:
            if not asset.encrypted:
                self.inventory.append(asset)
                target.storage.remove(asset)
                assets_extracted += 1
        print(f'Extracted {assets_extracted} asset/s.')
        self.inventory.remove(removable_drive)          # Consumes removable drive asset if successful

    def encrypt_decrypt_asset(self, asset_name):
        item = None                 # Finds asset in inv by name, used for better readability in main.py
        for asset in self.inventory:
            if asset.name == asset_name:
                item = asset
                break

        security_chip = None        # Validation
        for asset in self.inventory:
            if asset.name == 'Security Chip':
                security_chip = asset
                break

        if not security_chip:       # Check if sec chip
            print('You need a Security Chip to encrypt or decrypt assets.')
            return

        if security_chip:           # Main function, de/encrypt asset
            if item.encrypted:
                item.decrypt()
                print(f'\n{item.name} decrypted.')
            else:
                item.encrypt()
                print(f'\n{item.name} encrypted.')
            self.inventory.remove(security_chip)

    def upgrade_rig(self):
        if not self.rig:
            print('You do not own a rig.')
            return

        hardware_patch = None
        for asset in self.inventory:
            if asset.name == 'Hardware Patch':
                hardware_patch = asset          #Sets to true if hacker inventory has needed item
                break

        if hardware_patch:
            self.rig.upgrade(hardware_patch)
            self.inventory.remove(hardware_patch)
        else:
            print('You need a Hardware Patch to upgrade your rig.')

    def store_asset(self, asset_name = None):
        if not self.rig:                                            # Validation
            print('You need a rig to be able to store assets.')
            return

        if asset_name: # Single item transfers
            for asset in self.inventory:
                if asset.name == asset_name:
                    if asset.encrypted:
                        print(f'\n{asset.name} needs to be decrypted before transfer.')
                        return
                    self.rig.storage.append(asset) #Clone item to Rig class storage list
                    self.inventory.remove(asset)
                    print(f'{asset_name} is now stored in the rig.')
                    return
            print(f'No asset named {asset_name} was found in inventory.')
        else:                                               # Transfers all items
            if asset.encrypted:
                print(f'All items needs to be decrypted before transfer.')
                return
            self.rig.storage.extend(self.inventory)
            self.inventory.clear()
            print('\nAll assets are now in rig storage.')

    def retrieve_asset(self, asset_name = None):
        if not self.rig:
            print('You need a rig to retrieve things in first choom')
            return
        if asset_name:
            for asset in self.rig.storage:
                if asset.name == asset_name:
                    self.inventory.append(asset)
                    self.rig.storage.remove(asset)
                    print(f'{asset_name} has been retrieved from the rig.')
            print(f'You actually need to own a {asset_name} to retrieve it bucko.')
        else:
            for asset in self.rig.storage:
                self.inventory.append(asset)
                self.rig.storage.remove(asset)
            print('\nAll assets are now in inventory.')

    def scan_inventory(self, asset_name):
        for asset in self.inventory:
            if asset.name == asset_name:
                self.inventory.remove(asset)
                print(f'{asset_name} removed from inventory.')
                return asset # Instructions unclear, is this what was meant by 'return and remove'?
            print(f'You do not own {asset_name}')
            return None # see above comment?

    def __str__(self):
        rig_name = self.rig.name if self.rig else 'No rig.'
        if self.inventory:
            hacker_inv = '\n'.join(str(asset) for asset in self.inventory) #Had to google this one, converts each inv obj into str, iterates on each asset
        else:
            hacker_inv = 'No assets.'
        return (f'\n----- Hacker Information -----\n'
                f'Hacker: {self.name}\n'
                f'Rig Name: {rig_name}\n'
                f'Trace Level: {self.trace_level}\n'
                f'Inventory: {hacker_inv}\n'
                f'------------------------------')