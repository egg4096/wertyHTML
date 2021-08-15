#!/bin/bash

python translate.py
google-chrome output.html &>/dev/null &
