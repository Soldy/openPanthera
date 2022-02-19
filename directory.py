#!/usr/bin/python3
import os


_migrationTypeList = [
    '10-table',
    '15-table-link',
    '20-function',
    '30-procedure',
    '40-view',
    '50-index',
    '60-forein',
    '70-migration',
    '60-seed',
    '90-event',
    '95-admin'
]


def init():
    os.mkdir('panthera')
    for i in _migrationTypeList:
        os.mkdir('panthera/'+i)


def check():
    if os.path.isdir('panthera') == False:
        return print('Directory is missing')
    for i in _migrationTypeList:
        if os.path.isdir('panthera/'+i) == False:
           return print('Directory is not complet')
    print('Directory Structure is healthy')

def fix():
    if os.path.isdir('panthera') == False:
        os.mkdir('panthera')
    for i in _migrationTypeList:
        if os.path.isdir('panthera/'+i) == False:
           os.mkdir('panthera/'+i)
    print('Directory structure is fixed')

def _reader(target):
    out = []
    target_path = ('panthera/'+target)
    if os.path.isdir('panthera') == False:
       return print('Directory is missing')
    for i in os.listdir(target_path):
        if os.path.isfile(target_path+i):
           with open(target_path+i) as f:
               out.appent(f.read())
    return out

def readTable():
    return _reader(_migrationTypeList[0])

def readTableLink():
    return _reader(_migrationTypeList[1])

def readFunction():
    return _reader(_migrationTypeList[2])

def readProcedure():
    return _reader(_migrationTypeList[3])

def readView():
    return _reader(_migrationTypeList[4])

def readIndex():
    return _reader(_migrationTypeList[5])

def readForein():
    return _reader(_migrationTypeList[6])

def readMigration():
    return _reader(_migrationTypeList[7])

def readSeed():
    return _reader(_migrationtypelist[8])

def readEvent():
    return _reader(_migrationtypelist[9])

def readAdmin():
    return _reader(_migrationtypelist[10])

