#!/usr/bin/python3
import os
import sys
import time
import directory as d
import mariadblib as m
import containers as c
import hnyconfig as config


def _split(command):
    return command.solit(" ")

def _buildShort(command):
    if command[1] in c.shortTypeDict.values():
        return m.build(shortTypeDict[command[1]))

def _shortSimpleResolve(command):
    if command[0] == "b":
        return _buildShort(command)

def commandResolve(command):
    if len(command) == 2:
        return _shortSimpleResolve(command)
    if len(_split(command)) == 2:
        return _shortSimpleResolve(_split(command))




