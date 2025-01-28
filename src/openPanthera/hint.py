"""
Header hint reader
We want to ensure the AI receives the correct information, so we prepare the data before feeding it.
"""


class reader:
  def __init__(self):
    self._vars = {}
    self._in = False
    self._cols = []
    self._args = []
    self._tables = []
    self._functions = []
    self._procedurs = []
    self._returns = []

  def typeCheck(self, line)->bool:
      
  def _firstLineCheck(self, line_)->bool:
    line = line_.lstrip()
    if line[:3] == '/**':
      self._in = True
    else:
      self._in = False 

  def _lastLineCheck(self, line_)->bool:
    line = line_.lstrip()
    if line[:3] == '**/':
      self._in = False
    else:
      self._in = True

  def _dataMine(self, lines_)->None:
    for line in lines_:
      if self._in:
        if self._dataLine(line) == False:
          self._lastLineCheck(line)
      else:
        self._firstLineCheck(line)
  def _dataLineVar(self, parts_)->list:
    _type = (_parts[2].strip())
    _name = (_parts[3].strip())
    _additional = (''.join(_parts[3:]))
    _col = {
      "name" : _name,
      "type" : _type,
      "additional" : _additional
    }
    return _col
  def _dataLineTwoNames(self, parts_)->list:
    _name = (_parts[2].strip())
    _additional = (''.join(_parts[2:]))
    _two_names = {
      "name" : _name,
      "additional" : _additional
    }
    return _two_names
  def _dataLineArgument(self, parts_)-> None:
    self._args.append(
      self._dataLineVar(parts_)
    )
  def _dataLineTable(:self, parts_)-> None:
    self._tables.append(
      self._dataLineTwoNames(parts_)
    )
  def _dataLineFunction(self, parts_)-> None:
    self._functions.append(
      self._dataLineTwoNames(parts_)
    )
  def _dataLineProcedure(self, parts_)-> None:
    self._procedurs.append(
      self._dataLineTwoNames(parts_)
    )
  def _dataLineView(self, parts_)-> None:
    self._views.append(
      self._dataLineTwoNames(parts_)
    )
  def _dataLineReturn(self, parts_)-> None:
    self._returns.append(
      self._dataLineVar(parts_)
    )
  def _dataLineCol(self, parts_)-> None:
    self._cols.append(
      self._dataLineVar(parts_)
    )
  def _dataLine(self, line_)->bool:
    _line = line.strip()
    if _line[:1] != '*':
      return False
    _parts = _line.split()
    if len(_parts) < 3:
      return False
    _name = (_parts[1].strip())
    if _name == "@pcol": 
      self._dataLineCol(parts_)
    elif _name == "@parg":
      self._dataLineArgument(parts_)
    elif _name == "@preturn":
      self._dataLineReturn(parts_)
    elif _name == "@ptable":
      self._dataLineTable(parts_)
    elif _name == "@pfunction":
      self._dataLineFunction(parts_)
    elif _name == "@pprocedure":
      self._dataLineProcedure(parts_)
    elif _name == "@pview":
      self._dataLineView(parts_)
    else:
      return False
    return True
