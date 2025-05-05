#!/usr/bin/python3
"""
cli menu
"""
from openPanthera import commander

def menu():
    """
    menu fuction
    """
    print(commander.help())
    while True:
        command = input(' {OP} >> ')
        commander.resolve(command)

menu()
