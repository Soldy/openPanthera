#!/usr/bin/python3
import os
import sys
import time
import hashlib
import mariadb
import openPanthera.directory as directory
import openPanthera.containers as c

_directory = directory
_config = {}
_inited = False
_conn = ''

_table_query = """
CREATE TABLE IF NOT EXISTS panthera_migration (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    migration INT DEFAULT 0,
    destroyed INT DEFAULT 0,
    type VARCHAR(64) NOT NULL,
    file VARCHAR(256) NOT NULL,
    hash VARCHAR(512),
    date INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);
"""

def _sha256(string):
    crypto = hashlib.new('sha256')
    crypto.update(
        bytes(string ,encoding='utf8')
    )
    return crypto.hexdigest()


class MariaDbClass:
    def __init__(self, ui, config, directory_):
        self._p = ui.log
        self._config = config
        self._directory = directory_
        try:
            self._conn = mariadb.connect(
                user      = config.get('user'),
                password  = config.get('password'),
                host      = config.get('host'),
                port      = int(config.get('port')),
                database  = config.get('database')
            )
        except mariadb.Error as e:
            print(f"MariaDb died in my arm: {e}")
            sys.exit(1)
        self._conn.autocommit = True
        self._cur = self._conn.cursor()

    def _buildScript(self, title_:str)->int:
        scripts = self._directory.reader(title_)
        utitle = title_[0].upper() + title_[1:]
        for script in  scripts:
            block_ = True
            if title_ == 'destroy':
               block_ = False
            else:
               block_ = self.checkExitBuildScript(
                   title_,
                   script,
                   scripts[script]
                )
            if not block_ :
                self._p(utitle+' "'+str(script)+'" executing')
                self._cur.execute(scripts[script])
                if title_ != 'destroy':
                    self._cleanBuildScript(
                        title_,
                        script
                    )
                    self._insertBuildScript(
                        title_,
                        script,
                        scripts[script]
                    )
                self._p(utitle+' "'+str(script)+'" executed')
            else:
                self._p(utitle+' "'+str(script)+'" already done')
        return 0

    def build(self, name:str):
        if name == "destroy":
            self._destroyBuildScript()
        return self._buildScript(name)
    
    def show(self, name:str):
        shows = {
           'table'     : self._showTables,
           'view'      : self._showViews,
           'procedure' : self._showProcedures,
           'function'  : self._showFunctions
        }
        shows[name]()
    def clean(self, name:str):
        cleans = {
           'function'  : self._deleteAllFunctions,
           'procedure'  : self._deleteAllProcedures,
           'table'     : self._deleteAllTables,
           'view'      : self._deleteAllViews
        }
        cleans[name]()
    def initMigrationTable(self):
        self._cur.execute(_table_query)

    def _insertBuildScript(self, type_:str, file_name_:str, file_:str)->int:
        self._cur.execute(
            "INSERT INTO panthera_migration (type, file, hash, date) VALUES (?, ?, ?, ?)", 
            (
               type_,
               file_name_,
               _sha256(file_),
               round(time.time())
            )
        )
        self._conn.commit() 

    def checkExitBuildScript(self, type_:str, file_name_:str, file_:str)->bool:
        self._cur.execute(
             "SELECT date FROM panthera_migration WHERE type=? AND file=? AND hash=? AND destroyed = 0",
             (
                type_,
                file_name_,
               _sha256(file_)
             )
        )
        for date in self._cur:
            return True
        return False

    def _destroyBuildScript(self):
        self._cur.execute(
             "UPDATE panthera_migration SET destroyed = ? WHERE destroyed = ?",
             (
                 int( time.time() ),
                 0
             )
        )
        self._conn.commit()

    def _cleanBuildScript(self, type_:str, file_name_:str):
        self._cur.execute(
             "UPDATE panthera_migration SET destroyed = ? WHERE destroyed = ? AND type = ? AND file = ?",
             (
                 int( time.time() ),
                 0,
                 type_,
                 file_name_
             )
        )
        self._conn.commit()
    def _showStatus(self, type_:str):
        lista = []
        self._cur.execute(
          "SHOW "+type_+" STATUS WHERE db = ?",
          [
            self._config.get('database')
          ]
        )
        for (
          Db,
          Name,
          Type,
          Definer,
          Modified,
          Created,
          Security_type,
          Comment,
          character_set_client,
          collation_connection,
          coll
        ) in self._cur:
          lista.append(Name)
        return lista
    def _dropIfExists(self, type_:str, name_:str):
        self._cur.execute(
          "DROP "+type_+" `"+name_+"`;"
        )
        self._p("Delete "+type_+" "+name_)
        self._conn.commit()
    def _showProcedures(self):
        for (
          Name
        ) in self._showStatus("PROCEDURE"):
          self._p(f"{Name}")
    def _deleteAllProcedures(self):
        for (
          Name
        ) in self._showStatus("PROCEDURE"):
            self._dropIfExists("PROCEDURE", Name)
    def _showFunctions(self):
        for (
          Name
        ) in self._showStatus("FUNCTION"):
          self._p(f"{Name}")
    def _deleteAllFunctions(self):
        for (
          Name
        ) in self._showStatus("FUNCTION"):
            self._dropIfExists("FUNCTION", Name)
    def _listViews(self):
        lista = []
        self._cur.execute(
          "SHOW FULL TABLES WHERE Table_Type = 'VIEW'"
        )
        for (
          Name,
          Type
        ) in self._cur:
          lista.append(Name)
        return lista
    def _showViews(self):
        for (
          Name
        ) in self._listViews():
          self._p(f"{Name}")
    def _deleteAllViews(self):
        for (
          Name
        ) in self._listViews():
            self._dropIfExists("VIEW", Name)
    def _listTables(self):
        lista = []
        self._cur.execute(
          "SHOW FULL TABLES WHERE Table_Type = 'BASE TABLE'"
        )
        for (
          Name,
          Type
        ) in self._cur:
          if Name != "panthera_migration":
            lista.append(Name)
        return lista
    def _showTables(self):
        for (
          Name
        ) in self._listTables():
            self._p(f"{Name}")
    def _deleteAllTables(self):
        for (
          Name
        ) in self._listTables():
            self._p(f"{Name}")
            self._dropIfExists("TABLES", Name)

