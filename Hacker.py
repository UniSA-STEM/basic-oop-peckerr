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
                    print('insert asset extraction method here')
                self.rig.storage.remove(asset)
                print(f'{self.name} launched a data spike at {target.name}')
                return
        print('You need a \'Data Spike\' to launch an attack.')

    def encrypt_asset(self, item):
        for asset in self.inventory:
            if asset.name == 'Security Chip':
                item.encrypted = True
                print(f'{item.name} has been encrypted.')









