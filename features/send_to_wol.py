#!/usr/bin/env python3
#
# send_to_wol.py
#
# [概要]
# Pythonのsubprocessモジュールを使って
# Wake-On-Lan(WOL)を送信して対象のマシンを
# 起動するプログラム
#

import subprocess
import sys


class SyncWOL:
    def __init__(self, mac_address):
        self.send_wol_by_subprocess()

    def send_wol_by_subprocess(self, mac_address):
        '''
        [概要]
        subprocessモジュールを使ってWOLを送信して対象のマシンを起動する関数

        Args: 
           mac_address: 各マシンから取得したMACアドレス
        '''
        try:
            result = subprocess.run(
                [
                    "wakeonlan", mac_address
                ],
                capture_output=True,
                text=True,
                check=True,
            )

            print("WOLパケットを送信成功: ", result.stdout.strip())

        except subprocess.CalledProcessError as e:
            print("WOLパケット送信失敗: ", e.stderr.strip())


if __name__ == "__main__":
    if len(sys.argv) == 2:
        #print(sys.argv[1])
        mac_address = sys.argv[1]
        SyncGPU.send_wol_by_subprocess(mac_address)
