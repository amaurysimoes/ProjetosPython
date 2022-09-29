import os

import wmi
c = wmi.WMI()

for item in c.Win32_PhysicalMedia():
    print(item)

for drive in c.Win32_DiskDrive():
    print(drive)

for disk in c.Win32_LogicalDisk():
    print(disk)

os.system('pause')