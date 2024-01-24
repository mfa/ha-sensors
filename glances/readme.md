## glances

notes for glances integration

### install

#### archlinux

packages to install on the system I want to monitor which is running archlinux

Packages:
```
sudo pacman -S glances python-bottle python-dateutil
# gpu support
sudo yay -S python-py3nvml
```

edit/start systemd config
```
sudo cp /usr/lib/systemd/system/glances.service /etc/systemd/system/glances.service
# change "glances -s" to "glances -w"
sudo vim /etc/systemd/system/glances.service
sudo systemctl daemon-reload
sudo systemctl start glances
sudo systemctl enable glances
```

#### raspberry pi os

for a system running raspberry pi os to monitor different raspberry PIs

Packages:
```
sudo apt install glances python3-bottle python3-dateutil
# no gpu support needed
```

edit/start systemd config
```
# disable existing one
sudo systemctl stop glances
sudo systemctl disable glances
# copy the template
sudo cp /usr/lib/systemd/system/glances.service /etc/systemd/system/glances.service
# change "glances -s" to "glances -w" and remove the "-B 127.0.0.1"
sudo vim /etc/systemd/system/glances.service
sudo systemctl daemon-reload
sudo systemctl start glances
sudo systemctl enable glances
```


### open issues

- gpu support is currently missing in homeassistant
