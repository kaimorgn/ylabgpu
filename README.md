# ylabgpu
## branch: main

# 1.実装環境
- OS: Ubuntu22.04
- Python: 3.11.11 # 異なる場合は pyenv コマンドで合わせる

# 2.リポジトリをクローン
~~~
$ cd; git clone github:kaimorgn/ylabgpu
~~~

# 2.リポジトリへ入り，セットアップをする
## 2.1 Pythonの仮想環境を作成・有効化
~~~
$ ./2-1_create_virtual_environment.sh
~~~

## 2.2 ufwを有効化
~~~
$ ./2-2_ufw_activate.sh
~~~

# 3.APIを有効化
＊3.1と3.2のどちらかを片方を選んで実行してください

## 3.1 screenを使用して有効化
~~~
$ cd; screen
$ cd ylabgpu/

$ ./3-1_screen_api_activate.sh
~~~
=> APIを有効化したら，アドレスを指定してアクセスできるか確認
~~~
# MBAでOK
$ nc -vz IP_ADDRESS 8404
~~~

## 3.2 serviceとして半永続的有効化
先にserviceファイルを編集する
~~~
$ emacs -nw gpuapp.service
~~~
ファイルを開いたら"XXX"と書かれている箇所のみを編集する．
"XXX"部分は自分が使用しているアカウント名(例: kai)を
記述し，保存して編集モードから抜ける．<br>
編集完了後，下記のファイルを実行してserviceを有効化する．
serviceとして有効化すると，APIが立ち上がる．
~~~
$ ./3-2_move_service_file.sh
~~~
=> APIを有効化したら，アドレスを指定してアクセスできるか確認
~~~
# MBAでOK
$ nc -vz IP_ADDRESS 8404
~~~

## 3.3 注意点
＊無事に有効化が完了した場合，PCの再起動はお控えください．
再起動後，APIを有効化しても外部PCからアクセスできない不具合を
確認しております．<br>
もし，再起動した場合は，下記の手順を実行し，ufwとAPIを再度有効化してください．
~~~
$ sudo ufw delete allow 8404/tcp
$ sudo ufw disable
$ sudo reboot

# 再起動後にufwを有効化
$ ssh MACHINE_NAME
$ sudo ufw allo 8404/tcp
$ sudo ufw enable

# APIを有効化
$ cd; cd ylabgpu/
$ ./3-1_screen_api_activate.sh
~~~
=> APIを有効化したら，アドレスを指定してアクセスできるか確認
~~~
# MBAでOK
$ nc -vz IP_ADDRESS 8404
~~~

以上
