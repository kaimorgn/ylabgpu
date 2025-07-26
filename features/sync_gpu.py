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
        '''
        [概要]
        self.handleが認識している単一のGPUのモデル名を取得して返す関数

        return:
            gpu_name: GPUのモデル名を返す(例: NVIDIA GeForce RTX 3090 Ti)
        '''
        gpu_name = pynvml.nvmlDeviceGetName(self.handle)
        return gpu_name

    def get_vram_usage(self):
        '''
        [概要]
        self.handleが認識している単一のGPUのVRAM情報を取得して返す関数

        return:
            vram_used: 使用されているVRAM領域を返す
            vram_total: VRAMの使用上限を返す
        '''
        vram_info = pynvml.nvmlDeviceGetMemoryInfo(self.handle)
        vram_used = vram_info.used / 1024**2
        vram_total = vram_info.total / 1024**2

        return vram_used, vram_total

    def get_vram_percent(self):
        '''
        [概要]
        VRAMの使用率(%)を取得して返す関数

        return:
            vram_percent: VRAMの使用率(%)情報
        '''
        utilization = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
        vram_percent = utilization.gpu

        return vram_percent

    def get_gpu_temp(self):
        '''
        [概要]
        GPUの排熱情報を取得して返す関数

        return:
            gpu_temp: GPUの排熱情報
        '''
        gpu_temp = pynvml.nvmlDeviceGetTemperature(
            self.handle,
            pynvml.NVML_TEMPERATURE_GPU
        )

        return gpu_temp

    def get_fan_speed(self):
        '''
        [概要]
        GPU ファンの稼働率(%)を取得して返す関数
        
        return:
           fan_speed: GPU ファンの稼働率(%)
        '''
        try:
            fan_speed = pynvml.nvmlDeviceGetFanSpeed(self.handle)

        except pynvml.NVMLError_NotSupported:
            fan_speed = -1

        return fan_speed

    def get_power_usage(self):
        '''
        [概要]
        GPU の電力消費情報を取得して返す関数

        return:
            power_usage: 使用している電力消費量
            power_limit: 使用できる電力上限
        '''
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
            "gpu_model": self.get_gpu_name(),
            "users": self.get_users(),
            "vram_total": self.get_vram_usage()[1],
            "power_limit": self.get_power_usage()[1]
        }

    def get_dynamic_info(self) -> dict:
        '''
        [概要]
        GPUの動的情報のみ(PC稼働中に変化しない情報)を辞書型で定義して返す
        '''
        return {
            "vram_used": self.get_vram_usage()[0],
            "vram_percent": self.get_vram_percent(),
            "gpu_temp": self.get_gpu_temp(),
            "fan_speed": self.get_fan_speed(),
            "power_usage": self.get_power_usage()[0],
        }   
    
    def monitoring(self):
        gpu_static_info = self.get_static_info()
        gpu_dynamic_info = self.get_dynamic_info()
        
        print(f"\n=== {self.hostname} GPU Monitoring ===")
        print(f"Login Users: {gpu_static_info['users']}\n")
        #print(f"ユーザ: {gpu_info_dict['detail_users']}\n")

        print(f"GPU Model:  {gpu_static_info['gpu_model']}")
        print(f"VRAM Used: {gpu_dynamic_info['vram_used']:.2f} / {gpu_static_info['vram_total']:.2f} MiB" )
        print(f"VRAM Percent: {gpu_dynamic_info['vram_percent']} %")
        print(f"GPU Temperature: {gpu_dynamic_info['gpu_temp']} ℃")
        print(f"Power Used: {gpu_dynamic_info['power_usage']:.2f} / {gpu_static_info['power_limit']:.2f} W")
        print(f"Fan Percent: {gpu_dynamic_info['fan_speed'] if gpu_dynamic_info['fan_speed'] is not None else 'N/A'} %")
        print("==========")

        return True

    
if __name__ == "__main__":
#    gpu_monitor = SyncGPU()
#    gpu_monitor.monitoring()
    SyncGPU().monitoring()
