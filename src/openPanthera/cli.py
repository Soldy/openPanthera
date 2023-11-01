#!/usr/bin/python3
import os
import sys
import openPanthera.commander as commander


sys.exit(
    commander.resolve(
        sys.argv[len(sys.argv)-1]
    )
)
