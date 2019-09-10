import os
import sys
import colorama
from colorama import Fore
import time
import getpass

qroot = "bandolero"
qpasswd = "bandolero123"

user = input("User : ")
passwd = getpass.getpass("Passwd : ")

if ((qroot == user) and (qpasswd == passwd)):  
    print("Sistem yükleniyor...!")
    time.sleep(2)

elif ((qroot != user) and (qpasswd == passwd)):
    print("user yanlış")
    sys.exit()

elif ((qroot == user) and (qpasswd != passwd)):
    print("password yanlış")
    sys.exit()

elif ((qroot != user) and (qpasswd != passwd)):
    print("Siktir git !")
    sys.exit()

os.system("clear")
print(Fore.GREEN + """

                                                                                               
                                                     
                          
                          
                                                    #######################################################
                                                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                                                    #                      Hacked By                      #                
                                                    #                      BandoLero                      #
                                                    #          Komutları görmek için Help yazın           #
                                                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                                                    #######################################################















   
    -Sistem-
    1-) Linux
    2-) Windows
    3-) Android 
    
    
    
    """)
sistem = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sistem Sec : ")

if sistem == "1":
    print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sistem Yükleniyor!")
    time.sleep(2)

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
        linux = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN)

            
        if linux == "1":
            os.system("apt-get upgrade && apt-get update && apt-get install ftp")
            print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Güncellemeler ve ek paketler başarı ile yüklendi...")
            os.system("python3 script.py")

        #2
        if linux == "2":
            mac = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "İnterface girin" + Fore.WHITE + ":")
            
            if mac == "wlan0":
                os.system("ifconfig wlan0 down")
                os.system("macchanger -r wlan0")
                os.system("service networking restart")
                os.system("service network-manager restart")
                print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "wlan0 mac adresi değiştirildi !")
                os.system("python3 script.py")

            if mac == "wlan1":
                os.system("ifconfig wlan1 down")
                os.system("macchanger -r wlan1")
                os.system("service networking restart")
                os.system("service network-manager restart")
                print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "wlan1 mac adresi değiştirildi !")
                os.system("python3 script.py")

            if mac == "eth0":
                os.system("ifconfig eth0 down")
                os.system("macchanger -r eth0")
                os.system("service networking restart")
                os.system("service network-manager restart")
                print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "eth0 mac adresi değiştirildi !")
                os.system("python3 script.py")
       
        #3        
        if linux == "3":
            hedefip = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Hedef ip giriniz : ")
            os.system("nmap " + hedefip)
            update = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Nmap ten çıkılsınmı ? [E/h]:")
            os.system("python3 script.py")
        
        #4
        if linux == "4":
            sqlmap = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sqlmap : ")
            os.system("sqlmap " + hedefip )
            update = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sqlmap ten çıkılsınmı ? [E/h] :")
            os.system("python3 script.py")
        
        #5
        if linux == "5":
            msfconsole = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Msfconsole için data base oluşturulsunmu ? [E/h]:")
            if msfconsole == "e":
                os.system("service postgresql start")
                os.system("msfdb init")
                print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Data Base Oluşturuldu..."))
                print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Msfconsole Başlatılıyor..."))
                os.system("msfconsole")
                os.system("python3 script.py")

        #6
        if linux == "6":
            print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Bettercap Başlatılıyor...")
            os.system("bettercap")
            os.system("python3 script.py")

        #7
        if linux == "7":
            print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Websploit Başlatılıyor...")
            os.system("websploit")
            os.system("python3 script.py")

        #8
        if linux == "8":
            os.system("vim script.py")
            os.system("python3 script.py")

        #9
        if linux == "9":
            os.system("reboot")
            print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Bilgisayar Yeniden Başlatılıyor...")

        #0    
        if linux == "0":
            sys.exit()
    home()

#windows
if sistem == "2":
    print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sistem Yükleniyor!")
    time.sleep(2)
    print("windows")

#android
if sistem == "3":
    print(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Sistem Yükleniyor!")
    time.sleep(2)
    os.system("clear")
    
print(Fore.GREEN +  """
                                                                                               
                                                     
                          
                          
#################################################~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                  Hacked By                   ##                  BandoLero                   ##       Komutları görmek için Help yazın       #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#################################################
   




   
    -Programlar-
    1-) Güncellemeler                      
    2-) msfconsole                 
    3-) nmap                        
    4-) 
    5-) 
    6-) 
    7-)                      
    8-)             
    9-) Reboot
    0-) Çıkış 
    
    
    
    """)

android = input(Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + " : ")

if android == "1":
    if android == "1":
        os.system("apt-get update && apt-get upgrade && pkg install python3 && pkg install python2 && pkg install unstable-repo && pkg install metasploit && pkg install nmap && apt install root-repo && apt install aircrack-ng")

    if android == "2":
        os.system("msfconsole")
    
    if android == "3":
        hedefip = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Hedef ip giriniz : "))
        os.system("nmap " + hedefip)
        update = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Nmap ten çıkılsınmı ? [E/h]:"))
        os.system("python3 script.py")
