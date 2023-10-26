#!/usr/bin/python3

import os, sys
import directory as d
import mariadblib as m
import hnyconfig as config


def menuWrite():
    print('===============================')
    print(config.get('name'))
    print('===============================')
    print('di Init Directory')
    print('dc Check Directory')
    print('df Fix or Update Directory')
    print('ch check migration')
    print('mi init migration table')
    print('bt build tables')
    print('bl build link tables')
    print('bf build functions')
    print('bp build procedures')
    print('bv build views')
    print('xx destroy att tables')
    print('h  help')
    print('e  exit')

def menuDo():
    command = input(' {OP} >> ')
    if command == 'e' or command == 'q':
        quit()
    elif command == 'h' or command == '?' or command == 'help':
        menuWrite()
    elif command == 'di' :
        d.init()
        print('Directory structure initilazed')
    elif command == 'df' :
        if d.fix() == True:
            print('Directory structure initilazed')
        else:
            print('Directory structure is fixed')
    elif command == 'dc' :
       check_result = d.check()
       if check_result == 0:
           print('Directory Structure is healthy')
       elif check_result == 1:
           print('Directory is missing')
       else:
           print('Directory Structure is healthy')
    elif command == 'bt' :
        d.check()
        m.buildTable()
    elif command == 'bl' :
        d.check()
        m.buildTableLink()
    elif command == 'bf' :
        d.check()
        m.buildFunction()
    elif command == 'bp' :
        d.check()
        m.buildProcedure()
    elif command == 'bv' :
        d.check()
        m.buildView()
    elif command == 'xx' :
        d.check()
        m.destroy()
    elif command == 'mi' :
        m.initMigrationTable()
        print('Migration table initalized')
    else :
        print("Unknown command")

def menu():
    menuWrite()
    while True:
        menuDo()

menu()
