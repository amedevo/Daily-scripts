import subprocess
import time
import os

os.system('clear')

RED = "\033[91m"
GREEN = "\033[32m"
RESET = "\033[0m"

logo = r"""     █████

    █████████   ██████   ██████ ██████████
   ███▒▒▒▒▒███ ▒▒██████ ██████ ▒▒███▒▒▒▒▒█
  ▒███    ▒███  ▒███▒█████▒███  ▒███  █ ▒ 
  ▒███████████  ▒███▒▒███ ▒███  ▒██████   
  ▒███▒▒▒▒▒███  ▒███ ▒▒▒  ▒███  ▒███▒▒█   
  ▒███    ▒███  ▒███      ▒███  ▒███ ▒   █
  █████   █████ █████     █████ ██████████
 ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒      ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒ """

for line in logo.splitlines():
    print(RED + line + RESET, flush=True)
    time.sleep(0.04)

print(GREEN + "\n[!] System Active! [!]" + RESET)
print(RESET + "--- Network Recon Tool ---")

def run_command(command):
    print(GREEN + f"\n[+] Executing: {command}" + RESET)
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8')
    except:
        return None

network_info = run_command("ip addr")
if network_info:
    print(network_info)

wifi_list = run_command("nmcli dev wifi")
if wifi_list and wifi_list.strip():
    print(wifi_list)
else:
    print(RED + "[!] WiFi card not detected!" + RESET)