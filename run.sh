#!/bin/bash
pip install -r requirements.txt;
touch log.log
python collectdata/run_keylogger.py &
python main.py &
