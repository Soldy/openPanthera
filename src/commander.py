#!/usr/bin/python3
import os
import sys
import time
import display as ui
import migrate as e
import hnyconfig as config
import VitrualSchema from schema as virtual

config.init('mariadb.conf.json')

shcema = virtual('', ui)

_resolvers = {
    'migrate'  : schema.migrate.resolv,
    'build'    : schema.mariadb.build,
    'directory': schema.directory.resolv
}

_shorters = short_specific_commands = {
    'migrate'  : c.short_migrate_commands,
    'build'    : c.short_types,
    'directory': c.short_directory_commands
}

def _shortResolve(command):
    if command[0] in c.short_commands.keys():
        main = c.short_commands[command[0]]
        if command[1] in _shorters[main].keys():
           sub = _shorters[main][command[1]]
           return _resolvers[main](sub)

def _split(command):
    if len(command) > 2:
        return command.split(" ")
    return command

def resolve(command):
    if command == 'h' or command == "help":
        return help()
    clean_command = _split(command)
    if len(clean_command) == 2:
        return _shortResolve(clean_command)

def help()->int:
    out = ''
    for command in c.short_commands.keys():
        for specific in c.short_specific_commands[command].keys():
            out += (
                command+
                specific+
                ' '+
                c.short_commands[command]+
                ' '+
                c.short_specific_commands[command][specific]+
                '\n'
            )
    ui.log(out)
    return 0
