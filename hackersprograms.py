import os
import sys
import colorama
from colorama import Fore

qkullanıcı = "bandolero"
qşifre = "bandolero123"

while (True):
    print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "-----------------------")) 
    kullanıcı = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "kullanıcı Adı :"))
    
    şifre = input((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Şifre :"))
    print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "-----------------------""")) 

    if ((qkullanıcı == kullanıcı) and (qşifre == şifre)):
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Hoşgeldiniz Efendim !"))
        break #şifre doğru girilene kadar tekrarlatır
    
    elif ((qkullanıcı != kullanıcı) and (qşifre != şifre)):
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Kullanıcı adı ve şifre yanlış !"))
        
    elif ((qkullanıcı == kullanıcı) and (qşifre != şifre)):
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Şifre yanlış girildi !"))
        
    elif ((qkullanıcı != kullanıcı) and (qşifre == şifre)):
        print((Fore.BLUE + "root@BandoLero" + Fore.WHITE + ":~# " + Fore.GREEN + "Kullanıcı yanlış girildi !"))



dosya = input("dosya oluşturulsunmu ? [E/h]:")
if dosya == "e":
    i = i
    while i < 10 :
        print("HACKED BY BANDOLERO!!!")
        os.system("mkdir bandolero")
