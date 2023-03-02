from pyudev import Context, Monitor
import subprocess
import os

isDeck = False
gameId = 9645277480512126976

while True:
	context = Context()
	monitor = Monitor.from_netlink(context)
	device = monitor.poll(timeout=None)
	if device:
		if device.sys_name == "sr0":
			if 'DISK_EJECT_REQUEST' in device:
				print("disk ejected")
				# not a good way to do this lol
				# os.system("killall pcsx2-qt")
			elif 'ID_CDROM_MEDIA' in device:
				print("ID_FS_LABEL: {0}".format(device['ID_FS_LABEL']))
				cnf = os.popen("7z e -so /dev/sr0 'SYSTEM.CNF'").read().splitlines()
				for line in cnf:
					if line[0:5] == 'BOOT2':
						if isDeck:
							subprocess.call(["steam", "steam://rungameid/{0}".format(gameId)])
						else:
							subprocess.call(["pcsx2-qt", "-batch", "-nogui", "-bigpicture", "-fullscreen", "-disc", "/dev/sr0"])
							# subprocess.call("pcsx2-qt -bigpicture -fullscreen -disc /dev/sr0", shell=True)
