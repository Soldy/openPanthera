"""
 open panthera fail helper
"""
import copy

class FailHelper:
    """
    simple fail class
    """
    def __init__(self):
        self._errors = []

    def get(self)->list[str]:
        """
        cloned error list

        :return: list[str]:
        """
        return copy.deepcopy(self._errors)

    def clean(self):
        """
        clean error log
        """
        self._errors = []

    def add(self, err:str):
        """
        add an error to log

        :param:str:
        """
        self._errors.append(err)

    def failed(self)->bool:
        """
        error check 

        :return: bool:
        """
        if len(self._errors) > 0:
            return True
        return False
