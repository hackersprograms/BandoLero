import os
import sys
import colorama
from tkinter import *
from colorama import Fore
print(Fore.GREEN +  """
                                                                                           
                                                 
                      
                      
                                                 #######################################################
                                                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                                                 #                      Hacked By                      #                
                                                 #                      BandoLero                      #
                                                 #          Komutları görmek için Help yazın           #
                                                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                                                 #######################################################
  
  
 






  
 
  -Program Özellikleri-
   1-) Güncellemeler                      
   2-) Mac değiştirme                 
   3-) Port Tarama                        
   4-) Sqlmap
   5-) Metasploit
   6-) Bettercap
   7-) Websploit                     
   8-) Düzenle               
   9-) Reboot
   0-) Çıkış
   """)

def home():  
    update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN))

        
    if update == "1":
        os.system("apt-get upgrade && apt-get update && apt --fix-broken install && apt-get install python-pip && apt-get install mplayer && apt-get install vlc && apt-get install apache2 && apt-get install net-tools && apt-get install ettercap-graphical && apt-get install git && apt-get install bettercap && apt-get install vim && apt-get install hydra && apt-get install zip && apt-get install set && apt-get install macchanger && apt-get install python3-tk && apt-get install python3-pip && apt-get install dmitry && apt-get install dirb && apt-get install nikto && apt-get install wafw00f && apt-get install telnet && apt-get install ftp && apt-get install whois && apt-get install ssh && apt-get install openssh-server && apt-get install whatweb && apt-get install theharvester && apt-get install cewl && apt-get install urlcrazy && apt-get install websploit && apt-get install wireshark && apt-get install netdiscover && apt-get install gimp && apt-get install apktool && apt-get install spyder3")
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Güncellemeler ve ek paketler başarı ile yüklendi..."))
        os.system("python3 def.py")

    #2
    if update == "2":
        update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "İnterface girin" + Fore.WHITE + ":"))
        
        if update == "wlan0":
            os.system("ifconfig wlan0 down")
            os.system("macchanger -r wlan0")
            os.system("service networking restart")
            os.system("service network-manager restart")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "wlan0 mac adresi değiştirildi !"))
            os.system("python3 def.py")

        if update == "wlan1":
            os.system("ifconfig wlan1 down")
            os.system("macchanger -r wlan1")
            os.system("service networking restart")
            os.system("service network-manager restart")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "wlan1 mac adresi değiştirildi !"))
            os.system("python3 def.py")

        if update == "eth0":
            os.system("ifconfig eth0 down")
            os.system("macchanger -r eth0")
            os.system("service networking restart")
            os.system("service network-manager restart")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "eth0 mac adresi değiştirildi !"))
            os.system("python3 def.py")
   
    #3        
    if update == "3":
        hedefip = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Hedef ip giriniz : "))
        os.system("nmap " + hedefip)
        update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Nmap ten çıkılsınmı ? [E/h]:"))
        os.system("python3 def.py")
    
    #4
    if update == "4":
        hedefip = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sqlmap : "))
        os.system("sqlmap " + hedefip )
        update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sqlmap ten çıkılsınmı ? [E/h] :"))
        os.system("python3 def.py")
    
    #5
    if update == "5":
        update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Msfconsole için data base oluşturulsunmu ? [E/h]:"))
        if update == "e":
            os.system("service postgresql start")
            os.system("msfdb init")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Data Base Oluşturuldu..."))
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Msfconsole Başlatılıyor..."))
            os.system("msfconsole")
            os.system("python3 def.py")

    #6
    if update == "6":
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Bettercap Başlatılıyor..."))
        os.system("bettercap")
        os.system("python3 def.py")

    #7
    if update == "7":
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Websploit Başlatılıyor..."))
        os.system("websploit")
        os.system("python3 def.py")

    #8
    if update == "8":
        os.system("vim def.py")
        os.system("python3 def.py")

    #9
    if update == "9":
        os.system("reboot")
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Bilgisayar kapatılıryor..."))

    #0    
    if update == "0":
        sys.exit()
home()


