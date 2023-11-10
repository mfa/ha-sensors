## glances

notes for glances integration

### install

packages to install on the system I want to monitor which is running archlinux

Packages:
```
sudo pacman -S glances python-bottle python-dateutil
# gpu support
sudo yay -S python-py3nvml
```

edit/start systemd config
```
sudo cp /usr/lib/systemd/system/glances.service /etc/systemd/system/multi-user.target.wants/glances.service
# change "glances -s" to "glances -w"
sudo vim /etc/systemd/system/multi-user.target.wants/glances.service
sudo systemctl daemon-reload
sudo systemctl start glances
```

### open issues

- gpu support is currently missing in homeassistant
