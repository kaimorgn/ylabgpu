#!/usr/bin/env python3
#
# sync_cpu.py
#
# [概要]
#

import psutil
import platform
import cpuinfo

import subprocess
import json
import re


class SyncCPU:
    def __init__(self):
        self.cpu_info = cpuinfo.get_cpu_info()

    def get_vendor(self):
        return self.cpu_info["vendor_id_raw"]
        
    def get_brand(self):
        return self.cpu_info["brand_raw"]

    def get_machine_type(self):
        return platform.machine()

    def get_logical_cores(self):
        return psutil.cpu_count(logical=True)

    def get_physical_cores(self):
        return psutil.cpu_count(logical=False)

    def get_use_core_info(self):
        return psutil.cpu_percent(interval=1, percpu=True)

    def get_frequency(self):
        return psutil.cpu_freq()

    def get_static_info(self) -> dict:
        '''
        [概要]
        静的情報のみ(PC稼働中に変化しない情報)を辞書型で定義して返すメソッド
        '''
        return {
            "vendor": self.get_vendor(),
            "brand": self.get_brand(),
            "machine_type": self.get_machine_type(),
            "logical_cores": self.get_logical_cores(),
            "physical_cores": self.get_physical_cores()
        }

    def get_dynamic_info(self) -> dict:
        '''
        [概要]
        動的情報のみ(PC稼働中に変化し続ける情報)を辞書型で定義して返すメソッド
        '''
        cores_usage = self.get_use_core_info()
        
        all_usage = sum(cores_usage) / len(cores_usage) if cores_usage else 0

        frequency = self.get_frequency()
        current_frequency = frequency.current if frequency else 0.0
        
        return {
            "overall_usage": round(all_usage, 2),
            "cores_usage": cores_usage,
            "current_frequency": current_frequency
        }
        
    def sample_all(self):
        print(f"CPU Vendor        : {self.get_vendor()}")
        print(f"CPU Brand         : {self.get_brand()}")
        print(f"CPU Machine Type  : {self.get_machine_type()}")
        print(f"CPU Logical Cores : {self.get_logical_cores()}")
        print(f"CPU Physical Cores: {self.get_physical_cores()}")
        print(f"CPU Usage Cores   : {self.get_use_core_info()}")
        print(f"CPU Frequency     : {self.get_frequency()}")

        

if __name__ == "__main__":
    sync_cpu = SyncCPU()
    static_dict = sync_cpu.get_static_info()
    dynamic_dict = sync_cpu.get_dynamic_info()
    print(static_dict)
    print(dynamic_dict)
    #sync_cpu.sample_all()
