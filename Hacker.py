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
    TRACE_THRESHOLD = 5 # constant for trace level checks

    def __init__(self, name):
        self.name = name
        self.inventory = [Asset('CryptoToken', 'Used to acquire or repair rigs.')]
        self.rig = None
        self.trace_level = 0

    def exposed(self):
        return self.trace_level > self.TRACE_THRESHOLD # returns true if trace level exceeds threshold -> hacker is exposed

    def reduce_trace(self):
        self.trace_level = max(0, self.trace_level - 1)
        print(f'Trace level reduced \n'
              f'New trace level: {self.trace_level}\n')

    def get_rig(self):
        for asset in self.inventory:
            if assets.name == 'CryptoToken':
                self.rig = Rig('BigDawg v2')              # placeholder name, maybe let user choose via input
                self.inventory.remove(asset)
                print(f'{self.name} activated rig: {self.rig.name}.')
                return
        print('You are broke buddy, no sweet sweet rig for you.')   # Change this to be professional :)

    def attack(self, target):
        if self.exposed():
            print('You are exposed. Reduce trace level to attack')
            return
        for asset in self.rig.storage:
            if asset.name == 'Data Spike':
                target.damage_counter += 1
                if target.broken_state:
                    print('insert asset extraction method here')     # METHOD NOT IMPLEMENTED
                    reduce_trace()                                   # Potentially unwise to have that here, locked behind attacking - which is blocked if exposed
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
            self.rig.storage.extend(self.inventory)
            self.inventory.clear()
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

    def __str__(self):
        return (f'Hacker: {self.name}\n'
                f'Rig Name: {self.rig.name}\n'
                f'Trace Level: {self.trace_level}\n'
                f'Inventory: {self.inventory}\n')



