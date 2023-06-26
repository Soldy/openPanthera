import directory as d
import mariadblib as m
import migrate as e
import hnyconfig as config

class VirtualSchema:
    def __init__(self, schema:str, ui):
        self.directory = d.DirectoryClass(ui, schema)
        self.mariadb = m.MariaDbClass(ui, config, self._directory)
        self.migrate = e.MigrateClass(self._mariadb, self._directory)
