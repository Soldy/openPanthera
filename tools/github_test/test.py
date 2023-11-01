import unittest
import sys
import os
import pytest
import openPanthera.lib as l


schema = l.schema('')
def test_directoryFix():
    schema.resolv('directory', 'fix')
def test_init():
    schema.resolv('init', 'sql')
def test_createTable():
    schema.resolv('build', 'table')
def test_createTableiLink():
    schema.resolv('build', 'table-link')
def test_createFunction():
    schema.resolv('build', 'function')
def test_createView():
    schema.resolv('build', 'view')
def test_createMigration():
    schema.resolv('build', 'migration')
def test_createDestroy():
    schema.resolv('build', 'destroy')
