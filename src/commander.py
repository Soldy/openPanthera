#!/usr/bin/python3
import os
import sys
import time
import display as ui
import directory as d
import mariadblib as m
import containers as c
import migrate as e
import hnyconfig as config


config.init('mariadb.conf.json')

d.display(ui)
defaultDirectory = d.DirectoryClass('')

e.display(ui)
defaultMariaDb = m.MariaDbClass(ui, config, defaultDirectory)
defaultMigrate = e.MigrateClass(defaultMariaDb, defaultDirectory)

_resolvers = {
    'migrate'  : defaultMigrate.resolv,
    'build'    : defaultMariaDb.build,
    'directory': defaultDirectory.resolv
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
        return helpOut()
    clean_command = _split(command)
    if len(clean_command) == 2:
        return _shortResolve(clean_command)


def helpOut():
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
    return out
