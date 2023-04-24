# WebAPIを動作させるためのライブラリ
from fastapi import FastAPI
import uvicorn
# M5stickとシリアル通信を行うためのライブラリ
import serial
import os

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
        return {"strings": "1バイト文字で入力してください(例 : 太郎 -> tarou)"}
    ser = serial.Serial(ttyNo, 115200, timeout=1)
    ser.write(str.encode())
    print(str)
    return {"strings": str}

ttyNo = getM5Tty()