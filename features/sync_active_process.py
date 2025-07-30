#!/usr/bin/env python3
#
# sync_active_process.py
#

import subprocess
import json


class SyncActiveProcess:
    def __init__(self, script_path="./features/active_process_monitor.sh"):
        self.script_path = script_path

    def run_script(self):
        '''
        [概要]

        Return:
            result.stdout: 実行したShellスクリプトの結果を返す
        '''
        try:
            result = subprocess.run(
                [
                    "bash", self.script_path
                ],
                capture_output=True,
                text=True,
                check=True
            )

            return result.stdout

        except subprocess.CalledProcessError as e:
            print(f"Error: Script execution failed. \n{e.stderr}")
            return None

    def display_process(self):
        '''
        [概要]
        Shellスクリプトの実行結果を表示するための関数
        '''
        output = self.run_script()
        if output is None:
            return

        try:
            processes = json.loads(output)
            #print(processes)

            if not processes:
                print("No User Processes were found using the CPU")
                return None

            print("List Of Active Processes")
            for proc in processes:
                print(proc)

        except json.JSONDecodeError as e:
            print(f"Error: Parse JSON failed. \n{e}")

    def redefine_dict_type(self):
        '''
        [概要]
        リストで取得した結果を辞書型に再定義して返す関数

        Return:
            result_dict: リストで取得した結果を辞書型に格納し直したデータ
        '''
        output = self.run_script()
        if output is None:
            return None

        try:
            processes = json.loads(output)
            #print(processes)
            result_dict = {}

            for i in range(len(processes)):
                key = f"process_{i+1}"
                result_dict[key] = processes[i]

            #print(result_dict)
            return result_dict

        except:
            print("予期せぬエラーが発生しました")


if __name__ == "__main__":
    #SyncActiveProcess().display_process()
    SyncActiveProcess().redefine_dict_type()
