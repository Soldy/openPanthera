#!/usr/bin/python3
import os,pathlib
import containers as c



def init()->bool:
    if os.path.exists('panthera'):
        return False
    os.mkdir('panthera')
    for i in c.migrationTypeList:
        if os.path.exists('panthera/'+i):
            return False
        os.mkdir('panthera/'+i)

def check()->int:
    if os.path.isdir('panthera') == False:
        return 1
    for i in c.migrationTypeList:
        if os.path.isdir('panthera/'+i) == False:
           return 2
    return 0

def fix()->bool:
    result = True
    if os.path.isdir('panthera') == False:
        os.mkdir('panthera')
        result = False
    for i in c.migrationTypeList:
        if os.path.isdir('panthera/'+i) == False:
           os.mkdir('panthera/'+i)
           result = False
    return result

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
    c.migrationTypeList[target] = _reader(target)
    return c.migrationTypeList[target]

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

