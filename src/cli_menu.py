#!/usr/bin/python3
import commander


def menu():
    print(commander.helpOut())
    while True:
        command = input(' {OP} >> ')
        commandResolve(command)

menu()
