# BetterSS
Son kullanıcının daha iyi ekran görüntüsü alması için tasarlandı.
____________________________________________________________________________________________________________________________________________________________________
BetterSS'i kurarken BetterSS Installer size yardım edecektir. BetterSS Installer'i kurmak için şunu yapabilirsiniz:

Elle:
1. https://github.com/androidprotmmas/BetterSS/blob/main/Files/installer.py
2. Buradaki dosyayı kaydedin ya da terminalde yeni bir dosya oluşturun:
```touch installer.py```
3. Dosyayı oluşturunca verdiğim bağlantıdaki kodları installer.py dosyasına yapıştırın.
4. ```sudo python3 installer.py``` yazın ve böylece BetterSS Installer bilgisayarınıza BetterSS'i kursun!

Terminalden:
1. **Eğer Debian tabanlı** GNU/Linux dağıtımı kullanıyorsanız:
```sudo apt install git && git clone https://github.com/androidprotmmas/BetterSS.git && cd BetterSS/Files && sudo python3 installer.py```
2. **Eğer Fedora tabanlı** GNU/Linux dağıtımı kullanıyorsanız:
```sudo dnf install git && git clone https://github.com/androidprotmmas/BetterSS.git && cd BetterSS/Files && sudo python3 installer.py```
3. **Eğer Pisi GNU/Linux tabanlı** GNU/Linux dağıtımı kullanıyorsanız:
```sudo pisi it git && git clone https://github.com/androidprotmmas/BetterSS.git && cd BetterSS/Files && sudo python3 installer.py```
____________________________________________________________________________________________________________________________________________________________________
Özellikler:

GUI arayüzde yani Tkinter'da, Debian ile Fedora tabanlı platform desteği.

CLI arayüzde, Pisi GNU/Linux desteği.

Kendisine has kurucu.

Tam Türkçe desteği.
