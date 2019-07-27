"""
A Python script to run linux utils to track
usage of a system and network.
"""
from collectdata.run_ps import get_ps 
from collectdata.ptyuuvis import push_file 
import time

starttime=time.time()

def main():
    while True: 
        ps_data = str(get_ps())
        push_file(ps_data, "Carrot", "Beer")

        time.sleep(600.0 - ((time.time() - starttime) % 600.0))

if __name__ == "__main__":
    main()
