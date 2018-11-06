from tkinter import *
def donothing():
   filewin = Toplevel(pencere)
   button = Button(filewin, text="Hazır değil")
   button.pack()
   
pencere = Tk()
pencere.geometry("400x300")
pencere.title("Hacked By BandoLero")

menubar = Menu(pencere)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Yeni", command = donothing)
filemenu.add_command(label = "Aç", command = donothing)
filemenu.add_command(label = "Kaydet", command = donothing)
filemenu.add_command(label = "Farklı Kaydet...", command = donothing)
filemenu.add_command(label = "Kapat", command = donothing)
# filemenu.add_separator() menüde çizgi çekmeye yarar
filemenu.add_separator()

filemenu.add_command(label = "Çıkış", command = pencere.quit)
menubar.add_cascade(label = "Dosya", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Geri Al", command = donothing)

editmenu.add_command(label = "Kes", command = donothing)
editmenu.add_command(label = "Kopyala", command = donothing)
editmenu.add_command(label = "Yapıştır", command = donothing)
editmenu.add_command(label = "Sil", command = donothing)
editmenu.add_command(label = "Hepsini Seç", command = donothing)

menubar.add_cascade(label = "Düzenle", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Yardım Sayfası", command = donothing)
helpmenu.add_command(label = "Hakkımda...", command = donothing)
menubar.add_cascade(label = "Yardım", menu = helpmenu)
pencere.config(menu = menubar)

#butona basıldığında Giris Yapıldı yazsın
def giris():
    print("Giris Yapıldı!")
    pencere2 = Tk()
    pencere2.title("Kayıt")
    pencere2.geometry("200x150")
    isim = Label(pencere2,text="İsim:")
    sifre = Label(pencere2,text="Sifre:")
    email = Label(pencere2,text="E-mail")
    tel = Label(pencere2,text="Telefon")
    
    def scrollbar():

        import tkinter as tk
        from time import sleep

        from math import trunc

        from tkinter import ttk

        fileList = range(3)

        step = trunc(100/len(fileList))

        def MAIN():
            """Put your loop in here"""
            for fileName in fileList:
                sleep(1)

                print(fileName)

                progress.step(step)
                progress.update()

            pencere3.destroy()

        pencere3 = tk.Tk()

        progress = ttk.Progressbar(pencere3, length=100)
        progress.pack()

        progress.after(1, MAIN)

    
    buton2 = Button(pencere2,text="Giriş",command=scrollbar)

    isim2 = Entry(pencere2,width=10)
    sifre2 = Entry(pencere2,width=10,show="*")
    email2 = Entry(pencere2,width=10)
    tel2 = Entry(pencere2,width=10)
    cbutton = Checkbutton(pencere2,text="Beni Hatırla")

    isim.grid(row=0,column=0)
    sifre.grid(row=1,column=0)
    isim2.grid(row=0,column=1)
    sifre2.grid(row=1,column=1)
    email.grid(row=2,column=0)
    email2.grid(row=2,column=1)
    tel.grid(row=3,column=0)
    tel2.grid(row=3,column=1)
    cbutton.grid(row=4,columnspan=2)
    buton2.grid(row=5,column=0)

scrollbar = Scrollbar(pencere)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(pencere, yscrollcommand=scrollbar.set)

for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

buton = Button(pencere,text="kayıt",command=giris)
buton.pack()

pencere.mainloop()

