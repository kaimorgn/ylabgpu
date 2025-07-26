# ylabgpu
## branch: feat_gpuinfo

# 1.実装環境
- OS: Ubuntu22.04
- Python: 3.11.11 # 異なる場合は pyenv コマンドで合わせる

# 2.リポジトリをクローン
~~~
$ cd; git clone github:kaimorgn/ylabgpu
$ cd ylabgpu/
$ git checkout feat_gpuinfo
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
│   └── sync_gpu.py
└── requirements.txt

1 directory, 5 files
~~~

# 4.仮想環境を構築
~~~
$ cd; cd .venv/
$ pyenv local 3.11.11
$ python3 -m venv pynvml_env
$ source pynvml_env/bin/activate
$ cd; cd ylabgpu
$ pip install -r requirements.txt
~~~

# 5.プログラムを実行
~~~
$ cd features/
$ ./command.sh
~~~

- 実行結果(実行するマシンごとに出力結果が異なる箇所があります)
~~~
=== junin GPU Monitoring ===
Login Users: ['kai']

GPU Model:  NVIDIA GeForce RTX 3090 Ti
VRAM Used: 454.75 / 24564.00 MiB
VRAM Percent: 0 %
GPU Temperature: 40 ℃
Power Used: 20.61 / 450.00 W
Fan Percent: 0 %
==========
~~~

# 6.今後の展望
- APIと連携してGPU周りのデータを渡せる(JSON形式)ようにする
- Reflexで構成したカードの中でデータを表示できるようにする
