"Run the linux ls util and return the data"

import os

from util import call_linux


def get_nmap():
    return run_util("nmap,-sP,10.128.0.1/24")
