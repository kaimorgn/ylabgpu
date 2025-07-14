#!/usr/bin/env python3
#
#
#
#
#

from fastapi import FastAPI
import uvicorn

from features.sync_gpu import SyncGPU
from features.sync_cpu import SyncCPU

app = FastAPI()


@app.get("/static-gpu")
def get_static_gpu_info():
    static_gpu = SyncGPU().get_static_info()
    return static_gpu


@app.get("/dynamic-gpu")
def get_dynamic_gpu_info():
    dynamic_gpu = SyncGPU().get_dynamic_info()
    return dynamic_gpu


@app.get("/static-cpu")
def get_static_cpu_info():
    static_cpu = SyncCPU().get_static_info()
    return static_cpu


@app.get("/dynamic-cpu")
def get_dynamic_cpu_info():
    dynamic_cpu = SyncCPU().get_dynamic_info()
    return dynamic_cpu


if __name__ == "__main__":
    uvicorn.run("apis:app", host="0.0.0.0", port=8404, reload=True)
