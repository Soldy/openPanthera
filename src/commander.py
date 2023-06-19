#!/usr/bin/python3
import os
import sys
import time
import directory as d
import mariadblib as m
import containers as c
import hnyconfig as config


def _split(command):
    if len(command) > 2:
        return command.split(" ")
    return command

def _buildShort(command):
    if command[1] in c.short_types.values():
        return m.build(c.short_types[command[1]])

def _directoryShort(command):
    if command[1] in c.short_types.values():
        return m.build(c.short_types[command[1]])

def _shortSimpleResolve(command):
    if command[0] == 'b':
        return _buildShort(command)
    if command[0] == 'd':
        return _buildShort(command)

def commandResolve(command):
    clean_command = _split(command)
    if len(clean_command) == 2:
        return _shortSimpleResolve(clean_command)


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
