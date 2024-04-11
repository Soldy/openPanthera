
separator_space = "    "

class AxpTableField:
    def __init__(
        self,
        otpions_:dict[str,str]
    ):
        self._options = options_
        self._uniq()
    def _uniq(self):
        if('uniq' in self._options.keys()):
            self._options.uniq = False
    def _null(self):
        if('null' in self._options.keys()):
            self._options.null = False
    def string(self)->str:
        return (
          separator_space +
          self._options.name +
          " " +
          self._options.type +
          ",\n"
        )

    

class AxpTable:
    def __init__(self, options:dict):
        self._options = options
        self._fields = []
        for i in self._options.fields.keys():
            self._fields[i] = AxpTableField(
              self._options.fields[i]
            )
    def _create(self)->str:
        return (
          "CREATE TABLE `"+
          self._options.name+
          "` (\n"
        )
    def _primaryStart(self)->str:
        return (
          separator_space +
          "`id` SERIAL,\n"
        )
    def _primaryEnd(self)->str:
        return (
          separator_space +
          "KEY `index` (`id`)"
        )
    def _fieldsString(self)->str:
        out = "" 
        for i in self._fields.keys():
            out += self._fields[i].string()
        return out
    def _end(self)->str:
        return (
          ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;"
        )
    def string(self)->str:
        out = ""
        out += self._create()
        out += self._primaryStart()
        out += self._fieldsString()
        out += self._primaryEnd()
        out += self._end()
