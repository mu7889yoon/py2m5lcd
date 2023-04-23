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

ttyNo = getM5Tty()

# getで受け取った文字列をM5stickに送信する
@app.get("/send/{str}")
def sendtr(str: str):
    ser = serial.Serial(ttyNo, 115200, timeout=1)
    ser.write(str.encode())
    return {"strings": str}

