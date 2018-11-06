import os
import sys
import colorama
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
   7-) Md5 oluşturucu                     
   8-) Md5 kırıcı               
   9-) Reboot
   0-) Çıkış
   """)

def home():  
    update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN))

        
    if update == "1":
        os.system("apt-get update && apt-get upgrade && apt -y install exploitdb && apt-get install apache2 && apt-get install net-tools && apt-get install ettercap-graphical && apt-get install git && apt-get install bettercap && apt-get install vim && apt-get install hydra && apt-get install zip && apt-get install set && apt-get install macchanger && dpkg --add-architecture i386 && apt-get install wine && apt-get install figlet && apt-get install cmatrix && apt-get install python3-tk && apt-get install python3-pip && pip install colorama && apt-get install dmitry && apt-get install dirb && apt-get install nikto && apt-get install wafw00f && apt-get install telnet && apt-get install ftp && apt-get install whois && apt-get install hydra && apt-get install ssh && apt-get install whatweb && apt-get install gobuster && apt-get install theharvester && apt-get install cewl && apt-get install urlcrazy && apt-get install hydra && apt-get install websploit && apt-get update--fix-missing")
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Güncellemeler ve ek paketler başarı ile yüklendi..."))

    #2
    if update == "2":
        update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "İnterface girin" + Fore.WHITE + ":"))
        
        if update == "wlan0":
            os.system("ifconfig wlan0 down")
            os.system("macchanger -r wlan0")
            os.system("service networking restart")
            os.system("service network-manager restart")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "wlan0 mac adresi değiştirildi !"))
            
        if update == "wlan1":
            os.system("ifconfig wlan1 down")
            os.system("macchanger -r wlan1")
            os.system("service networking restart")
            os.system("service network-manager restart")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "wlan1 mac adresi değiştirildi !"))
        
        if update == "eth0":
            os.system("ifconfig eth0 down")
            os.system("macchanger -r eth0")
            os.system("service networking restart")
            os.system("service network-manager restart")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "eth0 mac adresi değiştirildi !"))
   
    #3        
    if update == "3":
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Nmap açılıyor !"))
        os.system("nmap 192.168.1.1/24")
    #4
    if update == "4":
        os.system("sqlmap")
    #5
    if update == "5":
        update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Msfconsole için data base oluşturulsunmu ? [E/h]:"))
        if update == "E" or "e":
            os.system("service postgresql start")
            os.system("msfdb init")
            print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Data base oluşturuldu..."))
            
            os.system("msfconsole")
 

    #9
    if update == "9":
        os.system("reboot")
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Bilgisayar kapatılıryor..."))

    #0    
    if update == "0":
        sys.exit()
home()


