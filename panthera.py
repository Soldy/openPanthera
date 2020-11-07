#!/usr/bin/python

import os, sys

migrationTypeList = [
    '10-table',
    '15-table-link',
    '20-function',
    '30-procedure',
    '40-view',
    '50-index',
    '60-forein',
    '70-migration',
    '60-seed',
    '90-event',
    '95-admin'

]


def projectInit():
    os.mkdir('panthera')
    for i in migrationTypeList:
        os.mkdir('panthera/'+i)

