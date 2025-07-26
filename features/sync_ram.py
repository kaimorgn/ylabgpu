#!/usr/bin/env python3
#
# sync_ram.py
#
# [概要]
#

import psutil

import subprocess
import json
import re


class SyncRAM:
    def __init__(self):
        '''
        dmidecodeの出力内容を初期化時に取得（sudo権限が必要）
        '''
        try:
            result = subprocess.run(
                ["sudo", "dmidecode", "--type", "memory"],
                capture_output=True,
                text=True,
                check=True
            )
            self.output = result.stdout
        except subprocess.CalledProcessError as e:
            print("dmidecodeの実行に失敗しました:", e)
            self.output = ""

    def _get_number_of_devices(self):
        '''
        "Number Of Devices:"(デバイス数) を探して取得（System Information セクション）
        '''
        match = re.search(r"Number Of Devices:\s+(\d+)", self.output)
        return int(match.group(1)) if match else None

    def _get_maximum_capacity(self):
        # "Maximum Capacity:" を探して取得（数値とGB/MBを含む行のみ）
        matches = re.findall(r"Maximum Capacity:\s+([\d\s]+[GM]B)", self.output)
        return matches[0].strip() if matches else None

    def _get_manufacturers(self):
        # 複数の"Manufacturer:"項目をリスト化（空でない値のみ）
        manufacturers = re.findall(r"Manufacturer:\s+(.+)", self.output)
        # 空文字列や"Not Specified"などを除外
        valid_manufacturers = [
            m.strip() for m in manufacturers if m.strip() and m.strip() != "Not Specified"
        ]
        return self._format_with_count(valid_manufacturers)

    def _get_part_numbers(self):
        part_numbers = re.findall(r"Part Number:\s+(.+)", self.output)
        # 空文字列や"Not Specified"などを除外
        valid_part_numbers = [
            p.strip() for p in part_numbers if p.strip() and p.strip() != "Not Specified"
        ]
        return self._format_with_count(valid_part_numbers)

    def _get_sizes(self):
        # 各モジュールの容量を取得（例：32 GB）
        size_lines = re.findall(r"Volatile Size:\s+(.+)", self.output)
        # "None"や空文字列を除外し、有効な容量のみを返す
        valid_sizes = []
        for line in size_lines:
            line = line.strip()
            if line and line.lower() != "none" and "gb" in line.lower():
                valid_sizes.append(line)
        return self._format_with_count(valid_sizes)

    def _format_with_count(self, items):
        # アイテムの出現回数をカウント
        from collections import Counter
        counter = Counter(items)
        
        # {データ} x {個数} の形式で文字列として返す
        result = []
        for item, count in counter.items():
            if count == 1:
                result.append(item)
            else:
                result.append(item)
        
        # カンマ区切りの文字列として返す
        return ", ".join(result)

    def _get_info(self):
        self.info = psutil.virtual_memory()
        return True

    def get_used(self):
        self._get_info()
        used = self.info.used / (1024 ** 3)
        return used

    def get_available(self):
        self._get_info()
        available = self.info.available / (1024 ** 2)
        return available

    def get_total(self):
        self._get_info()
        total = self.info.total / (1024 ** 3)
        return total

    def get_percent_used(self):
        self._get_info()
        percent_used = int(self.info.percent)
        return percent_used

    def get_free(self):
        self._get_info()
        return self.info.free / (1024 ** 2)

    def get_cached(self):
        self._get_info()
        return getattr(self.info, "cached", 0) / (1024 ** 2)

    def get_buffers(self):
        self._get_info()
        return getattr(self.info, "buffers", 0) / (1024 ** 2)

    def get_shared(self):
        self._get_info()
        return getattr(self.info, "shared", 0) / (1024 ** 2)

    def create_memory_status_dict(self):
        '''
        RAMの現在の使用状況をdict型で返す（単位：MiBなどを含む）
        '''
        self._get_info()
        return {
            "used_mib": round(self.info.used / (1024 ** 2), 2),
            "available_mib": round(self.info.available / (1024 ** 2), 2),
            "total_mib": round(self.info.total / (1024 ** 2), 2),
            "percent_used": round(self.info.percent, 2),
            "free_mib": round(self.info.free / (1024 ** 2), 2),
            "cached_mib": round(getattr(self.info, "cached", 0) / (1024 ** 2), 2),
            "buffers_mib": round(getattr(self.info, "buffers", 0) / (1024 ** 2), 2),
            "shared_mib": round(getattr(self.info, "shared", 0) / (1024 ** 2), 2)
        }

    def create_ram_spec_dict(self):
        '''
        RAMハードウェア情報をdict型で返す
        '''
        return {
            "number_of_devices": self._get_number_of_devices(),
            "manufacturers": self._get_manufacturers(),
            "part_numbers": self._get_part_numbers(),
            "sizes": self._get_sizes(),
            "maximum_capacity": self._get_maximum_capacity()
        }

    def sample_str(self):
        ram_spec_dict = self.create_ram_spec_dict()
        memory_status_dict = self.create_memory_status_dict()

        print("----- RAM ハードウェア情報 -----")
        print(f"RAMスロット数   : {ram_spec_dict['number_of_devices']}")
        print(f"メーカー        : {ram_spec_dict['manufacturers']}")
        print(f"品番            : {ram_spec_dict['part_numbers']}")
        print(f"モジュール容量  : {ram_spec_dict['sizes']}")
        print(f"最大サポート容量: {ram_spec_dict['maximum_capacity']}")
        print("-------------------------------")

        print("----- RAM メモリ状況 -----")

        print(f"RAMメモリ使用量      : {memory_status_dict['used_mib']:.2f} / {memory_status_dict['total_mib']:.2f} MiB")
        print(f"RAMメモリ使用率(%)   : {memory_status_dict['percent_used']:.2f} %")
        print(f"RAMメモリ空き容量    : {memory_status_dict['available_mib']:.2f} MiB")
        print(f"RAMメモリ完全未使用量: {memory_status_dict['free_mib']:.2f} MiB")
        print(f"RAMキャッシュ領域    : {memory_status_dict['cached_mib']:.2f} MiB")
        print(f"RAMバッファ領域      : {memory_status_dict['buffers_mib']:.2f} MiB")
        print(f"共有RAM領域          : {memory_status_dict['shared_mib']:.2f} MiB")
        print("-------------------------------")

        return True

    def sample_json(self):
        ram_spec_dict = self.create_ram_spec_dict()
        memory_status_dict = self.create_memory_status_dict()

        print("----- RAM ハードウェア情報（JSON）-----")
        print(
            json.dumps(
                ram_spec_dict,
                indent=4,
                ensure_ascii=False
            )
        )
        print("-------------------------------")
        
        print("----- RAM メモリ状況（JSON）-----")
        print(
            json.dumps(
                memory_status_dict,
                indent=4,
                ensure_ascii=False
            )
        )
        print("-------------------------------")
        
        return True
    

if __name__ == "__main__":
    sync_ram = SyncRAM()
    sync_ram.sample_str()
    #sync_ram.sample_json()
    
