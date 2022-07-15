from setuptools import sic
from kütüphane import *

Kütüphane = Kütüphane()
print("""

*********************************
Kütüphane Programına Hoşgeldiniz;
1.Kitapları Göster
2.Kitap Sorgula
3.Kitap Ekle
4.Kitap Sil
5.Baskı Yükselt
Çıkmak için 'q' ya basın
*********************************


""")
while True:
    islem = input("islem seçin: ")
    if islem == "q":
        print("program sonlandırılıyor...")
        print("Yine bekleriz...")
        break
    elif islem == "1":
        Kütüphane.kitapları_goster()
    elif islem == "2":
        istek = input("Hangi kitabı istiyorsunuz?..: ")
        print("kitap sorgulanıyor")
        time.sleep(1)
        Kütüphane.kitap_sorgula(istek)
    elif islem == "3":
        isim = input("Eklemek istediğiniz kitabın adı?: ")
        yazar = input("Yazar adı:")
        yayınevi = input("Yayınevi adı: ")
        tür = input("kitap türü:")
        baskı = int(input("Baskı sayısı: "))
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("kitap ekleniyor...")
        time.sleep(2)
        Kütüphane.kitap_ekle(yeni_kitap)
        print("kitap eklendi...")
    elif islem == "4":
        sil = input("Silmek istediğiniz kitabın adı: ")
        print("kitap siliniyor...")
        Kütüphane.kitap_sil(sil)
        time.sleep(2)
        print("kitap silindi...")
    elif islem == "5":
        baskı = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?: ")
        print("baskı yükseltiliyor...")
        Kütüphane.baskı_yükselt(baskı)
        time.sleep(2)
        print("baskı yükseltildi...")
    else:
        print("gecersiz işlem!!!")