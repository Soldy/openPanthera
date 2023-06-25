import display as ui


def display(ui_):
    ui = ui_

class MigrateClass:
    def _init(self)->int:
        return self.mariadb.initMigrationTable()
    def resolv(self, command:str)->int:
        return self._list[command]()
    def __init__(self, mariadb_, directory_):
        self.mariadb   = mariadb_
        self.directory = directory_
        self._list = {
            'init' : self._init
        }
