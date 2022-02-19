#!/usr/bin/python


import mariadb
import sys
import os

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
        user="",
        password="",
        host="",
        port=,
        database=""
    )
except mariadb.Error as e:
    print(f"MariaDb died in my arm: {e}")
    sys.exit(1)

def build():

def migration():

def migrationTableBuild():

def migrationTableRead():

def migrationTableUpdate():

def seed():

def backupImport():

def backupExport():


