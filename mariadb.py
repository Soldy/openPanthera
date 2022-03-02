#!/usr/bin/python

import directory
import display
import hashlib
import mariadb
import config
import time
import sys
import os

_p = display.echo

_config = config.read('mariadb')

_migrationTypeList = [
    '10-table',
    '15-table-link',
    '20-function',
    '30-procedure',
    '40-view',
    '50-index',
    '60-forein',
    '70-migration',
    '80-seed',
    '90-event',
    '95-admin'
]


_table_query = """

CREATE TABLE IF NOT EXISTS panthera_migration (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    migration INT UNSIGNED NOT NULL,
    file VARCHAR(256) NOT NULL,
    hash VARCHAR(512),
    date INT UNSIGNED NOT NULL
    PRIMARY KEY ( id )
);

"""

try:
    conn = mariadb.connect(
        user=_config.user,
        password=config.password,
        host=config.host,
        port=_config.port,
        database=_config.database
    )
except mariadb.Error as e:
    print(f"MariaDb died in my arm: {e}")
    sys.exit(1)

_conn.autocommit = True
_cur = conn.cursor()

def _sha256(string):
    crypto = hashlib.new('sha256')
    crypto.update(
        bytes(string ,encoding='utf8')
    )
    return crypto.hexdigest()


def buildTable():
    tables = directory.readTable()
    for table in  tables:
        if not checkExitBuildScript('table', table):
            _cur.execute(tables[table])
            _insertBuildScript('table', table, tables[table]):
            _p('Table "'+str(tsble)+'" executed')

def buildTableLink():
    links = directory.readTableLink()
    for link in  links:
        if not checkExitBuildScript('link', link):
            _cur.execute(links[link])
            _insertBuildScript('link', link, links[link]):
            _p('Link "'+str(link)+'" executed')


def buildFunction():
    functions = directory.readFunction()
    for function in  functions:
        if not checkExitBuildScript('function', function):
            _cur.execute(functions[function])
            _insertBuildScript('function', function, functions[function]):
            _p('Function "'+str(function)+'" executed')

def buildProcedure():
    procedures = directory.readProcedure()
    for procedure in  procedures:
        if not checkExitBuildScript('procedure', procedure):
            _cur.execute(procedures[procedure])
            _insertBuildScript('procedure', procedure, procedures[procedure]):
            _p('Procedure "'+str(procudere)+'" executed')

def buildView():
    views = directory.readView()
    for view in  views:
        if not checkExitBuildScript('view', view):
            _cur.execute(views[view])
            _insertBuildScript('view', view, views[view]):
            _p('View "'+str(view)+'" executed')

def buildIndex():
    indexs = directory.readIndex()
    for index in  indexs:
        if not checkExitBuildScript('index', index):
            _cur.execute(indexs[index])
            _insertBuildScript('index', index, indexs[index]):
            _p('Index "'+str(index)+'" executed')

def buildForein():
    foreins = directory.readForein()
    for forein in  foreins:
        if not checkExitBuildScript('forein', forein):
            _cur.execute(foreins[forein])
            _insertBuildScript('forein', forein, foreins[forein]):
            _p('Forein "'+str(forein)+'" executed')

def buildMigration():
    migrations = directory.readMigration()
    for migration in  migrations:
        if not checkExitBuildScript('migration', migration):
            _cur.execute(migrations[migration])
            _insertBuildScript('migration', migration, migrations[migration]):
            _p('Migration "'+str(migration)+'" executed')

def buildSeed():
    seeds = directory.readSeed()
    for seed in  seeds:
        if not checkExitBuildScript('seed', seed):
            _cur.execute(seeds[seed])
            _insertBuildScript('seed', seed, seeds[seed]):
            _p('Seed "'+str(seed)+'" executed')

def buildEvent():
    events = directory.readEvent()
    for event in  events:
        if not checkExitBuildScript('event', event):
            _cur.execute(events[event])
            _insertBuildScript('event', event, events[event]):
            _p('Event "'+str(event)+'" executed')

def buildAdmin():
    admins = directory.readAdmin()
    for admin in  admins:
        if not checkExitBuildScript('admin', admin):
            _cur.execute(admins[admin])
            _insertBuildScript('admin', admin, admins[admin]):
            _p('Admin "'+str(admin)+'" executed')

def insertBuildScript(type_, file_name_, file_):
    _cur.execute(
        "INSERT INTO panthera_migration (type, file, hash, date) VALUES (?, ?i, ?, ?)", 
        (
           type_,
           file_,
           _sha512(file_),
           round(time.time())
        )
    )
    conn.commit() 

def checkiExitBuildScript(type_, file_name_):
    _cur.execute(
         "SELECT date FROM panthera_migration WHERE type=? AND file=? AND hash=?",
         type_,
         file_name_
    )
    for date in _cur:
        return True
    return False

def checkBuildScript(type_, file_name_, file_):
    _cur.execute(
         "SELECT date FROM panthera_migration WHERE type=? AND file=? AND hash=?",
         type_,
         file_name_,
         _sha512(file_)

    )
    for date in _cur:
        return True
    return False

def build():

def migration():

def migrationTableBuild():

def migrationTableRead():

def migrationTableUpdate():

def seed():

def backupImport():

def backupExport():


