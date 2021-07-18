import os
import time
#İşletim sistemi kontrolü:
if os.name == "nt":
    print("BetterSS, NT çekirdeğini kullanan işletim sistemlerinde (Windows, ReactOS) çalışmaz.")
    print("BetterSS Installer kapatılıyor.")
    time.sleep(3)
    exit()
#Pisi GNU/Linux için:
if os.path.isfile('/etc/pisilinux-release'):
    print("BetterSS'e hoşgeldiniz!")
    islem = input("Lütfen yapmak istediğiniz işlemi seçiniz(ekran görüntüsü/bilgi/çıkış):")
    if islem == "ekran görüntüsü":
        os.system("spectacle")    
        exit()
    elif islem == "bilgi":
        print("BetterSS kullandığınız GNU/Linux dağıtımında daha kolay ekran görüntüsü almanızı hedefleyen özgür bir yazılımdır.\nLisans: GPL 3.0")  
        onay = input('Siz "evet" yazdığınız an program kapatılacaktır:')
        if onay == "evet":
            exit()
        else:
            print("Geçersiz bir cevap girdiniz, BetterSS kapatılıyor.")
            time.sleep(3)
            exit()  
    elif islem == "çıkış":
        exit()
    else:
        print("Geçersiz bir cevap girdiniz. BetterSS kapatılıyor.")
        time.sleep(3)
        exit()
#Debian, Fedora için:
else:
    from tkinter import *
def ss():
    if os.path.isfile('/etc/debian_version'):
        os.system("flameshot gui")
        exit()
    elif os.path.isfile('/etc/fedora-release'):
        os.system("flameshot gui")
        exit()
    else:
        metin1.config(text="Kullandığınız GNU/Linux veya Linux dağıtımını BetterSS desteklemiyor.\nBetterSS kapatılıyor.")   
        time.sleep(3)
        exit() 
def info():
    metin1.config(text="BetterSS kullandığınız GNU/Linux dağıtımında daha kolay ekran görüntüsü almanızı hedefleyen özgür bir yazılımdır.\nLisans: GPL 3.0")
    buton.config(text="Ekran görüntüsü al.",command=ss)
    buton1.config(text="Programı kapat",command=kapat)
    buton2.destroy()
def kapat():
    exit()
pencere=Tk()
pencere.title("BetterSS")

metin=Label(pencere)
metin.config(text="BetterSS programına hoşgeldiniz!\nBaşınıza gelebilecek herhangi bir durumda sorumluluk almayacağımızı belirtiriz.")
metin.pack()

metin1=Label(pencere)
metin1.config(text="BetterSS'de ne yapmak istersiniz?")
metin1.pack()

buton=Button(pencere)
buton.config(text="Ekran görüntüsü al.",command=ss)
buton.pack()

buton1=Button(pencere)
buton1.config(text="Bilgi",command=info)
buton1.pack()

buton2=Button(pencere)
buton2.config(text="Programı kapat",command=kapat)
buton2.pack()
mainloop()
