#!/usr/bin/python


import mariadb
import sys
import os


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


