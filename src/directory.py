#!/usr/bin/python3
import os,pathlib
import containers as c


class directoryClass:
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
    def fix(self, )->bool:
        result = True
        if os.path.isdir('panthera') == False:
            os.mkdir('panthera')
            result = False
        for i in c.migrationTypeList:
            if os.path.isdir('panthera/'+i) == False:
               os.mkdir('panthera/'+i)
               result = False
        return result
    def reader(self, target:str)->list:
        c.migrationTypeList[target] = _reader(target)
        return c.migrationTypeList[target]
    def resolv(self, command):


