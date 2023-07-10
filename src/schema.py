import directory as d
import mariadblib as m
import migrate as e
import hnyconfig as config

class VirtualSchema:
    def resolv(self, main, sub):
        return self._agents[main](sub)
    def __init__(self, schema:str, ui):
        self._directory = d.DirectoryClass(schema, ui)
        self._mariadb = m.MariaDbClass(ui, config, self._directory)
        self._migrate = e.MigrateClass(self._mariadb, self._directory)
        self._agents = {
            'migrate'  : self._migrate.resolv,
            'build'    : self._mariadb.build,
            'directory': self._directory.resolv
        }
