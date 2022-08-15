#!/usr/bin/python3
import os,pathlib


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
    if not os.path.exists('panthera'):
        os.mkdir('panthera')
    for i in _migrationTypeList:
        if not os.path.exists('panthera/'+i):
            os.mkdir('panthera/'+i)

def check()->bool:
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

def _reader(target:str)->list:
    out = {}
    target_path = (
        str(pathlib.Path().absolute())+
        '/panthera/'+
        target
    )
    if os.path.isdir('panthera') == False:
       return print('Directory '+target+' is missing')
    for i in os.listdir(target_path):
        if os.path.isfile(target_path+'/'+i):
           with open(target_path+'/'+i) as f:
               out[i]=str(f.read())
    return out

def reader(target:str)->list:
    _migrationTypeList[target] = _reader(target)
    return _migrationTypeList[target]

def readTable()->list:
    return readader('10-table')

def readTableLink()->list:
    return readader('15-table-link')

def readFunction()->list:
    return readader('20-function')

def readProcedure()->list:
    return readader('30-procedure')

def readView()->list:
    return readader('40-view')

def readIndex()->list:
    return readader('50-index')

def readForein()->list:
    return readader('60-forein')

def readMigration()->list:
    return readader('70-migration')

def readSeed()->list:
    return readader('80-seed')

def readEvent()->list:
    return readader('90-event')

def readAdmin()->list:
    return readader('95-admin')

