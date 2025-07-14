#!/bin/bash

cd; cd .venv/
python3 -m venv fapi
source fapi/bin/activate
cd; cd ylabgpu/
pip install -r requirements.txt
pip install fastapi uvicorn pynvml psutil py-cpuinfo
