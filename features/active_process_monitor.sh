#!/bin/bash

# 人間ユーザ（UID >= 1000，nologin以外）を抽出
users=$(awk -F: '($3>=1000)&&($7!~/nologin/) {print $1}' /etc/passwd)

# 全プロセス情報をJSONで取得
processes=$(ps -eo user,pid,%cpu,%mem,etime,comm | jc --ps -p)

# jqで対象ユーザのうち，cpu_percent >= 0.1 のものだけ抽出，空配列は除外
jq -n --argjson procs "$processes" --arg users "$users" '
  ($users | split("\n") | map(select(length > 0))) as $user_list |
  [$user_list[] as $u |
    $procs[] |
    select(.user == $u and (.cpu_percent | tonumber) >= 0.1)
  ]
'

