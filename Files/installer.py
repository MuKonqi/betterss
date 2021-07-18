import os
import time
print("BetterSS Installer'a hoşgeldiniz!")
if os.name == "nt":
    print("BetterSS ve BetterSS Installer, NT çekirdeğini kullanan işletim sistemlerinde (Windows, ReactOS) çalışmaz.")
    print("BetterSS Installer kapatılıyor.")
    time.sleep(3)
    exit()
bilgi = input('Eğer "evet" yazarsanız bilgi komutu, "atla" yazarsanız bu bölüm pas geçilecektir(evet/atla/çıkış):')
if bilgi == "atla":
    print("Bilgi bölümü atlandı.")
elif bilgi == "evet":
    print("BetterSS Installer, BetterSS'i kurmanızı sağlayan bir araçtır.")
    print("Lisans: GPL 3.0")
    onay = input('Siz "evet" yazdığınız an program kapatılacaktır:')
    if onay == "evet":
        exit()
    else:
        print("Geçersiz bir cevap girdiniz, BetterSS Installer kapatılıyor.")
        time.sleep(3)
        exit()
elif bilgi == "çıkış":
    exit()
else:
    print("Geçersiz bir cevap girdiniz. BetterSS Installer kapatılıyor.")
    time.sleep(3)
    exit()
print("BetterSS kurulumu başlıyor!")
user="/home/"
user1 = input("Kuruluma başlanması için kullanıcı adınızı girmeniz gerekmektedir:")
user2="/Masaüstü/"
user3=user+user1+user2
user4="/Desktop/"
user5=user+user1+user4
if os.path.isfile('/etc/debian_version'):
    os.system("sudo apt install python3 python3-tk git flameshot -y")
    os.system("sudo git clone https://github.com/androidprotmmas/BetterSS.git")
    os.system("cd BetterSS/Files ; sudo mv BSS.py /usr/local/bin/ ; sudo mv desktop.png /usr/local/bin/ ; chmod +x BetterSS.desktop")
    try:
        os.system("cd BetterSS/Files ; sudo mv BetterSS.desktop "+user3)
    except:
        try:
            os.system(" cd BetterSS/Files; sudo mv BetterSS.desktop "+user5)
        except:
            print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
    print("Kurulum tamamlandı.") 
    print("BetterSS Installer kapatılıyor.")
    time.sleep(3)
    exit()
elif os.path.isfile('/etc/fedora-release'):
    os.system("sudo dnf install python3 python3-tkinter git flameshot -y")
    os.system("sudo git clone https://github.com/androidprotmmas/BetterSS.git")
    os.system("cd BetterSS/Files ; sudo mv BSS.py /usr/local/bin/ ; sudo mv desktop.png /usr/local/bin/ ; chmod +x BetterSS.desktop")
    try:
        os.system("cd BetterSS/Files ; sudo mv BetterSS.desktop "+user3)
    except:
        try:
            os.system(" cd BetterSS/Files; sudo mv BetterSS.desktop "+user5)
        except:
            print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
    print("Kurulum tamamlandı.") 
    print("BetterSS Installer kapatılıyor.")
    time.sleep(3)
    exit()
elif os.path.isfile('/etc/pisilinux-release'):
    os.system("sudo pisi it python3 python3-tk git spectacle -y")
    os.system("sudo git clone https://github.com/androidprotmmas/BetterSS.git")
    os.system("cd BetterSS/Files ; sudo mv BSS.py /usr/local/bin/ ; sudo mv desktop.png /usr/local/bin/ ; chmod +x BetterSS.desktop")
    try:
        os.system("cd BetterSS/Files ; sudo mv BetterSS.desktop "+user3)
    except:
        try:
            os.system(" cd BetterSS/Files; sudo mv BetterSS.desktop "+user5)
        except:
            print("Bazı hatalarla karşılaşıldı, kurulum yarıda kesildi.")
    print("Kurulum tamamlandı.") 
    print("BetterSS Installer kapatılıyor.")
    time.sleep(3)
    exit()
else:
    print("Kullandığınız GNU/Linux veya Linux dağıtımını BetterSS desteklemiyor.\nBetterSS kapatılıyor.")
    time.sleep(3)
    exit()
