pip3 install -r requirements.txt
python3 -m venv venv
source venv/bin/active
sudo cp run.service /etc/systemd/system
sudo systemctl enable run.service
sudo systemctl restart run.service