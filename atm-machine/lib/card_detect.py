import os, string, time
from ctypes import windll
import config

def get_driveStatus():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()  # The GetLogicalDrives function retrieves a bitmask
    # representing the currently available disk drives.
    for label in range(26):  # The uppercase letters 'A-Z'
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices


def detect_device():
    original = set(get_driveStatus())
    print('Please insert or re-insert your card...')
    time.sleep(2)
    add_device = set(get_driveStatus()) - original
    if (len(add_device)):
        # print("There were %d" % (len(add_device)))
        for drive in add_device:
            # print("The drives added: %s." % (drive+65))
            return drive + 65
    else:
        return 0

def detect_remove():
    original = set(get_driveStatus())
    print('Please remove your card...')
    time.sleep(2)
    subt_device = original - set(get_driveStatus())
    if (len(subt_device)):
        for drive in subt_device:
            return drive + 65
    else:
        return 0

def check_removable(mode):
    if mode == "1":
        while True:
            drive = detect_device()
            if drive != 0:
                return chr(drive)

    else:
        while True:
            drive = detect_remove()
            if drive != 0:
                return drive


def is_card_exist(drive):
    return 1 if os.path.exists(drive+":\\"+config.FILE_NAME) else 0


