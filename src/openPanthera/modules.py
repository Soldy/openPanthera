#!/usr/bin/python3
import os
import json

_schema_json = 'schema.json'

def listCheck(list_:list)->list:
    clean_list = list(set(list_))
    if '' not in clean_list:
        clean_list.append('')
    return clean_list

def read()->list:
    if os.path.exists(_schema_json) == False:
        return ['']
    list_out = []
    with open(schemas_json, 'r') as list_file:
        list_out = json.load(list_file)
    return listCheck(list_out)

