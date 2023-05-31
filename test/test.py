import unittest
import sys
import os
#sys.path.append(os.getcwd() + '/..')
import directory as d
import mariadblib as m
import hnyconfig as config


m.initMigrationTable()
m.buildTable()
