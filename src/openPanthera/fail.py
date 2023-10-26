"""
" open panthera fail manager
"""
import copy

class FailHelper:
    def get(self)->list:
        return copy.deepcopy(self._errors)
    def clean(self):
        self._errors = []
    def add(self, err):
        self._errors.append(err)
    def failed(self)->bool:
        if len(self._errors) > 0:
            return True
        return False
    def __init__(self):
        self._errors = []
