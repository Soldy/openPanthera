"""
Virtual schema descriptor
"""
import hnyconfig as config
import openPanthera.directory as d
import openPanthera.mariadblib as m
import openPanthera.migrate as e
import openPanthera.modules as o

class VirtualSchema:
    """
    Virtual schema manager

    :param: str:
    :param: ui:
    """
    def __init__(self, schema:str, ui):
        self._directory = d.DirectoryClass(schema, ui)
        self._mariadb = m.MariaDbClass(ui, config, self._directory)
        self._migrate = e.MigrateClass(self._mariadb, self._directory)
        self._agents = {
            'migrate'  : self._migrate.resolv,
            'init'     : self._init,
            'build'    : self._mariadb.build,
            'clean'    : self._mariadb.clean,
            'directory': self._directory.resolv,
            'show'     : self._mariadb.show
        }

    def resolv(self, main, sub)->any:
        """
        Virtual schema agent service

        :param: str:
        :param: str:
        :return: any:
        """
        return self._agents[main](sub)

    def check(self, main)->bool:
        """
        Virtual schema agent check

        :param: str:
        :return: bool:
        """
        if main in self._agents:
            return True
        return False

    def _init(self, sub: str):
        """
        Virtual schema manager
        sub init

        :param: str:
        """
        if sub == 'sql':
            self._mariadb.initMigrationTable()
        if sub == 'directory':
            self._directory.init()


def schemas(ui)->VirtualSchema:
    """
    Schema definitor

    :return: VirtualSchema
    """
    schema_list = []
    for schema_name in o.read():
        schema_list.append(
          VirtualSchema(
            schema_name,
            ui
          )
        )
    return schema_list
