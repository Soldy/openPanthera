"""
Header hint reader
We want to ensure the AI receives the correct information, so we prepare the data before feeding it.
"""


class reader:
    """
    AXPN reader and preparator
    """
    def __init__(self):
        self._meta = {
            "first_line":0,
            "last_line":0
        }
        self._data = {
           'vars'      : {},
           'cols'      : [],
           'args'      : [],
           'tables'    : [],
           'functions' : [],
           'procedurs' : [],
           'views'     : [],
           'returns'   : []
        }

    def metaFirst(self)->int:
        """
        first meta line

        :return:int:
        """
        return int(self._meta["first_line"])

    def metaLast(self)->int:
        """
        first meta line

        :return:int:
        """
        return int(self._meta["last_line"])

    def typeCheck(self)->bool:
        """
        correct type check
        """
        return True

    def _firstLineCheck(self, line_)->bool:
        """
        first line check

        :param:str:
        :return:bool:
        """
        line = line_.lstrip()
        if line[:3] == '/**':
            return True
        return False

    def _lastLineCheck(self, line_)->bool:
        """
        last line check

        :param:str:
        :return:bool:
        """
        line = line_.lstrip()
        if line[:3] == '**/':
            return True
        return False

    def dataMine(self, lines_:list[str])->None:
        """
        last line check

        :param:list[str]:
        """
        serial = 0
        in_in = False
        for line in lines_:
            if in_in:
                if self._dataLine(line):
                    if self._lastLineCheck(line):
                        self._meta["last_line"] = int(serial)
                        in_in = False
            else:
                if self._firstLineCheck(line):
                    self._meta["first_line"] = int(serial)
                    in_in = True
        serial = serial + 1

    def _dataLineVar(self, parts_: list[str])->dict[str,str]:
        """
        data line variables

        :param:list[str]:
        :param:dict[str,str]:
        """
        atype = parts_[2].strip()
        name = parts_[3].strip()
        additional = ''.join(parts_[3:])
        col = {
          "name" : name,
          "type" : atype,
          "additional" : additional
        }
        return col

    def _dataLineTwoNames(self, parts_:list[str])->dict[str,str]:
        """
        two name section data line

        :param:list[str]:
        :param:dict[str,str]:
        """
        name = parts_[2].strip()
        additional = ''.join(parts_[2:])
        two_names = {
          "name" : name,
          "additional" : additional
        }
        return two_names

    def _dataLineArgument(self, parts_)->None:
        self._data['args'].append(
          self._dataLineVar(parts_)
        )

    def _dataLineTable(self, parts_)-> None:
        self._data['tables'].append(
          self._dataLineTwoNames(parts_)
        )

    def _dataLineFunction(self, parts_)-> None:
        self._data['functions'].append(
          self._dataLineTwoNames(parts_)
        )

    def _dataLineProcedure(self, parts_)-> None:
        self._data['procedurs'].append(
          self._dataLineTwoNames(parts_)
        )

    def _dataLineView(self, parts_)-> None:
        self._data['views'].append(
          self._dataLineTwoNames(parts_)
        )

    def _dataLineReturn(self, parts_)-> None:
        self._data['returns'].append(
          self._dataLineVar(parts_)
        )

    def _dataLineCol(self, parts_)-> None:
        self._data['cols'].append(
          self._dataLineVar(parts_)
        )

    def _dataLine(self, lines_)->bool:
        """
        data line / meta line processor

        :param:list[str]:
        :return:bool:
        """
        line = lines_.strip()
        if line[:1] != '*':
            return False
        parts = line.split()
        if len(parts) < 3:
            return False
        name = parts[1].strip()
        if name == "@pcol":
            self._dataLineCol(parts)
        elif name == "@parg":
            self._dataLineArgument(parts)
        elif name == "@preturn":
            self._dataLineReturn(parts)
        elif name == "@ptable":
            self._dataLineTable(parts)
        elif name == "@pfunction":
            self._dataLineFunction(parts)
        elif name == "@pprocedure":
            self._dataLineProcedure(parts)
        elif name == "@pview":
            self._dataLineView(parts)
        else:
            return False
        return True
