"Run the linux ls util and return the data"

import os

from util import call_linux


def get_netstat():
    return run_util("netstat,-nplt")
