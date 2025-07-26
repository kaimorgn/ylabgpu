#!/bin/bash
#
# send_to_wol.sh
#

# WOLを実行する関数（今回はテスト用にecho）
send_wol() {
    local mac_address="$1"

    # MACアドレスの形式チェック（12桁の16進数記号のみ許可）
    if [[ ! "$mac_address" =~ ^([A-Fa-f0-9]{2}[:-]){5}([A-Fa-f0-9]{2})$ ]]; then
        echo "Error: Invalid MAC address(Ex: AA:BB:CC:DD:EE:FF)"
        exit 1
    fi

    # テスト出力（実際の実行部分はechoで代替）
    echo "Send to Magick Packet: $mac_address"
    # wakeonlan "$mac_address"
}

# 実行部分（mainのような扱い）
if [ $# -ne 1 ]; then
    echo "USAGE: ./send_to_wol.sh <MAC_ADDRESS>"
    exit 1
fi

# 関数を呼び出す
send_wol "$1"
