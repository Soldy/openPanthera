#!/usr/bin/python3
import os
import sys
import time
import directory
import display
import hashlib
import mariadb
import containers as c

_directory = directory
_config = {}
_inited = False
_conn = ''
_cur = 'hu'

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
                    self._insertBuildScript(
                        title_,
                        script,
                        scripts[script]
                    )
                self._p(utitle+' "'+str(script)+'" executed')
            else:
                self._p(utitle+' "'+str(script)+'" already done')
        return 0

    def build(self, name:str)->int:
        print(name)
        if name == "destroy":
            self.destroyScript()
        return self._buildScript(name)

    def initMigrationTable(self)->int:
        self._cur.execute(_table_query)
        return 0

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
        return 0
    def checkExitBuildScript(self, type_, file_name_, file_):
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


    def destroyScript(self):
        self._cur.execute(
             "UPDATE panthera_migration SET destroyed = ? WHERE destroyed = ?",
             (
                 int( time.time() ),
                 0
             )
        )
        self._conn.commit()
        return 0

