# ylabgpu
## branch: feat_processinfo

# 1.実装環境
- OS: Ubuntu22.04
- Python: 3.11.11 # 異なる場合は pyenv コマンドで合わせる

# 2.リポジトリをクローン
~~~
$ cd; git clone github:kaimorgn/ylabgpu
~~~

# 3.ディレクトリ構造
~~~
$ tree
=> 
.
├── README.md
└── features
    ├── active_process_monitor.sh
    └── sync_active_process.py

1 directory, 3 files
~~~

# 4.プログラムを実行
~~~
$ cd features
$ ./sync_active_process.py
~~~
- 実行結果
~~~
{'process_1': {'user': 'kai', 'pid': 72521, 'elapsed': '02:30', 'command': 'emacs', 'cpu_percent': 1.1, 'mem_percent': 0}}
~~~

# 5.今後の展望
- APIと連携してプロセス一覧をJSON形式で渡せるようにする
- Reflexで構成したカードの中で実行中のプロセスを表示できるようにする
