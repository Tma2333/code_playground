#!/bin/bash
# usb_auto-detect.bash

read target

for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev)
do
	syspath="${sysdevpath%/dev}"
	devname="$(udevadm info -q name -p $syspath)"
	[[ "$devname" == "bus/"* ]] && continue
	eval "$(udevadm info -q property --export -p $syspath)"
	[[ -z "$ID_SERIAL" ]] && continue
	if [[ $ID_SERIAL == *"$target"* ]]; then
		USBdev=$devname
        echo "$USBdev"
		break
	fi
done
