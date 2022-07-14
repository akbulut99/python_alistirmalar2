import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def veri_güncelle(eski_yayinevi,yeni_yayınevi):
    cursor.execute("UPDATE kitaplık set Yayınevi = ? where yayınevi = ?",(yeni_yayınevi,eski_yayinevi))
    con.commit()
    print("veriler güncellendi...")


eski_yayınevi = input("eski yayınevini girin: ")
yeni_yayınevi = input("yeni yayın evini girin: ")
veri_güncelle(eski_yayınevi,yeni_yayınevi)