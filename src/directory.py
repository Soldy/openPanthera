#!/usr/bin/python3
import os


_migrationTypeList = {
    '10-table'     :{},
    '15-table-link':{},
    '20-function'  :{},
    '30-procedure' :{},
    '40-view'      :{},
    '50-index'     :{},
    '60-forein'    :{},
    '70-migration' :{},
    '80-seed'      :{},
    '90-event'     :{},
    '95-admin'     :{}
}



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
    out = {}
    target_path = ('panthera/'+target)
    if os.path.isdir('panthera') == False:
       return print('Directory is missing')
    for i in os.listdir(target_path):
        if os.path.isfile(target_path+i):
           with open(target_path+i) as f:
               out[i]=str(f.read())
    return out



def readTable():
    name = '10-table'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readTableLink():
    name = '15-table-link'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readFunction():
    _migrationTypeList['20-function'] = _reader('20-function')
    return _migrationTypeList['20-function']

def readProcedure():
    name = '30-procedure'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readView():
    name = '40-view'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readIndex():
    name = '50-index'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readForein():
    name = '60-forein'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readMigration():
    name = '70-migration'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readSeed():
    name = '80-seed'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readEvent():
    name = '90-event'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

def readAdmin():
    name = '95-admin'
    _migrationTypeList[name] = _reader(name)
    return _migrationTypeList[name]

