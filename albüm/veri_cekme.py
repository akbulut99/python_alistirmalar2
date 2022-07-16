from sarki import *

sarki = sarki()
print("""

Spotify
************************************
1.şarkıları göster
2.şarkı ekle
3.şarkı ara
4.toplam süre
programdan çıkmak için 'q' ya basın
************************************

""")
while True:
 islem = input("İşlem Seçin: ")
 if islem == "q":
    print("program kapatılıyor....")
    print("yine bekleriz...")
    break
 elif islem == "1":
    sarki.bilgileri_göster()
 elif islem == "2":
    isim = input("Şarkı adı girin: ")
    sanatci = input("Sanatcı adı girin: ")
    albüm = input("Albüm bilgisi girin: ")
    süre = float(input("Dakika cinsinden süre girin: "))
    yeni_sarki = müzik(isim,sanatci,albüm,süre)
    print("müzik ekleniyor...........")
    sarki.bilgi_ekle(yeni_sarki)
    time.sleep(2)
    print("müzik başarıyla eklendi...")
 elif islem == "3":
    print("""
    1.Müzik adına göre
    2.Sanatçı adına göre
    """)
    islem = input("Hangi bilgiye göre arama yapmak istersiniz?:")
    if islem == "1":
        islem2 = input("şarkı adı girin")
        sarki.bilgileri_göster(islem2)

    elif islem == "2":
        islem3 = input("Sanatcı adı girin: ")
        sarki.bilgileri_göster(islem3)
 elif islem == "4":
    pass