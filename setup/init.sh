#!/bin/bash

# Modify : 2023/04/19 v1.0.0
# Author : @mu7889yoon

# Update Package
sudo apt update
sudo apt install -y git python3-pip cockpit
# Clone Repository
git clone -b Validation https://github.com/mu7889yoon/py2m5lcd.git
cd py2m5lcd
# Install Package
pip3 install -r requirements.txt
cd setup
# Setup Service
sudo cp uvicorn.service /etc/systemd/system/
sudo systemctl enable uvicorn.service
sudo systemctl start uvicorn.service
sudo systemctl enable cockpit.service
sudo systemctl start cockpit.service
# Test LCDにSetup completeを表示
curl http://localhost:8080/send/Setup%20Complete



