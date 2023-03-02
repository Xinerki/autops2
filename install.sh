# im not good at sh lol
cp autops2.service /home/deck/.config/systemd/user/autops2.service
systemctl --user daemon-reload
systemctl --user start autops2