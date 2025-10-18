"""
File: Main.py
Description: Module used to test Asset.py, Rig.py, and Hacker.py
Author: Thomas Cochrane
ID: 110466784
Username: COCTY007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Import classes
from Hacker import Hacker

def main():
    hacker = Hacker('MrCoolGuy')
    hacker.get_rig()
    print(hacker)
    hacker.store_asset('CryptoToken')
    hacker.attack(hacker.rig)
    hacker.extract_asset(hacker.rig)


main()