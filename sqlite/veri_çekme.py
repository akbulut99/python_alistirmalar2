import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def veri_cekme():
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()
    for k,y,yy,s in liste:
     print("kitap adı: {} \nYazar: {}\nYayın evi: {}\nSayfa sayısı: {}".format(k,y,yy,s))
     print("********************")
def veri_cek():
    cursor.execute("SELECT İsim,Yazar FROM kitaplık")
    liste2 = cursor.fetchall()
    for i,y in liste2:
        print("kitap adı: {}\Yazar Adı: {}".format(i,y))
        print("***********")


veri_cek()
veri_cekme()
con.close()
