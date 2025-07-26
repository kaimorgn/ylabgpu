# ylabgpu
## branch: feat_cpuinfo

# 1.実装環境
- OS: Ubuntu22.04
- Python: 3.11.11 # 異なる場合は pyenv コマンドで合わせる

# 2.リポジトリをクローン
~~~
$ cd; git clone github:kaimorgn/ylabgpu
$ cd ylabgpu/
$ git checkout feat_cpuinfo
~~~

# 3.ディレクトリ構成
~~~
$ tree
=> 
.
├── README.md
├── features
│   ├── clean.sh
│   ├── command.sh
│   ├── cpu_domain_info.py
│   ├── sync_cpu.py
│   ├── sync_hdd.py
│   └── sync_ram.py
└── requirements.txt

1 directory, 8 files
~~~

# 4.仮想環境を構築
~~~
$ cd; cd .venv/
$ pyenv local 3.11.11
$ python3 -m venv psutil_env
$ source psutil_env/bin/activate
$ cd; cd ylabgpu/
$ pip install -r requirements.txt
~~~

# 5.プログラムを実行
~~~
$ cd features/
$ ./command.sh
$ ./clean.sh # __pycache__を削除
~~~

- 実行結果(実行するマシンごとに出力結果が異なります)
~~~
===== CPU Info =====
===== 各部品の製造元と製品番号 =====
CPU Vendor: GenuineIntel
CPU Model: 13th Gen Intel(R) Core(TM) i9-13900K
RAM Vendor: Crucial Technology
RAM Model: CT32G4DFD832A.M16FF
RAM Slots: 4
HDD Vendor: WDC
HDD Model: CT32G4DFD832A.M16FF
===== 各部品の稼働状況 =====
CPU Core Used Percent: 0.0 %
RAM Used: 2.53 / 125.54 GB
RAM Percent: 2 %
HDD Used: 0.54 / 5.41 TB
HDD Percent: 10.5 %
~~~

# 6.今後の展望
- APIと連携してCPU周りのデータを渡せる(JSON形式)ようにする
- Reflexで構成したカードの中でデータを表示できるようにする
