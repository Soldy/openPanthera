#!/usr/bin/python
import directory
import display
import hashlib
import mariadb
import hnyconfig as config
import time
import sys
import os

_p = display.echo

_config = config.init('mariadb.conf.json')

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
    migration INT DEFAULT 0,
    type VARCHAR(64) NOT NULL,
    file VARCHAR(256) NOT NULL,
    hash VARCHAR(512),
    date INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);

"""

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


def buildTable():
    tables = directory.readTable()
    for table in  tables:
        if not checkExitBuildScript('table', table, tables[table]):
            _cur.execute(tables[table])
            _insertBuildScript('table', table, tables[table])
            _p('Table "'+str(table)+'" executed')
        else:
            _p('Table "'+str(table)+'" already done')

def buildTableLink():
    links = directory.readTableLink()
    for link in  links:
        if not checkExitBuildScript('link', link):
            _cur.execute(links[link])
            _insertBuildScript('link', link, links[link])
            _p('Link "'+str(link)+'" executed')
        else:
            _p('Link "'+str(link)+'" already done')


def buildFunction():
    functions = directory.readFunction()
    for function in  functions:
        if not checkExitBuildScript('function', function, functions[function]):
            _cur.execute(functions[function])
            _insertBuildScript('function', function, functions[function])
            _p('Function "'+str(function)+'" executed')
        else:
            _p('Function "'+str(function)+'" already done')

def buildProcedure():
    procedures = directory.readProcedure()
    for procedure in  procedures:
        if not checkExitBuildScript('procedure', procedure, procedures[procedure]):
            _cur.execute(procedures[procedure])
            _insertBuildScript('procedure', procedure, procedures[procedure])
            _p('Procedure "'+str(procudere)+'" executed')
        else:
            _p('Procedure "'+str(procedure)+'" already done')

def buildView():
    views = directory.readView()
    for view in  views:
        if not checkExitBuildScript('view', view, views[view]):
            _cur.execute(views[view])
            _insertBuildScript('view', view, views[view])
            _p('View "'+str(view)+'" executed')
        else:
            _p('View "'+str(view)+'" already done')

def buildIndex():
    indexs = directory.readIndex()
    for index in  indexs:
        if not checkExitBuildScript('index', index, indexs[index]):
            _cur.execute(indexs[index])
            _insertBuildScript('index', index, indexs[index])
            _p('Index "'+str(index)+'" executed')
        else:
            _p('Index "'+str(index)+'" already done')

def buildForein():
    foreins = directory.readForein()
    for forein in  foreins:
        if not checkExitBuildScript('forein', forein, foreins[forein]):
            _cur.execute(foreins[forein])
            _insertBuildScript('forein', forein, foreins[forein])
            _p('Forein "'+str(forein)+'" executed')
        else:
            _p('Forein "'+str(forein)+'" already done')

def buildMigration():
    migrations = directory.readMigration()
    for migration in  migrations:
        if not checkExitBuildScript('migration', migration, migrations[migration]):
            _cur.execute(migrations[migration])
            _insertBuildScript('migration', migration, migrations[migration])
            _p('Migration "'+str(migration)+'" executed')
        else:
            _p('Migration "'+str(migration)+'" already done')

def buildSeed():
    seeds = directory.readSeed()
    for seed in  seeds:
        if not checkExitBuildScript('seed', seed, seeds[seed]):
            _cur.execute(seeds[seed])
            _insertBuildScript('seed', seed, seeds[seed])
            _p('Seed "'+str(seed)+'" executed')
        else:
            _p('Seed "'+str(seed)+'" already done')

def buildEvent():
    events = directory.readEvent()
    for event in  events:
        if not checkExitBuildScript('event', event, events[event]):
            _cur.execute(events[event])
            _insertBuildScript('event', event, events[event])
            _p('Event "'+str(event)+'" executed')
        else:
            _p('Event "'+str(event)+'" already done')

def buildAdmin():
    admins = directory.readAdmin()
    for admin in  admins:
        if not checkExitBuildScript('admin', admin, admins[admin]):
            _cur.execute(admins[admin])
            _insertBuildScript('admin', admin, admins[admin])
            _p('Admin "'+str(admin)+'" executed')
        else:
            _p('Admin "'+str(admin)+'" already done')


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
         "SELECT date FROM panthera_migration WHERE type=? AND file=? AND hash=?",
         (
            type_,
            file_name_,
           _sha256(file_)
         )
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


#def build():
#
#def migration():
#
#def migrationTableBuild():
#
#def migrationTableRead():
#
#def migrationTableUpdate():
#
#def seed():
#
#def backupImport():
#
#def backupExport():


