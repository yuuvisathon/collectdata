"""
run linux utils
"""

import os
import subprocess

def run_util(which_one, where=''):
    if where:
        os.chwd(where)
    return os.subprocess([which_one.split(',')])

