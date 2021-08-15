#!/bin/bash

python translator.py
google-chrome output.html &>/dev/null &
