# M5stickCのLCDをWeb APIで操作する

## ファイル構造

```
├── setup
│   ├── init.sh             # Raspberry Piのセットアップファイル
│   └── uvicorn.service     # uvicornをデーモン化するためのファイル
├── m5stick
│   └── recvStr.ino         # M5stickのLCDを操作するファイル
├── sendStr.py              # M5stickに文字列を送信するファイル
├── requirements.txt        # 必要なパッケージのリスト
├── README.md               # 本ファイル
└── .gitignore              # gitで管理しないファイルのリスト
```

## セットアップ手順
### Raspberry Piのセットアップ
1. Raspbperr Pi imagerを起動する。
2. Raspberry Pi OS (32-bit) Liteを選択する。
3. 歯車のアイコンから、詳細設定を行う。
4. ホストネームを設定する。(ex, Y611-1, Y611-2など)
5. SSHを有効にする。
6. ユーザー名をpi、パスワードもpiに設定する。
7. 書き込みを行う。
待っている間に、[m5stickのセットアップ](#M5stickのセットアップ)を行う。
8. 書き込みが完了したら、Raspberry PiにSDカードを挿入する。
9. Raspberry PiとM5stickをUSBで接続し、Raspberry Piの電源を入れる。
9. SSH で Raspberry Pi にログインする。
10. 以下のコマンドを実行し、セットアップを開始する。
```
$ wget https://raw.githubusercontent.com/mu7889yoon/py2m5lcd/setup/init.sh
$ bash init.sh
```
11. M5stickCのLCDに、```Setup Complete```と表示されたら、セットアップ完了。

### M5stickのセットアップ
1. 本リポジトリのm5stickディレクトリにあるrecvStr.inoをArduino IDEで開く。
2. Arduino IDEのツールから、recvStr.inoを書き込む。
3. 完了