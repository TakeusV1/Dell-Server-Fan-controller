## YOU NEED "ipmitool" installed on your system... (Windows)
import os

# Idrac IP
idrac_ip = 'xx.xx.xx.xx'
# Idrac user & password
idrac_user = 'root'
idrac_pass = 'somepassword'
# C:\Program Files\Dell\SysMgt\iDRACTools\IPMI
ipmitool_path = "C:\Program Files\Dell\SysMgt\iDRACTools\IPMI"

while True:
    try:
        os.system('cls')
        print('Desired fan speed (in %)\n')
        temp = input('(0-100) > ')
        temp = int(temp)
        if temp < 0 or temp > 100:
            print('Value between 0 and 100 !!!!')
        else:
            os.chdir(ipmitool_path)
            os.system(f'ipmitool -I lanplus -H {idrac_ip} -U {idrac_user} -P {idrac_pass} raw 0x30 0x30 0x02 0xff {hex(temp)}')
            print(f'The fan speed has been set to {temp}%')
            if input('(nothing/close) > ') == 'close':
                break
    except:
        print('only int argument !!!!!!!!')

# https://www.reddit.com/r/homelab/comments/7xqb11/dell_fan_noise_control_silence_your_poweredge/