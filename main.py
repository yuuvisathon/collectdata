"""
A Python script to run linux utils to track
usage of a system and network.
"""
from collectdata.run_ps import get_ps 

def main():
    print(get_ps())

if __name__ == "__main__":
    main()
