#!/usr/bin/python3
import os
import sys
import time
import containers as c
import display as ui
import hnyconfig as config
import schema as s
import modules as m

config.init('mariadb.conf.json')
schemas_list = m.read()



_schema = s.VirtualSchema('', ui)

_shorters = c.short_specific_commands


def _shortResolve(command:str):
    if command[0] in c.short_commands.keys():
        main = c.short_commands[command[0]]
        if command[1] in _shorters[main].keys():
           sub = _shorters[main][command[1]]
           return _schema.resolv(main, sub)

def _split(command:str)->list:
    if len(command) > 2:
        return command.split(" ")
    return command

def resolve(command:str):
    if command == 'h' or command == "help":
        return help()
    clean_command = _split(command)
    if clean_command[0] == 'x' and clean_command[1] == 'x':
        clean_command = 'bx'
    if len(clean_command) == 2:
        return _shortResolve(clean_command)

def help()->int:
    out = ''
    for command in c.short_commands.keys():
        for specific in _shorters[c.short_commands[command]].keys():
            out += (
                command+
                specific+
                ' '+
                c.short_commands[command]+
                ' '+
                c.short_specific_commands[c.short_commands[command]][specific]+
                '\n'
            )
    ui.log(out)
    return 0
