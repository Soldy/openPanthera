#!/usr/bin/python3
import os
import pathlib
import containers as c
import display as ui


def display(ui_):
    ui = ui_


class DirectoryClass:
    def _mainPath(self)->str:
        return (
            str(pathlib.Path().absolute())+
            self._path_plus+
            '/panthera/'
        )
    def _targetPath(self, target:str)->str:
        return (
            self._mainPath()+
            target+
            '/'
        )
    def _mainCheck(self)->bool:
        return os.path.isdir(
            self._mainPath()
        )
    def _targetCheck(self, target)->bool:
        return os.path.isdir(
            self._targetPath(target)
        )
    def _fileCheck(self, target, file_name)->bool:
        return os.path.isfile(
            self._targetPath(target)+
            file_name
        )
    def _mkdir(self, target:str):
        os.mkdir(self._targetPath(target))
    def _reader(self, target:str)->list:
        out = {}
        target_dict = c.migration_type_dict[target]
        if self._targetCheck(target_dict) == False:
           return print('Directory '+target+' is missing')
        for i in os.listdir(self._targetPath(target_dict)):
            if self._fileCheck(target_dict, i):
               with open(self._targetPath(target_dict)+i) as f:
                   out[i]=str(f.read())
            else:
               print(i)
        return out
    def init(self)->int:
        if os.path.exists('panthera') == False:
            os.mkdir('panthera')
        for i in c.migrationTypeList:
            if self._targetCheck(i) == False:
               self._mkdir(i)
    def check(self)->int:
        result = 0
        if self._mainCheck() == False:
            ui.log('Main directory is missing')
            result = 1
        for i in c.migrationTypeList:
            if self._targetCheck(i) == False:
               ui.log('Sub directory '+i+' missing')
               result = 2
        return result
    def fix(self)->int:
        if self._mainCheck() == False:
            os.mkdir(self._mainCheck())
            ui.log('Main directory fixxed')
        for i in c.migrationTypeList:
            if self._targetCheck(i) == False:
               self._mkdir(i)
               ui.log('Sub directory '+i+' fixxed')
    def reader(self, target:str)->list:
        c.migrationTypeList[target] = self._reader(target)
        return c.migrationTypeList[target]
    def resolv(self, command)->any:
        return self.list[command]()
    def __init__(self, path:str):
        """ variable defination """
        self._path_plus = path
        self.list = {
            'init' : self.init,
            'check': self.check,
            'fix'  : self.fix
        }


