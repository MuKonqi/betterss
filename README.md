# BetterSS
Basit bir Flameshot ya da Spetacle başlatıcısı. 
____________________________________________________________________________________________________________________________________________________________________
BetterSS'i kurarken BetterSS Installer size yardım edecektir. BetterSS Installer'i kurmak için şunu yapabilirsiniz:

Elle:
1. https://github.com/MuKonqi/BetterSS/blob/main/Files/installer.py
2. Buradaki dosyayı kaydedin ya da terminalde yeni bir dosya oluşturun:
```touch installer.py```
3. Dosyayı oluşturunca verdiğim bağlantıdaki kodları installer.py dosyasına yapıştırın.
4. ```sudo python3 installer.py``` yazın ve böylece BetterSS Installer bilgisayarınıza BetterSS'i kursun!

Terminalden:
1. **Eğer Debian tabanlı** GNU/Linux dağıtımı kullanıyorsanız:
 ```sudo apt install git -y && git clone https://github.com/MuKonqi/BetterSS.git && cd BetterSS/Files && sudo python3 installer.py```
Bunları yazınca BetterSS Installer, bilgisayarınıza BetterSS'i kuracaktır!
2. **Eğer Fedora tabanlı** GNU/Linux dağıtımı kullanıyorsanız:
```sudo dnf install git -y && git clone https://github.com/MuKonqi/BetterSS.git && cd BetterSS/Files && sudo python3 installer.py```
Bunları yazınca BetterSS Installer, bilgisayarınıza BetterSS'i kuracaktır!
3. **Eğer Pisi GNU/Linux tabanlı** GNU/Linux dağıtımı kullanıyorsanız:
```sudo pisi it git -y && git clone https://github.com/MuKonqi/BetterSS.git && cd BetterSS/Files && sudo python3 installer.py```
Bunları yazınca BetterSS Installer, bilgisayarınıza BetterSS'i kuracaktır!
____________________________________________________________________________________________________________________________________________________________________
Özellikler:
1. GUI arayüzde yani Tkinter'da, Debian ile Fedora tabanlı platform desteği.
2. CLI arayüzde, Pisi GNU/Linux desteği.
3. Kendisine has kurucu.
4. Tam Türkçe desteği.
