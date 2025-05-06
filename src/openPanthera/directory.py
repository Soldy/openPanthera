"""
Directory manager
"""
#!/usr/bin/python3
import os
import openPanthera.containers as c




class DirectoryClass:
    """
    :param: str:
    :param: Display:
    """
    def __init__(self, path_:str, ui_):
        """ variable defination """
        self._ui = ui_
        self._path_plus = path_
        self.list = {
            'init' : self.init,
            'check': self.check,
            'fix'  : self.fix
        }

    def _mainPath(self)->str:
        """
        :return:str:
        """
        return (
            str(os.getcwd())+
            self._path_plus+
            '/panthera/'
        )

    def _targetPath(self, target_:str)->str:
        """
        :param:str:
        :return:str:
        """
        return (
            self._mainPath()+
            target_+
            '/'
        )

    def _mainCheck(self)->bool:
        """
        :return:bool:
        """
        return os.path.isdir(
            self._mainPath()
        )

    def _targetCheck(self, target_:str)->bool:
        """
        :param:str:
        :return:bool:
        """
        return os.path.isdir(
            self._targetPath(target_)
        )

    def _fileCheck(self, target_:str, file_name_:str)->bool:
        """
        :param:str:
        :param:str:
        :return:bool:
        """
        return os.path.isfile(
            self._targetPath(target_)+
            file_name_
        )

    def _mkdir(self, target_:str):
        """
        :return:int:
        """
        os.mkdir(self._targetPath(target_))

    def _reader(self, target_:str)->dict:
        """
        :param:str
        :return:dict[str,str]:
        """
        out = {}
        target_dict = c.migration_type_dict[target_]
        if not self._targetCheck(target_dict):
            return print('Directory '+target_+' is missing')
        print(target_dict)
        print(self._targetPath(target_dict))
        file_list = sorted(os.listdir(self._targetPath(target_dict)))
        print(file_list[:])
        if isinstance(file_list, list):
            return {}
        for i in file_list:
            if self._fileCheck(target_dict, i):
                with open(self._targetPath(target_dict)+i) as f:
                    out[i]=str(f.read())
            else:
                print(i)
        return out

    def init(self)->int:
        """
        :return:int:
        """
        if os.path.exists('panthera') is False:
            os.mkdir('panthera')
        for i in c.migrationTypeList:
            if self._targetCheck(i) is False:
                self._mkdir(i)

    def check(self)->int:
        """
        :return:int:
        """
        result = 0
        if self._mainCheck() is False:
            self._ui.log('Main directory is missing')
            result = 1
        for i in c.migrationTypeList:
            if self._targetCheck(i) is False:
                self._ui.log('Sub directory '+i+' missing')
                result = 2
        return result

    def fix(self)->int:
        """
        :return:int:
        """

        if self._mainCheck() is False:
            os.mkdir(self._mainCheck())
            self._ui.log('Main directory fixxed')
        for i in c.migrationTypeList:
            if self._targetCheck(i) is False:
                self._mkdir(i)
                self._ui.log('Sub directory '+i+' fixxed')

    def reader(self, target_:str)->list:
        """
        :param:str:
        :return:list[any]:
        """
        c.migrationTypeList[target_] = self._reader(target_)
        return c.migrationTypeList[target_]

    def resolv(self, command_:str)->any:
        """
        :param:str:
        :return:any:
        """
        return self.list[command_]()
