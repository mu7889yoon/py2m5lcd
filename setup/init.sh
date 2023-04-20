#!/bin/bash

# Modify : 2023/04/19 v1.0.0
# Author : @mu7889yoon

# Update Package
sudo apt update
sudo apt install -y git python3-pip cockpit
git clone -b develop https://github.com/mu7889yoon/py2m5lcd.git
cd py2m5lcd
pip3 install -r requirements.txt
cd setup
sudo cp uvicorn.service /etc/systemd/system/
sudo systemctl enable uvicorn.service
sudo systemctl start uvicorn.service
sudo systemctl enable cockpit.service
sudo systemctl start cockpit.service




