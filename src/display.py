#!/usr/bin/python3
import os, sys


_active = True

def set(active):
    _active = active

def echo(text):
    if _active:
         print(text)
