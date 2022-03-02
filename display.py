#!/usr/bin/python3

import os, sys


_active = True

def echo(text):
    if _active:
         print(text)
