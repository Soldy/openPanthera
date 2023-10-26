#!/usr/bin/python3
from datetime import datetime

_active = True
_log = []

def _stamp()->int:
    return (datetime.now() - datetime(1970, 1, 1)).total_seconds()

def _append(type_:str, text:str):
    _log.append({
        'type':type_,
        'time':_stamp(),
        'message':text
    })

def set(active:bool):
    _active = active

def echo(text:str):
    if _active:
         print(text)

def log(text:str):
    _append('log', text)
    echo(text)

def error(text:str):
    _log.append('error',text)
    echo(text)
