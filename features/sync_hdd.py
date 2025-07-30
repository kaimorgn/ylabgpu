#!/usr/bin/env python3
#
# sync_hdd.py
#
#

import psutil
import subprocess
import re
import json


class SyncHDD:
    def __init__(self, device="/dev/sda"):
        self.device = device

    def _run_smartctl(self):
        result = subprocess.run(
            [
                "sudo", "smartctl", "--all", self.device
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"smartctl failed: {result.stderr}")
        return result.stdout

    def _get_disk_usage(self, disk_usage="/"):
        self.usage = psutil.disk_usage(disk_usage)
        return True

    def parse_vendor(self):
        result = self._run_smartctl()
        for line in result.splitlines():
            line = line.strip()
            if line.startswith("Device Model:"):
                value = line.split(":", 1)[1].strip()
                parts = value.split(" ", 1)
                return parts[0] if len(parts) == 2 else "Unknown"
        return None

    def parse_model(self):
        result = self._run_smartctl()
        for line in result.splitlines():
            line = line.strip()
            if line.startswith("Device Model:"):
                value = line.split(":", 1)[1].strip()
                parts = value.split(" ", 1)
                return parts[1] if len(parts) == 2 else value
        return None

    def parse_serial_number(self):
        result = self._run_smartctl()
        for line in result.splitlines():
            line = line.strip()
            if line.startswith("Serial Number:"):
                return line.split(":", 1)[1].strip()
        return None

    def get_usage_total(self):
        self._get_disk_usage()
        
        return self.usage.total / (1024 ** 4)

    def get_usage_used(self):
        self._get_disk_usage()

        return self.usage.used / (1024 ** 4)

    def get_usage_free(self):
        self._get_disk_usage()

        return self.usage.free / (1024 ** 4)

    def get_usage_percent(self):
        self._get_disk_usage()

        return self.usage.percent

    def create_hdd_info_dict(self):
        return {
            "vendor": self.parse_vendor(),
            "model": self.parse_model(),
            "serial": self.parse_serial_number()
        }

    def create_hdd_usage_dict(self):
        return {
            "total": self.get_usage_total(),
            "used": self.get_usage_used(),
            "free": self.get_usage_free(),
            "percent": self.get_usage_percent()
        }

    def sample_str(self):
        hdd_info_dict = self.create_hdd_info_dict()
        hdd_usage_dict = self.create_hdd_usage_dict()
        
        print("--- HDD ハードウェア情報 ---")
        print(f"HDD Vendor        : {hdd_info_dict['vendor']}")
        print(f"HDD Model         : {hdd_info_dict['model']}")
        print(f"HDD Serial Number : {hdd_info_dict['serial']}")
        print("----------------------------")
        
        print("\n--- HDD 使用状況 ---")
        print(f"HDD Total Capacity        : {hdd_usage_dict['total']:.2f} TB")
        print(f"HDD Used Capacity         : {hdd_usage_dict['used']:.2f} TB")
        print(f"HDD Free Capacity         : {hdd_usage_dict['free']:.2f} TB")
        print(f"HDD Used Percent Capacity : {hdd_usage_dict['percent']} %")
        print("----------------------------")

        return True
    
    def sample_json(self):
        hdd_info_dict = self.create_hdd_info_dict()
        hdd_usage_dict = self.create_hdd_usage_dict()

        print("----- HDD ハードウェア情報（JSON）-----")
        print(
            json.dumps(
                hdd_info_dict,
                indent=4,
                ensure_ascii=False
            )
        )
        print("-------------------------------")
        
        print("----- HDD 使用状況（JSON）-----")
        print(
            json.dumps(
                hdd_usage_dict,
                indent=4,
                ensure_ascii=False
            )
        )
        print("-------------------------------")
        
        return True


if __name__ == "__main__":
    sync_hdd = SyncHDD()
    sync_hdd.sample_str()
    sync_hdd.sample_json()
    
