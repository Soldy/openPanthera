import openPanthera.display as ui
import openPanthera.schema as s
import hnyconfig as config


config.init('mariadb.conf.json')
def schema(name:str):
    return s.VirtualSchema(name, ui)

