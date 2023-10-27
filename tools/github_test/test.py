import unittest
import sys
import os
import pytest
import openPanthera.lib as l


schema = l.schema('')
def test_init():
    schema.resolv('init', 'sql')
def test_createTable():
    schema.resolv('build', 'table')
def test_createFunction():
    schema.resolv('build', 'function')
def test_createView():
    schema.resolv('build', 'view')
def test_createDestroy():
    schema.resolv('build', 'destroy')
