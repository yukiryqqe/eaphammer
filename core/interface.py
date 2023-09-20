import os
import time
from . import utils

class Interface:
    def __init__(self, interface):
        self.interface = interface

    def up(self):
        print(f'[*] Bringing {self.interface} up...')
        os.system(f'ip link set {self.interface} up')
        print('[*] Complete!')
        time.sleep(0.5)

    def down(self):
        print(f'[*] Bringing {self.interface} down...')
        os.system(f'ip link set {self.interface} down')
        print('[*] Complete!')
        time.sleep(0.5)

    def mode_monitor(self):
        print(f'[*] Placing {self.interface} into monitor mode...')
        os.system(f'iw dev {self.interface} set type monitor')
        print('[*] Complete!')
        time.sleep(0.5)

    def mode_managed(self):
        print(f'[*] Placing {self.interface} into managed mode...')
        os.system(f'iw dev {self.interface} set type managed')
        print('[*] Complete!')
        time.sleep(0.5)

    def nm_off(self):
        print('[*] Reticulating radio frequency splines...')
        os.system(f'nmcli device set {self.interface} managed no')
        utils.sleep_bar(1, f'[*] Using nmcli to tell NetworkManager not to manage {self.interface}...')
        print(f'[*] Success: {self.interface} no longer controlled by NetworkManager.')

    def nm_on(self):
        os.system(f'nmcli device set {self.interface} managed yes')
        utils.sleep_bar(1, f'[*] Using nmcli to give NetworkManager control of {self.interface}...')
        print(f'[*] Success: {self.interface} is now managed by NetworkManager.')

    def set_ip_and_netmask(self, ip, netmask):
        os.system(f'ifconfig {self.interface} {ip} netmask {netmask}')

    def __str__(self):
        return self.interface
