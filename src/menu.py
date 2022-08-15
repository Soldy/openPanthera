#!/usr/bin/python3

import os, sys
import openpanthera.directory as d
import mariadblib as m


def menuWrite():
    print('===============================')
    print('di Init Directory')
    print('dc Check Directory')
    print('df Fix or Update Directory')
    print('ch check migration')
    print('mi init migration table')
    print('bt build tables')
    print('bf build functionss')
    print('a  auto mode')
    print('e  exit')

def menuDo():
    command = input(' {OP} >> ')
    if command == 'e' :
        quit()
    elif command == 'di' :
        d.init()
        print('directory structure initilazed')
    elif command == 'dc' :
        d.check()
    elif command == 'bt' :
        d.check()
        m.buildTable()
    elif command == 'bf' :
        d.check()
        m.buildFunction()
    elif command == 'mi' :
        m.initMigrationTable()
        print('migration table initalized')

def menu():
    while True:
        menuWrite()
        menuDo()

menu()
