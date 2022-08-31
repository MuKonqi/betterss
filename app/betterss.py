#!/usr/bin/env python3

# Copyright (C) 2022 MuKonqi (Muhammed Abdurrahman)

# BetterSS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# BetterSS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with BetterSS.  If not, see <https://www.gnu.org/licenses/>.

import os
import time
import getpass
username=getpass.getuser()

lang_en="/home/"+username+"/.config/betterss/lang/en.txt"
lang_tr="/home/"+username+"/.config/betterss/lang/tr.txt"

if os.path.isfile('/etc/fedora-release'):
    if not os.path.isdir("/home/"+username+"/.config/betterss"):
        os.system("cd /home/"+username+"/.config/ ; mkdir betterss ; cd betterss ; mkdir lang")
        input1=input("Can't found language setting. First, select a language.\nDil ayarı bulunamadı. İlk önce bir dil seçin.\n\nOptions / Seçenekler: en / tr\nAnswer / Cevap: ")
        if input1 == "en":
            os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; touch en.txt")
            input2=input("English selected.")
        if input1 == "tr":
            os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; touch tr.txt")
            input2=input("Türkçe seçildi.")
    if os.path.isfile(lang_en):
        print("Welcome to BetterSS!")
        process = input("Please select the action you want to perform: Options: screenshot, settings, info, output: ")
    if os.path.isfile(lang_tr):
        print("BetterSS'e hoşgeldiniz!")
        process = input("Lütfen yapmak istediğiniz işlemi seçiniz: Seçenekler: ekran görüntüsü, ayarlar, bilgi, çıkış: ")
    if process == "ekran görüntüsü" or process == "screenshot" or process == "ss":
        os.system("spectacle")    
        exit()
    elif process == "settings" or process == "ayarlar":
        if os.path.isfile("/home/"+username+"/.config/betterss/lang/en.txt"):
            input11=input("Do you want to change the language to Turkish (Türkçe)?\nAnswer: ")
            if input11 == "yes" or input11 == "yes":
                os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; rm * ; touch tr.txt")
                print("Türkçe dili uygulandı.\n\nDeğişikliklerin uygulanması için BetterSS kapatılıyor...")
                exit()
        if os.path.isfile("/home/"+username+"/.config/betterss/lang/tr.txt"):
            input11=input("Dili İngilizce (English) olarak değiştirmek istiyor musunuz?\nCevap: ")
            if input11 == "evet" or input11 == "yes":
                os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; rm * ; touch en.txt")
                print("English language is applied.\n\nBetterSS is shutdown to apply changes.")
                exit()
    elif process == "bilgi" or process == "info":
        if os.path.isfile(lang_en):
            print("BetterSS is a Spetacle launcher on the Pisi GNU/Linux distribution you are using.\nLicense: GPLv3")
            time.sleep(7)
            exit()
        if os.path.isfile(lang_tr):
            print("BetterSS kullandığınız Pisi GNU/Linux dağıtımında bir Spetacle başlatıcısıdır.\nLisans: GPLv3")
            time.sleep(7)
            exit()
    else:
        exit()

from tkinter import *
from tkinter import messagebox
import subprocess


