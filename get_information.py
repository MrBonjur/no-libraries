########################################################################
#                       Get information about PC                       #
#                      18.03.2022 create MrBonjur                      #
#    * Output:                                                         #
#        user: Hello                                                   #
#        user domain: DESKTOP-KMTQRLO                                  #
#        cpu: AMD FX(tm)-8320 Eight-Core Processor                     #
#        cpu family: AMD64 Family 21 Model 2 Stepping 0, AuthenticAMD  #
#        gpu: ASUS R7 250X Series                                      #
#        names disks: ['WD-WMC6M0J5H5F2']                              #
#        windows version: 10                                           #
#        monitor size: [1920, 1080]                                    #
########################################################################

import subprocess
import getpass
import winreg
import platform
import ctypes
import os


def get_user() -> str:
    return getpass.getuser()


def get_user_domain() -> str:
    return os.environ["USERDOMAIN"]


def get_cpu_name() -> str:
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(reg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
    return winreg.QueryValueEx(key, 'ProcessorNameString')[0].strip()


def get_cpu_family() -> str:
    return platform.processor()


def get_gpu() -> str:
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\WinSAT")
    return winreg.QueryValueEx(key, 'PrimaryAdapterString')[0].strip()


def get_names_disks() -> list:
    serials = subprocess.check_output('wmic diskdrive get SerialNumber').decode().split('\n')[1:]
    return [s.strip() for s in serials if not s.strip().isdigit() and s.strip()]


def get_windows_version() -> int:
    return int(platform.release())


def get_monitor_size() -> list:
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    return [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


user = get_user()
user_domain = get_user_domain()
cpu = get_cpu_name()
cpu_family = get_cpu_family()
gpu = get_gpu()
names_disks = get_names_disks()
windows_version = get_windows_version()
monitor_size = get_monitor_size()

print(f"user: {user}")
print(f"user domain: {user_domain}")
print(f"cpu: {cpu}")
print(f"cpu family: {cpu_family}")
print(f"gpu: {gpu}")
print(f"names disks: {names_disks}")
print(f"windows version: {windows_version}")
print(f"monitor size: {monitor_size}")
