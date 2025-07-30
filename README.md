# ylabgpu
## branch: dev/backend_api

# 1.実装環境
- OS: Ubuntu22.04
- Python: 3.11.11 # 異なる場合は pyenv コマンドで合わせる

# 2.リポジトリをクローン
~~~
$ cd; git clone github:kaimorgn/ylabgpu
$ cd; ylabgpu/
$ git checkout dev/backend_api
~~~

# 3.ディレクトリ構成
~~~
$ tree
=> 
.
├── README.md
├── backend_api.py
├── clean.sh
├── features
│   ├── active_process_monitor.sh
│   ├── clean.sh
│   ├── cpu_domain_info.py
│   ├── send_to_wol.py
│   ├── send_to_wol.sh
│   ├── sync_active_process.py
│   ├── sync_cpu.py
│   ├── sync_gpu.py
│   ├── sync_hdd.py
│   └── sync_ram.py
└── requirements.txt

1 directory, 14 files
~~~

# 4.仮想環境を構築
~~~
$ cd; cd .venv/
$ pyenv local 3.11.11
$ python3 -m venv ylabgpu
$ source ylabgpu/bin/activate
$ cd; cd ylabgpu/
$ pip install -r requirements.txt
~~~

# 4.プログラムを実行
~~~
$ python backend_api.py
~~~

# 5.今後の展望
- CPUとGPU，プロセス一覧をAPIで取得できるようになった．<br>
＊WOLは今回は除外した
- 次はReflexで構成したWebアプリ上で取得した情報を表示できるようにする．


