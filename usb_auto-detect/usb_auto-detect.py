#!/usr/bin/python3

import argparse
import os

usb_dev_path = '/sys/bus/usb/devices/'

def usb_dev_list():
    dev_list = [[], []]
    for bus in os.listdir(usb_dev_path):
        if 'usb' in bus: 
            for root, dirs, files in os.walk(os.path.join(usb_dev_path, bus)):
                if 'dev' in files:
                    with open(os.path.join(root, 'uevent')) as fd1:
                        for param in fd1.readlines():
                            param = param.strip().split('=')
                            key =  param[0]
                            value = param[1]
                            if (key == 'DEVNAME') and ('bus' not in value):
                                dev_path = os.path.join('/dev/', value)
                                dev_list[0].append(dev_path)
                                with open(os.path.join(root, 'device', 'uevent')) as fd2:
                                    for param in fd2.readlines():
                                        param = param.strip().split('=')
                                        key = param[0]
                                        value = param[1]
                                        if 'NAME' in key:
                                            dev_name = value
                                            dev_list[1].append(dev_name)
    return dev_list

print(usb_dev_list())

        