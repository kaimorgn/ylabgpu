#!/bin/bash

./clean.sh
source ~/.venv/pynvml_env/bin/activate
python sync_gpu.py
