#!/usr/bin/python3

import os, sys
import directory as d


def menu():
    print('di Init Directory')
    print('dc Check Directory')
    print('df Fix or Update Directory')
    print('ch check migration')
    print('a  auto mode')
    print('e  exit')
    while True:
       command = input(' {OP} >> ')
       if command == 'e' :
           quit()
       if command == 'id' :
           projectInit()

menu()
