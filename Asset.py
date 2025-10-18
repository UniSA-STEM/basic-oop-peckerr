"""
File: Asset.py
Description: A class that represents an asset, to be moved, consumed, or used in various actions taken via other .py files.
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False              # Base state assets are not encrypted

    def encrypt(self):
        self.encrypted = True

    def decrypt(self):
        self.encrypted = False

    def __str__(self):
        if self.encrypted:
            return f'{self.name} {self.description} [Encrypted]'
        else:
            return f'{self.name} {self.description}'


#ASSET LIST
# CryptoToken: Used to acquire or repair rigs. (H)
# Data Spike: Used in battles. (R)
# Removable Drive: Found in rigs and used for extraction. (R)
# Security Chip: Used to encrypt or decrypt assets. (H or R)
# Hardware Patch: Used to upgrade rigs. (H)