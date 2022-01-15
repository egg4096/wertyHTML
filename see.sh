#!/bin/bash

python3 translate.py
google-chrome output.html &>/dev/null &
