"Run the linux ls util and return the data"

import os

from util import run_util


def get_ls():
    return run_util("ls,-R,~")
