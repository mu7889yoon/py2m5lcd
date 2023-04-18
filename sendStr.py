# WebAPIを動作させるためのライブラリ
from fastapi import FastAPI
import uvicorn
# M5stickとシリアル通信を行うためのライブラリ
import serial
import os

app = FastAPI()

# getで受け取った文字列をM5stickに送信する
@app.get("/send/{str}")
def sendtr(str: str):
    ser = serial.Serial('/dev/tty.usbserial-59529F6CAB', 115200, timeout=1)
    ser.write(str.encode())
    return {"message": "success"}
