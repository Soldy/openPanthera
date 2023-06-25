"""
" open panthera name container
"""


migration_type_dict = {
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

short_types = {
    't' : 'table',
    'l' : 'table-link',
    'f' : 'function',
    'p' : 'procedure',
    'v' : 'view',
    'i' : 'index',
    'k' : 'forein',
    'm' : 'migration',
    's' : 'seed',
    'e' : 'event',
    'a' : 'admin',
    'x' : 'destroy'
}

short_commands = {
    'b' : 'build',
    'd' : 'directory',
    'm' : 'migrate'
}

short_directory_commands = {
    'i' : 'init',
    'c' : 'check',
    'f' : 'fix',
}

short_migrate_commands = {
   's'  : 'init',
   'i'  : 'import',
   'e'  : 'export',
   'b'  : 'backup'
}

short_specific_commands = {
   'd' : short_directory_commands,
   'b' : short_types,
   'm' : short_migrate_commands
}

migrationTypeList = {
    '10-table'      :{},
    '15-table-link' :{},
    '20-function'   :{},
    '30-procedure'  :{},
    '40-view'       :{},
    '50-index'      :{},
    '60-forein'     :{},
    '70-migration'  :{},
    '80-seed'       :{},
    '90-event'      :{},
    '95-admin'      :{},
    'xx-destroy'    :{}
}
