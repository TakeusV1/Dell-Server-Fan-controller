## YOU NEED "ipmitool" installed on your system... (Windows)
from os import system
import subprocess
# Idrac IP
idrac_ip = 'xx.xx.xx.xx'
# Idrac user & password
idrac_user = 'root'
idrac_pass = 'somepassword'
# C:\Program Files\Dell\SysMgt\iDRACTools\IPMI
ipmitool_path = "C:\Program Files\Dell\SysMgt\iDRACTools\IPMI"

while True:
    try:
        system('cls')
        print(f"""
## DELL SERVER FAN SPEED CONTROLLER
------------
Hostname: {subprocess.check_output(f'ipmitool -I lanplus -H {idrac_ip} -U {idrac_user} -P {idrac_pass} mc getsysinfo system_name',  cwd=f'{ipmitool_path}').decode("utf-8")}Bios version: {subprocess.check_output(f'ipmitool -I lanplus -H {idrac_ip} -U {idrac_user} -P {idrac_pass} mc getsysinfo system_fw_version',  cwd=f'{ipmitool_path}').decode("utf-8")}Operating system: {subprocess.check_output(f'ipmitool -I lanplus -H {idrac_ip} -U {idrac_user} -P {idrac_pass} mc getsysinfo primary_os_name',  cwd=f'{ipmitool_path}').decode("utf-8")}========================
Desired fan speed (in %)
        """)

        temp = input('(0-100) > ')
        temp = int(temp)
        if temp < 0 or temp > 100:
            print('Value between 0 and 100 !!!!')
        else:
            subprocess.run(f'ipmitool -I lanplus -H {idrac_ip} -U {idrac_user} -P {idrac_pass} raw 0x30 0x30 0x01 0x00',cwd=f'{ipmitool_path}')
            subprocess.run(f'ipmitool -I lanplus -H {idrac_ip} -U {idrac_user} -P {idrac_pass} raw 0x30 0x30 0x02 0xff {hex(temp)}',cwd=f'{ipmitool_path}')
            print(f'The fan speed has been set to {temp}%\n')
            response = input('(nothing/reset/close) > ')
            if response == 'close':
                break
            elif response == 'reset':
                subprocess.run(f'ipmitool -I lanplus -H {idrac_ip} -U {idrac_user} -P {idrac_pass} raw 0x30 0x30 0x01 0x01',cwd=f'{ipmitool_path}')
    except:
        print('only int argument !!!!!!!!')

## BASED ON https://www.reddit.com/r/homelab/comments/7xqb11/dell_fan_noise_control_silence_your_poweredge/