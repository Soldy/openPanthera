#!/usr/bin/python3
import os
import pathlib
import containers as c

class directoryClass:
    def _mainPath(self)->str:
        return (
            str(pathlib.Path().absolute())+
            self._path_plus+
            '/panthera/'
        )
    def _targetPath(self, target:str)->str:
        return (
            self._mainPath()+
            target
        )
    def _mainCheck(self)->bool:
        return os.path.isdir(
            self._mainPath()
        )
    def _targetCheck(self, target)->bool:
        return os.path.isdir(
            self._path(target)
        )
    def _fileCheck(self, target, file_name)->bool:
        return os.path.isdir(
            self._path(target)+
            file_name
        )
    def _mkdir(self, target:str):
        os.mkdir(self._path(target))
    def _reader(self, target:str)->list:
        out = {}
        target_dict = c.migrationTypeDict[target]
        if self._targetCheck(target_dict) == False:
           return print('Directory '+target+' is missing')
        for i in os.listdir():
            if self._fileCheck(target_dict, i):
               with open(self._targetPath(target_path)+i) as f:
                   out[i]=str(f.read())
        return out
    def init(self)->bool:
        if os.path.exists('panthera'):
            return False
        os.mkdir('panthera')
        for i in c.migrationTypeList:
            if self._targetCheck(i):
                return False
            self._mkdir(i)
    def check(self)->int:
        if self._mainCheck() == False:
            return 1
        for i in c.migrationTypeList:
            if self._targetCheck(i) == False:
               return 2
        return 0
    def fix(self)->bool:
        result = True
        if self._mainCheck() == False:
            os.mkdir(self._mainCheck())
            result = False
        for i in c.migrationTypeList:
            if self._targetCheck(i) == False:
               self._mkdir(i)
               result = False
        return result
    def reader(self, target:str)->list:
        c.migrationTypeList[target] = self._reader(target)
        return c.migrationTypeList[target]
    def resolv(self, command)->any:
        return self.list[command]()
    def __init__(self, path):
        self._path_plus = path
        self.list = {
            'init' : self.init,
            'check': self.check,
            'fix'  : self.fix
        }


