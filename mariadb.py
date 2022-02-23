#!/usr/bin/python

import directory
import mariadb
import config
import sys
import os

_config = config.read('mariadb')

_table_query = """

create table panthera_migration (
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

_cur = conn.cursor()

def buildTable():
    tables = directory.readTable()
    for table in  tables:
        cur.execute(tables[table])

def buildTableLink():
    links = directory.readTableLink()
    for link in  links:
        cur.execute(links[link])

def buildFunction():
    functions = directory.readFunction()
    for function in  functions:
        cur.execute(functions[function])

def buildProcedure():
    procedures = directory.readProcedure()
    for procedure in  procedures:
        cur.execute(procedures[procedure])

def buildView():
    views = directory.readView()
    for view in  views:
        cur.execute(views[view])

def buildIndex():
    indexs = directory.readIndex()
    for index in  indexs:
        cur.execute(indexs[index])

def buildForein():
    foreins = directory.readForein()
    for forein in  foreins:
        cur.execute(foreins[forein])

def buildMigration():
    migrations = directory.readMigration()
    for migration in  migrations:
        cur.execute(migrations[migration])

def buildSeed():
    seeds = directory.readSeed()
    for seed in  seeds:
        cur.execute(seeds[seed])

def buildEvent():
    events = directory.readEvent()
    for event in  events:
        cur.execute(events[event])

def buildAdmin():
    admins = directory.readAdmin()
    for admin in  admins:
        cur.execute(admins[admin])

def build():

def migration():

def migrationTableBuild():

def migrationTableRead():

def migrationTableUpdate():

def seed():

def backupImport():

def backupExport():


