#!/usr/bin/env python3
#
# backend_api.py
#
# [概要]
#
#
#

from fastapi import FastAPI
import uvicorn

from features.cpu_domain_info import CPUDomainInfo
from features.sync_gpu import SyncGPU
from features.sync_active_process import SyncActiveProcess
#from features.send_to_wol import 


app = FastAPI()


@app.get("/static-cpu")
def static_cpu_info():
    return CPUDomainInfo().static_cpu_info()


@app.get("/dynamic-cpu")
def dynami_cpu_info():
    return CPUDomainInfo().dynamic_cpu_info()


@app.get("/static-gpu")
def static_gpu_info():
    return SyncGPU().get_static_info()


@app.get("/dynamic-gpu")
def dynami_gpu_info():
    return SyncGPU().get_dynamic_info()


@app.get("/active-process-info")
def active_process_info():
    return SyncActiveProcess().redefine_dict_type()


if __name__ == "__main__":
    uvicorn.run("backend_api:app", host="0.0.0.0", port=8000, reload=True)
