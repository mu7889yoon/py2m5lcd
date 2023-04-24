# WebAPIを動作させるためのライブラリ
from fastapi import FastAPI
import uvicorn
# M5stickとシリアル通信を行うためのライブラリ
import serial
import os
# ホストネームを取得するためのライブラリ
import socket
# ログを出力するためのライブラリ
from logging import getLogger
logger = getLogger(__name__)

app = FastAPI()

# M5stickのシリアルポート番号を取得する
def getM5Tty():
    for i in range(30):
        usbSerial = '/dev/ttyUSB{}'.format(i)
        if(os.path.exists(usbSerial)):
            print(usbSerial)
            return usbSerial
    return None

# 文字列のバリデーションを行う。Ascii文字のみ受け付ける
def validateStr(str):
    for c in str:
        if ord(c) > 127:
            return False
    return True

# getで受け取った文字列をM5stickに送信する
@app.get("/send/{str}")
def sendStr(str: str):
    if not validateStr(str):
        logger.warning("Invalid string : {}".format(str))
        return {"1バイト文字で入力してください(例 : 太郎 -> tarou)"}
    if ttyNo == None:
        logger.error("M5stick not found")
        return {"M5stickが見つかりませんでした、接続されているか確認してください。"}
    else:
        # ser = serial.Serial(ttyNo, 115200, timeout=1)
        # ser.write(str.encode())
        logger.info("Send string : {}".format(str))
        return {str}

ttyNo = getM5Tty()
sendStr(socket.gethostname())
logger.info("M5stick serial port : {}".format(ttyNo))
logger.info("Start Up Complete")