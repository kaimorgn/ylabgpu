# ylabgpu
## branch: feat_wol

# 1.実装環境
- OS: Ubuntu22.04
- Python: 3.11.11 # 異なる場合は pyenv コマンドで合わせる

# 2.リポジトリをクローン
~~~
$ cd; git clone github:kaimorgn/ylabgpu
$ cd; ylabgpu/
$ git checkout feat_wol
~~~

# 3.ディレクトリ構成
~~~
$ tree
=> 
.
├── README.md
└── features
    ├── clean.sh
    ├── send_to_wol.py
    └── send_to_wol.sh

1 directory, 4 files
~~~

# 4.プログラムを実行
~~~
$ cd features/
$ ./send_to_wol.py XX:XX:XX:XX:XX:XX
$ ./send_to_wol.sh XX:XX:XX:XX:XX:XX
~~~

- 実行結果(PythonスクリプトとShellスクリプトでは出力結果の有無が異なります)

# 5.今後の展望
- APIと連携してマジックパケットを送信できるようにする．このとき，Shellスクリプトの方が望ましいかもしれない
- Reflexで構成したボタンをクリックすると，マジックパケットが送信されてWOLできるようにする