def settings():
    if not os.path.isfile("/home/"+username+"/.config/betterss/theme/dark.txt") and not os.path.isfile("/home/"+username+"/.config/betterss/theme/light.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    if os.path.isfile("/home/"+username+"/.config/betterss/theme/dark.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    elif os.path.isfile("/home/"+username+"/.config/betterss/theme/light.txt"):
        bg="#FFFFFF"
        fg="#000000"
        button_bg="#000000"
        button_fg="#FFFFFF"
        a_button_bg="#FFFFFF"
        a_button_fg="#000000"
    def dark():
        os.system("cd /home/"+username+"/.config/betterss/theme/ ; rm * ; touch dark.txt")
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Successful! Dark theme applied.")
        if os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Koyu tema uygulandı.")
        exit()
    def light():
        os.system("cd /home/"+username+"/.config/betterss/theme/ ; rm * ; touch light.txt")
        if os.path.isfile(lang_en):
            messagebox.showinfo("Information","Successful! Light theme applied.")
        if os.path.isfile(lang_tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Açık tema uygulandı.")
        exit()
    def langen():
        os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; touch en.txt")
        messagebox.showinfo("Information","Successful! English language applied.")
        exit()
    def langtr():
        os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","Başarılı! Türkçe dili uygulandı.") 
        exit()       
    window2=Tk()
    window2.config(background=bg)
    window2.resizable(0, 0)
    if os.path.isfile(lang_en):
        window2.title("Settings | BetterSS")
        text11=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Please select the theme you want to apply.")
        space11=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button11=Button(window2, text="Dark", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth="3 ")
        button12=Button(window2, text="Light", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3" )
        space2=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n\n")
        text12=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="You can change your language preferences below.")
        space12=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button13=Button(window2, text="English (English)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth ="3")
        button14=Button(window2, text="Turkish (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth= "3")
    if os.path.isfile(lang_tr):
        window2.title("Ayarlar | BetterSS")
        text11=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen uygulamak istediğiniz temayı seçiniz.")
        space11=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button11=Button(window2, text="Koyu", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button12=Button(window2, text="Açık", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        space2=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n\n")
        text12=Label(window2, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        space12=Label(window2, background=bg, foreground=fg, font="arial 3", text="\n")
        button13=Button(window2, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        button14=Button(window2, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    text11.pack()
    space11.pack()
    button11.pack()
    button12.pack()
    space2.pack()
    text12.pack()
    space12.pack()
    button13.pack()
    button14.pack()
    mainloop()
def first_start():
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
    os.system("cd /home/"+username+"/.config/; mkdir betterss ; cd betterss ; mkdir lang theme")
    def llangen():
        os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; touch en.txt")
        messagebox.showinfo("Information","English language applied! When you click 'OK', BetterSS settings will open.")
        lwindow.destroy()
        settings()
    def llangtr():
        os.system("cd /home/"+username+"/.config/betterss/lang/ ; rm * ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda BetterSS ayarları açılacak.")
        lwindow.destroy()
        settings()
    lwindow=Tk()
    lwindow.title("Choose a language for BetterSS")
    lwindow.config(background=bg)
    lwindow.resizable(0, 0)
    text1=Label(lwindow, background=bg, foreground=fg, font="arial 10 bold", text="Please choose a language.\nLütfen bir dil seçin.")
    text1.pack()
    space1=Label(lwindow, background=bg, foreground=fg, font="arial 3", text="\n")
    space1.pack()
    button1=Button(lwindow, text="English (İngilizce)", command=llangen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
    button1.pack()
    button2=Button(lwindow, text="Türkçe (Turkish)", command=llangtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    button2.pack()
    mainloop()

if not os.path.isdir("/home/"+username+"/.config/betterss/lang/"):
    messagebox.showerror("Warning","Can't found language setting. When you click 'OK' language settings will open. ")
    first_start()
    exit()

bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/home/"+username+"/.config/betterss/theme/dark.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/home/"+username+"/.config/betterss/theme/light.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
else:
    if os.path.isfile("/home/"+username+"/.config/betterss/lang/en.txt"):
        messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' BetterSS settings will open.")
    elif os.path.isfile("/home/"+username+"/.config/betterss/lang/tr.txt"):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, BetterSS ayarları 'OK' tuşuna bastığınızda açılacaktır.")
    settings()
    exit()

window=Tk()
window.config(background=bg)
window.resizable(0, 0)
window.title("BetterSS")

def about():
    def betterss():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://github.com/MuKonqi/betterss")
    def foss():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://www.gnu.org/philosophy/free-sw.tr.html")
    def developer():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
            if not os.getuid() == 0:
                os.system("xdg-open https://github.com/MuKonqi")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
            if not os.getuid() == 0:
                os.system("xdg-open https://mukonqi.github.io")
    def license():
        if os.path.isfile(lang_en):
            if os.getuid() == 0:
                messagebox.showerror("Error","Links cannot be opened while rooted.")
        elif os.path.isfile(lang_tr):
            if os.getuid() == 0:
                messagebox.showerror("Hata","Bağlantılar, kök haklarına sahipken açılamaz.")
        if not os.getuid() == 0:
            os.system("xdg-open https://www.gnu.org/licenses/gpl-3.0-standalone.html")
    if os.path.isfile(lang_en):
        window=Tk()
        window.title("About | BetterSS")
        window.config(background=bg)
        window.resizable(0, 0)
        space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 7") 
        button1=Button(window, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="BetterSS\nBetterSS\nFlameshot launcher for Debian GNU/Linux and Fedora Linux based distros", command=betterss)
        space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        button2=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="License: GNU General Public License, Version 3.0 (GPLv3)", command=license)
        button3=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="License type: Free and Open Source Software (FOSS)", command=foss)
        button4=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Developer: MuKonqi (Muhammed Abdurrahman)", command=developer)
    elif os.path.isfile(lang_tr):
        window=Tk()
        window.title("Hakkında | BetterSS")
        window.config(background=bg)
        window.resizable(0, 0)
        space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 7") 
        button1=Button(window, font="arial 15 bold italic", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="BetterSS\nDebian GNU/Linux ve Fedora Linux tabanlı dağıtımlar için Flameshot başlatıcısı", command=betterss)
        space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 1")
        button2=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Lisans: GNU General Public License, Version 3.0 (GPLv3)", command=license)
        button3=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Lisans türü: Özgür ve Açık Kaynaklı Yazılım (FOSS)", command=foss)
        button4=Button(window, font="arial 12 bold", cursor="hand2", activeforeground=a_button_fg, activebackground=a_button_bg, background=a_button_bg, foreground=a_button_fg, text="Geliştirici: MuKonqi (Muhammed Abdurrahman)", command=developer)
    space1.pack()
    button1.pack()
    space2.pack()
    button2.pack()
    button3.pack()
    button4.pack()

def main():
    subprocess.Popen("flameshot", shell=TRUE)

if os.path.isfile(lang_en):
    menu1=Menu(window)
    window.config(menu=menu1)
    run=Menu(menu1, tearoff=0)
    menu1.add_cascade(label="Run",menu=run)
    run.add_command(label="Settings", command=settings)
    run.add_command(label="About", command=about)
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Do you want to take a screenshot?")
    space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
    button1=Button(window, text="Yes, please take a screenshot.", command=main, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth ="3")
    button2=Button(window, text="No, please quit.", command=window.destroy, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2 ", borderwidth="3")
if os.path.isfile(lang_tr):
    menu1=Menu(window)
    window.config(menu=menu1)
    run=Menu(menu1, tearoff=0)
    menu1.add_cascade(label="Çalıştır",menu=run)
    run.add_command(label="Ayarlar", command=settings)
    run.add_command(label="Hakkında", command=about)
    text1=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Ekran görüntüsü almak ister misiniz?")
    space1=Label(window, background=bg, foreground=fg, font="arial 3", text="\n")
    button1=Button(window, text="Evet, lütfen ekran görüntüsü al.", command=main, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    button2=Button(window, text="Hayır, lütfen çık.", command=window.destroy, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
text1.pack()
space1.pack()
button1.pack()
button2.pack()

mainloop()