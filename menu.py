#!/usr/bin/python3

import os, sys
import directory as d


def menuWrite():
    print('di Init Directory')
    print('dc Check Directory')
    print('df Fix or Update Directory')
    print('ch check migration')
    print('a  auto mode')
    print('e  exit')

def menuDo():
    command = input(' {OP} >> ')
    if command == 'e' :
        quit()
    if command == 'di' :
        d.init()
        print('directory structure initilazed')

def menu():
    while True:
        menuWrite()
        menuDo()

menu()
