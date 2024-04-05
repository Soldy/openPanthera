
_sup_types = [
    "VARCHAR",
    "CHAR",
    "TINYINT",
    "BOOLEAN",
    "INT1",
    "SMALLINT",
    "INT2",
    "MEDIUMINT",
    "INT3",
    "INT",
    "INTEGER",
    "INT4",
    "BIGINT",
    "INT8",
    "DECIMAL",
    "DEC",
    "NUMERIC",
    "FIXED",
    "FLOAT",
    "DOUBLE",
    "REAL",
    "BIT",
    "BINARY",
    "VARBINARY",
    "BLOB",
    "TINYBLOB",
    "MEDIUMBLOB",
    "LONGBLOB",
    "TINYTEXT",
    "TEXT",
    "MEDIUMTEXT",
    "LONGTEXT",
    "JSON",
    "CHAR",
    "VARCHAR",
    "ENUM",
    "INET4",
    "INET6"
]

_sup_engines = [
    'Aria',
    'Federated',
    'InnoDB',
    'MyISAM',
    'MyRocks',
    'Mroonga'
]



class FielsHelper: 

class FieldHelper:
    def __init__(self, name:str, types:dict):
        self._name = name
        self._types = types
        self._unsigned = False
        self._notnull = False
        if types['unsigned']:    
            self._unsigned = True
        if types['notnull']:    
            self._notnull = True
    def create(self):
        out = "    `"+self._name+"`"
        if self._types['type'] in _sup_types:
            out = (out+" "+self._types['type'])
        if self._unsigned:    
            out = (out+" UNSIGNED")
        if self._notnull:    
            out = (out+" NOT NULL")
        return out
    def functionInput(self):

    def functionCheck(self)

class TableCreator:
    def tableStart(self, name:str)->str:
        out = ("TABLE CREATE `"+name+"` (\n")
        return out
    def tableIndexStart(self)->str:
    def tableIndexEnd(self)->str:
        
    def fieldSeparate(self)->str:
        return ",\n"

    def tableEnd(self name:str)->str:
        out = ")  ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;"
        return out


class TableManager:
    def __init __(self):
        self._table = {
            "name":"notset",
            "fields":[],
            "engine":"InnoDB",
            "charset":"utf8",
            "collate":"utf8_general_ci",
            "id":True,

        }
    def fromJson


