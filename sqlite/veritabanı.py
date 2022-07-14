import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_sayısı INT)")
    con.commit()
def veri_ekle(isim,yazar,yayınevi,sayfa_sayısı):
  cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
  con.commit()
  print("veriler eklendi")




isim = str(input("isim girin: "))
yazar = str(input("Yazar Adı: "))
Yayınevi = str(input("Yayınevi: "))
sayfa_sayısı = int(input("sayfa sayısı: "))
veri_ekle(isim,yazar,Yayınevi,sayfa_sayısı)
con.close()