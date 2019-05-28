#!/usr/bin/python3

import argparse
import os

usb_dev_path = '/sys/bus/usb/devices/'

parser = argparse.ArgumentParser(description='Search for all USB devices.')
parser.add_argument('-l', '--list', action='store_true',
                  help='showing list of all devices')
parser.add_argument('-f', '--find', type=str, metavar = 'NAME',
                  help='show all matching devices')
args = parser.parse_args()

def usb_dev_list(out = False):
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
                                            dev_name = value.strip('/"')
                                            dev_list[1].append(dev_name)
    if out:
        for i in range(len(dev_list[0])):
            print('{}: {}'.format(dev_list[0][i], dev_list[1][i]))
    return dev_list

def find_usb_dev (dev_name, out = False):
    dev_list = usb_dev_list(False)
    index = []
    for i in range(len(dev_list[0])):
        if dev_name.lower() in dev_list[1][i].lower():
            index.append(i)
    if len(index) == 0:
        print('No matching USB devices found')
        return None
    if out:
        print('Found {} matching result:'.format(len(index)))
        for i in index:
            print('{}: {}'.format(dev_list[0][i], dev_list[1][i]))
    return [(dev_list[0][i], dev_list[1][i]) for i in index]


if args.list:
    usb_dev_list(out = True)
if args.find:
    find_usb_dev(args.find, out = True)




        