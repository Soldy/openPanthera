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
         print(text+"\033[0m")

def log(text:str):
    _append('log', text)
    echo("\033[38;2;230;255;255m"+text)

def error(text:str):
    _append('error',text)
    echo("\033[38;2;255;0;0m"+text)
