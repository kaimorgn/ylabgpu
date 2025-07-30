#!/usr/bin/env python3

from features.sync_cpu import SyncCPU
from features.sync_ram import SyncRAM
from features.sync_hdd import SyncHDD


class CPUDomainInfo:
    def __init__(self):
        self.cpu = SyncCPU()
        self.ram = SyncRAM()
        self.hdd = SyncHDD()

    def static_cpu_info(self):
        return {
            "cpu_vendor": self.cpu.get_vendor(),
            "cpu_model": self.cpu.get_brand(),
            "ram_vendor": self.ram._get_manufacturers(),
            "ram_model": self.ram._get_part_numbers(),
            "ram_slots": self.ram._get_number_of_devices(),
            "ram_max": self.ram.get_total(),
            "hdd_vendor": self.hdd.parse_vendor(),
            "hdd_model": self.hdd.parse_model(),
            "hdd_max": self.hdd.get_usage_total(),
        }

    def dynamic_cpu_info(self):
        return {
            "cpu_core_percent": self.cpu.get_use_core_percent(),
            "ram_used": self.ram.get_used(),
            "ram_used_percent": self.ram.get_percent_used(),
            "hdd_used": self.hdd.get_usage_used(),
            "hdd_used_percent": self.hdd.get_usage_percent()
        }

    def output_sample(self):
        static_info = self.static_cpu_info()
        dynamic_info = self.dynamic_cpu_info()

        print("===== CPU Info =====")
        print("===== 各部品の製造元と製品番号 =====")
        print(f"CPU Vendor: {static_info['cpu_vendor']}")
        print(f"CPU Model: {static_info['cpu_model']}")
        print(f"RAM Vendor: {static_info['ram_vendor']}")
        print(f"RAM Model: {static_info['ram_model']}")
        print(f"RAM Slots: {static_info['ram_slots']}")
        print(f"HDD Vendor: {static_info['hdd_vendor']}")
        print(f"HDD Model: {static_info['ram_model']}")

        print("===== 各部品の稼働状況 =====")
        print(f"CPU Core Used Percent: {dynamic_info['cpu_core_percent']} %")
        print(f"RAM Used: {dynamic_info['ram_used']:.2f} / {static_info['ram_max']:.2f} GB")
        print(f"RAM Percent: {dynamic_info['ram_used_percent']} %")
        print(f"HDD Used: {dynamic_info['hdd_used']:.2f} / {static_info['hdd_max']:.2f} TB")
        print(f"HDD Percent: {dynamic_info['hdd_used_percent']} %")
        

if __name__ == "__main__":
    CPUDomainInfo().output_sample()
    # print(CPUDomainInfo().static_cpu_info())
    # print(CPUDomainInfo().dynamic_cpu_info())
