#-*-coding:utf-8-*-
import time
import requests
from bs4 import BeautifulSoup
import webbrowser
import sys
import base64

print("Coder BY : Mr.Ghost")

print("*"*20,"\n")
time.sleep(2)

Kullanıcı = ("Mesut")
şifre = ("alone")
sayılar = [1,2,3,4]


def gir(kullanici_adi):
    while True:
        sys_enter = input("[*]Kullanıcı adı : ")
        time.sleep(1)

        if not sys_enter == Kullanıcı:
            time.sleep(1)
            print("Kullanıcı adı hatalı!\n")
            time.sleep(1)
            continue

        else:
            break
gir("")

# self.password.setEchoMode(QLineEdit.Password)

def gir1(sifre):
    while True:
        sys_enter_pswd = input("[*]Şifre : ")

        if not sys_enter_pswd == şifre:
            time.sleep(1)
            print("Şifre hatalı!\n")
            time.sleep(1)
            continue

        else:
            break
gir1("")

#print("*"*20)        
time.sleep(1)
print("\nHOŞGELDİNİZ!\n")

print("İşlemler :")

print("""
1-> Webten veri çekme
2-> Web sayfası açma
3-> Şifreli veri çözme(BASE64)
4-> Veri şifreleme(BASE64)
5-> Yardım
""")

while True:
    try:
        işlem = int(input("\nYapılacak işlemin numarasını girin : "))
        
        if işlem >= 6:
            time.sleep(1)
            print("Lütfen geçerli bir sayı girin!")
            continue

        elif işlem <= 0:
            time.sleep(1)
            print("Lütfen geçerli bir sayı girin!")
            continue
                        
        elif işlem == 2:
            def yap1(Web_sayfası_açma):
                işlem2 = str(input("\nAçılacak web sayfasını girin : "))

                webbrowser.open(işlem2)

            yap1("")

        elif işlem == 1:
            def yap(Webten_veri_çekme):
                time.sleep(1)

                işlem3 = str(input("\nVeri çekilecek sayfayı girin : "))
                
                istek = requests.get(işlem3)

                içerik = istek.content

                soup = BeautifulSoup(içerik,"html.parser")

                print(soup.prettify())

                print("*"*25,"PARAGRAFLAR","*"*25)

                time.sleep(1)

                #print("\nBu sayfa kodlarında paragraf yok!")
                
                for i in soup.find_all("p"):
                    # Burada sadece içindeki verileri istediğimiz için i.text dedik
                    print(i.text, {"class": "haberler-title"})
                    print("-----------")
            yap("")

        elif işlem == 4:
            time.sleep(1)

            işlem4 = input("\nŞifrelenecek veriyi girin : ")

            şifrele = base64.b64encode(işlem4.encode("utf-8"))

            time.sleep(1)

            print("\nVeri şifrelendi : ",şifrele)

        elif işlem == 3:
            işlem5 = str(input("\nÇözülecek şifreli veriyi girin : "))

            #şifrele2 = base64.b64encode(işlem5.encode("utf-8"))

            #geçici = şifrele2

            çöz = base64.decodebytes(şifrele)

            #çöz2 = base64.decodebytes(çöz)

            time.sleep(1)

            print("\nVeri çözüldü : ",çöz.decode())

        elif işlem == 5:
            print("""
İletişim :
İnstagram => Cihangir.sh
E-posta => hakops82@gmail.com
                """)

        else:
            print("")
        
    except(TypeError,ZeroDivisionError,ValueError):
        time.sleep(1)
        print("Lütfen geçerli veri girin!")