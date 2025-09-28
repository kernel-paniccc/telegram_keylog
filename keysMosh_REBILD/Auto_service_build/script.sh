#!/bin/bash

install_pip() {
    echo "Установка pip..."
    if command -v apt &> /dev/null; then
        sudo apt install -y python3 python3-pip
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3 python3-pip
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3 python3-pip
    else
        echo "Error"
        exit 1
    fi
}

install_pip

if command -v pip3 &> /dev/null; then
    echo "pip установлен успешно."
else
    echo "Ошибка установки pip."
    exit 1
fi


echo "Установка зависимостей из requirements.txt..."
pip3 install -r requirements.txt
pip3 install opencv-python pyzbar


sudo chmod +777 run.py

sudo cp hikk.service /etc/systemd/system

sudo systemctl daemon-reload
sudo systemctl enable hikk.service
sudo systemctl restart hikk.service

