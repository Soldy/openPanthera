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
    for table in  tables::
        cur.execute(tables[table])



def build():

def migration():

def migrationTableBuild():

def migrationTableRead():

def migrationTableUpdate():

def seed():

def backupImport():

def backupExport():


