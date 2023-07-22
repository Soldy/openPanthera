#!/usr/bin/python3
import json

def listCheck(list_:list)->list:
    clean_list = list(set(list_))
    if "" not in clean_list:
        clean_list.append("")
    return clean_list

def read()->list:
    list_out = []
    with open('schemas.json', 'r') as list_file:
        list_out = json.load(list_file)
    return listCheck(list_out)

