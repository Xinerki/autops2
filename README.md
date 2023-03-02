# autops2

# **this readme is far from done btw!!!**

### Automatically boot into PS2 disks using PCSX2!!
Made with the power of sheer anger. Sponsored (this is a joke) by CEX in Zaandam, NL.

# Installation
- TODO: does deck come with python3?
- TODO: it definitely doesnt come with pyudev for sure
- Install `pcsx2` from pacman **(NOT FLATPAK!!!)**
    - preferrably, set up [rwfus](https://github.com/ValShaped/rwfus) beforehand instead of disabling the read-only mode.
- Clone the repo to `~/autops2`
- TODO: add pcsx2 to steam
- TODO: get pcsx2 non-steam gameid
- TODO: edit script to the id

## Quick/temporary method:
This method will not persist after system reboot or after you close your terminal
- Open your terminal of choice
- Navigate to `~/autops2`, probably by just doing `cd ~/autops2`
- Run `python3 autops2.py`
    - or run `nohup python3 autops2.py` so you can close the terminal without worrying, might not persist going from desktop to gamemode though

## Service method:
This method makes the autops2 script run on startup (and easily restart it)

i think install.sh does this for you but just in case:
- Copy the autops2 service file to systemd stuff
```bash
cp autops2.service /home/deck/.config/systemd/user/autops2.service
```
- Reload the units
```bash
systemctl --user daemon-reload
```

- Start the service
```bash
systemctl --user start autops2
```