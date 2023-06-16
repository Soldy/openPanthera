"""
" open panthera name container
"""


migrationTypeDict = {
    'table'       : '10-table',
    'table-link'  : '15-table-link',
    'function'    : '20-function',
    'procedure'   : '30-procedure',
    'view'        : '40-view',
    'index'       : '50-index',
    'forein'      : '60-forein',
    'migratrtion' : '70-migration',
    'seed'        : '80-seed',
    'event'       : '90-event',
    'admin'       : '95-admin',
    'destroy'     : 'xx-destroy'
}

migrationTypeList = {
    '10-table'     :{},
    '15-table-link':{},
    '20-function'  :{},
    '30-procedure' :{},
    '40-view'      :{},
    '50-index'     :{},
    '60-forein'    :{},
    '70-migration' :{},
    '80-seed'      :{},
    '90-event'     :{},
    '95-admin'     :{},
    'xx-destroy'   :{}
}

