#!/usr/bin/env python3
#
#
#
#

import pynvml
import socket
import subprocess


class SyncGPU:
    def __init__(self):
        pynvml.nvmlInit()
        self.count = pynvml.nvmlDeviceGetCount()
        self.hostname = socket.gethostname()

        self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)

    def get_detail_users(self):
        result = subprocess.run(
            ["who"],
            stdout=subprocess.PIPE,
            text=True
        )

        detail_users = result.stdout.strip().split("\n")
        
        return detail_users

    def get_users(self):
        detail_users = self.get_detail_users()
        
        users = list(
            set(
                [
                    line.split()[0] for line in detail_users if line
                ]
            )
        )

        return users

    def get_gpu_name(self):
        gpu_name = pynvml.nvmlDeviceGetName(self.handle)
        return gpu_name

    def get_memory_usage(self):
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(self.handle)
        memory_used = memory_info.used / 1024**2
        memory_total = memory_info.total / 1024**2

        return memory_used, memory_total

    def get_memory_util(self):
        utilization = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
        memory_util = utilization.gpu

        return memory_util

    def get_machine_temp(self):
        machine_temp = pynvml.nvmlDeviceGetTemperature(
            self.handle,
            pynvml.NVML_TEMPERATURE_GPU
        )

        return machine_temp

    def get_fan_speed(self):
        try:
            fan_speed = pynvml.nvmlDeviceGetFanSpeed(self.handle)

        except pynvml.NVMLError_NotSupported:
            fan_speed = -1

        return fan_speed

    def get_power_usage(self):
        power_usage = pynvml.nvmlDeviceGetPowerUsage(self.handle) / 1000
        power_limit = pynvml.nvmlDeviceGetEnforcedPowerLimit(self.handle) /1000

        return power_usage, power_limit

    def create_gpu_info_dict(self):
        return {
            "hostname": self.hostname,
            "detail_users": self.get_detail_users(),
            "users": self.get_users(),
            "gpu_name": self.get_gpu_name(),
            "memory_used": self.get_memory_usage()[0],
            "memory_total": self.get_memory_usage()[1],
            "memory_util": self.get_memory_util(),
            "machine_temp": self.get_machine_temp(),
            "fan_speed": self.get_fan_speed(),
            "power_usage": self.get_power_usage()[0],
            "power_limit": self.get_power_usage()[1],
        }

    def get_static_info(self) -> dict:
        '''
        [概要]
        GPUの静的情報のみ(PC稼働中に変化しない情報)を辞書型で定義して返す
        '''
        return {
            "hostname": self.hostname,
            "gpu_name": self.get_gpu_name(),
            "users": self.get_users(),
            "memory_total": self.get_memory_usage()[1],
            "power_limit": self.get_power_usage()[1]
        }

    def get_dynamic_info(self) -> dict:
        '''
        [概要]
        GPUの動的情報のみ(PC稼働中に変化しない情報)を辞書型で定義して返す
        '''
        return {
            "memory_used": self.get_memory_usage()[0],
            "memory_util": self.get_memory_util(),
            "machine_temp": self.get_machine_temp(),
            "fan_speed": self.get_fan_speed(),
            "power_usage": self.get_power_usage()[0],
        }   
    
    def monitoring(self):
        gpu_info_dict = self.create_gpu_info_dict()
        
        print(f"\n=== {self.hostname} GPUモニタリング ===")
        print(f"ログイン中のユーザ: {gpu_info_dict['users']}\n")
        #print(f"ユーザ: {gpu_info_dict['detail_users']}\n")

        print(f"GPU {gpu_info_dict['gpu_name']}")
        print(f"  メモリ使用量: {gpu_info_dict['memory_used']:.2f} / {gpu_info_dict['memory_total']:.2f} MiB" )
        print(f"  メモリ使用率(%): {gpu_info_dict['memory_util']} %")
        print(f"  マシン内温度: {gpu_info_dict['machine_temp']} ℃")
        print(f"  ファン稼働率: {gpu_info_dict['fan_speed'] if gpu_info_dict['fan_speed'] is not None else 'N/A'} %")
        print(f"  消費電力: {gpu_info_dict['power_usage']:.2f} / {gpu_info_dict['power_limit']:.2f} W")

        return True

    
if __name__ == "__main__":
#    gpu_monitor = SyncGPU()
#    gpu_monitor.monitoring()
    SyncGPU().monitoring()
