"Run the linux ls util and return the data"

import os

from collectdata.util import run_util


def get_netstat():
    return run_util("netstat,-nplt")
