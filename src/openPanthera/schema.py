"""
Virtual schema descriptor
"""
import openPanthera.directory as d
import openPanthera.mariadblib as m
import openPanthera.migrate as e
import openPanthera.modules as o
import hnyconfig as config

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
        schema_list = VirtualSchema(
            schema_name,
            ui
        )

