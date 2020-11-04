#!/usr/bin/python

import os, sys

migrationTypeList = [
    '10-table',
    '15-table-link',
    '20-function',
    '30-procedure',
    '30-view',
    '80-seed',
    '90-event',
    '95-admin'

]


/**
**/
def projectInit():
    os.mkdir('panthera', 0700)
    for i in migradtionTypeList:
        os.mkdir('panthera'+i, 0700)

