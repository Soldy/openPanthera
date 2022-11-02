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
    target_dict = c.migrationTypeDict[target]
    target_path = (
        str(pathlib.Path().absolute())+
        '/panthera/'+
        target_dict
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
    return readader('table')

def readTableLink()->list:
    return readader('table-link')

def readFunction()->list:
    return readader('function')

def readProcedure()->list:
    return readader('procedure')

def readView()->list:
    return readader('view')

def readIndex()->list:
    return readader('index')

def readForein()->list:
    return readader('foreign')

def readMigration()->list:
    return readader('migration')

def readSeed()->list:
    return readader('seed')

def readEvent()->list:
    return readader('event')

def readAdmin()->list:
    return readader('admin')

