import subprocess
import time
import os

os.system('clear')

KIRMIZI = "\033[91m"
YESIL = "\033[32m"
NORMAL = "\033[0m"

logo = r"""     █████

    █████████   ██████   ██████ ██████████
   ███▒▒▒▒▒███ ▒▒██████ ██████ ▒▒███▒▒▒▒▒█
  ▒███    ▒███  ▒███▒█████▒███  ▒███  █ ▒ 
  ▒███████████  ▒███▒▒███ ▒███  ▒██████   
  ▒███▒▒▒▒▒███  ▒███ ▒▒▒  ▒███  ▒███▒▒█   
  ▒███    ▒███  ▒███      ▒███  ▒███ ▒   █
  █████   █████ █████     █████ ██████████
 ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒ """

for satir in logo.splitlines():
    print(KIRMIZI + satir + NORMAL, flush=True)
    time.sleep(0.04)

print(YESIL + "\n[!] Sistem Aktif ! [!]" + NORMAL)
print(NORMAL + "--- Ağ Keşif Aracı ---")

def komut_calistir(komut):
    print(YESIL + f"\n[+] Çalıştırılıyor: {komut}" + NORMAL)
    try:
        sonuc = subprocess.check_output(komut, shell=True)
        return sonuc.decode('utf-8')
    except:
        return None

ag_bilgisi = komut_calistir("ip addr")
if ag_bilgisi:
    print(ag_bilgisi)

wifi_listesi = komut_calistir("nmcli dev wifi")
if wifi_listesi and wifi_listesi.strip():
    print(wifi_listesi)
else:
    print(KIRMIZI + "[!] WiFi kartı tespit edilemedi!" + NORMAL)