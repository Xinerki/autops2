from pyudev import Context, Monitor
import subprocess
import os

while True:
	# print("polling")
	context = Context()
	monitor = Monitor.from_netlink(context)
	device = monitor.poll(timeout=None)
	if device:
		if device.sys_name == "sr0":
			# print("{0.action} on {0.sys_name}".format(device))
			# for x in device:
			# 	print("{0}: {1}".format(x, device[x]))
			if 'DISK_EJECT_REQUEST' in device:
				print("disk ejected")
			elif 'ID_CDROM_MEDIA' in device:
				print("ID_FS_LABEL: {0}".format(device['ID_FS_LABEL']))
				# if os.path.exists('SYSTEM.CNF'):
				# 	os.remove('SYSTEM.CNF')
				cnf = os.popen("7z e -so /dev/sr0 'SYSTEM.CNF'").read().splitlines()
				for line in cnf:
					if line[0:5] == 'BOOT2':
						print("it's ps2!!")
				# os.system("7z e /dev/sr0 'SYSTEM.CNF' -r")
				# if os.path.exists("SYSTEM.CNF"):
				# 	f = open("SYSTEM.CNF", 'r')
				# 	for line in f:
				# 		if line[0:5] == 'BOOT2':
				# 			print("it's ps2!!")
				# 	f.close()
				# 	os.remove('SYSTEM.CNF')
				# else:
				# 	print("not a ps2!!")
			#print('{0.action}: {0}'.format(device))
