"""
run linux utils
"""

import os
import subprocess

def run_util(which_one, where=''):
    if where:
        os.chwd(where)
    
    return subprocess.check_output(which_one.split(','))

