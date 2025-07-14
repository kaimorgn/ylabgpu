#!/bin/bash

# 許可するポート番号
sudo ufw allow ssh
sudo ufw allow 8000/tcp
sudo ufw allow 8404/tcp

# ufwの状態を確認し，有効化またはリロードを実行する関数
enable_or_reload_ufw() {
    # 状態を取得（active or inactive）
    local status
    status=$(sudo ufw status verbose | grep "Status:" | awk '{print $2}')

    if [ "$status" = "active" ]; then
        echo "ufw is already active. Reloading rules..."
        sudo ufw reload
    else
        echo "ufw is not active. Enabling ufw..."
        sudo ufw --force enable
    fi
}

# 実行部
enable_or_reload_ufw
