#!/bin/bash

./clean.sh
source ~/.venv/psutil_env/bin/activate
python cpu_domain_info.py

