#!/usr/bin/python3
import openPanthera.commander as commander


def menu():
    print(commander.help())
    while True:
        command = input(' {OP} >> ')
        commander.resolve(command)

menu()
