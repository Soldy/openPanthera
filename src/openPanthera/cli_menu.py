#!/usr/bin/python3
import openPanthera.commander as commander


def menu():
    print(commander.helpOut())
    while True:
        command = input(' {OP} >> ')
        commandResolve(command)

menu()
