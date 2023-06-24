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
_p = {}
_config = {}
_inited = False
_conn = ''
_cur = ''

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

def init(config, directory_):
    _config = config
    _directory = directory_
    try:
        _conn = mariadb.connect(
            user      = config.get('user'),
            password  = config.get('password'),
            host      = config.get('host'),
            port      = int(config.get('port')),
            database  = config.get('database')
        )
    except mariadb.Error as e:
        print(f"MariaDb died in my arm: {e}")
        sys.exit(1)
    _conn.autocommit = True
    _cur = _conn.cursor()

def _sha256(string):
    crypto = hashlib.new('sha256')
    crypto.update(
        bytes(string ,encoding='utf8')
    )
    return crypto.hexdigest()

def _buildScript(title_:str)->bool:
    scripts = _directory.reader(title_)
    utitle = title_[0].upper() + title_[1:]
    for script in  scripts:
        if not checkExitBuildScript(title_, script, scripts[script]):
            _p(utitle+' "'+str(script)+'" executing')
            _cur.execute(scripts[script])
            _insertBuildScript(title_, script, scripts[script])
            _p(utitle+' "'+str(script)+'" executed')
        else:
            _p(utitle+' "'+str(script)+'" already done')
    return True

def build(name):
    if name == "destroy":
        destroyScript()
    return  _buildScript(name)

def initMigrationTable():
    _cur.execute(_table_query)

def _insertBuildScript(type_, file_name_, file_):
    _cur.execute(
        "INSERT INTO panthera_migration (type, file, hash, date) VALUES (?, ?, ?, ?)", 
        (
           type_,
           file_name_,
           _sha256(file_),
           round(time.time())
        )
    )
    _conn.commit() 

def checkExitBuildScript(type_, file_name_, file_):
    _cur.execute(
         "SELECT date FROM panthera_migration WHERE type=? AND file=? AND hash=? AND destroyed = 0",
         (
            type_,
            file_name_,
           _sha256(file_)
         )
    )
    for date in _cur:
        return True
    return False


def destroyScript():
    _cur.execute(
         "UPDATE panthera_migration SET destroyed = ? WHERE destroyed = ?",
         (
             int( time.time() ),
             0
         )
    )
    _conn.commit()

