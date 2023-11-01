#!/usr/bin/python3
import os
import openPanthera.containers as c




class DirectoryClass:
    def _mainPath(self)->str:
        return (
            str(os.getcwd())+
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
    def _reader(self, target:str)->dict:
        out = {}
        target_dict = c.migration_type_dict[target]
        if self._targetCheck(target_dict) == False:
           return print('Directory '+target+' is missing')
        print(target_dict)
        print(self._targetPath(target_dict))
        file_list = sorted(os.listdir(self._targetPath(target_dict)))
        print(file_list[:])
        if type(file_list) is not list:
            return {}
        for i in file_list:
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
            self._ui.log('Main directory is missing')
            result = 1
        for i in c.migrationTypeList:
            if self._targetCheck(i) == False:
               self._ui.log('Sub directory '+i+' missing')
               result = 2
        return result
    def fix(self)->int:
        if self._mainCheck() == False:
            os.mkdir(self._mainCheck())
            self._ui.log('Main directory fixxed')
        for i in c.migrationTypeList:
            if self._targetCheck(i) == False:
               self._mkdir(i)
               self._ui.log('Sub directory '+i+' fixxed')
    def reader(self, target:str)->list:
        c.migrationTypeList[target] = self._reader(target)
        return c.migrationTypeList[target]
    def resolv(self, command:str)->any:
        return self.list[command]()
    def __init__(self, path:str, ui_):
        """ variable defination """
        self._ui = ui_
        self._path_plus = path
        self.list = {
            'init' : self.init,
            'check': self.check,
            'fix'  : self.fix
        }


