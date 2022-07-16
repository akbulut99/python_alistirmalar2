
import sqlite3
import time
class müzik():
    def __init__(self,isim,sanatci,albüm,sarkisüresi):
        self.sarkiadi = isim
        self.sanatci = sanatci
        self.albüm = albüm
        self.sarkisüresi = sarkisüresi
    
    def __str__(self):
            
     return "Şarkı adı: {}\nSanatçı: {}\nAlbüm:{}\nSüresi(dakika):{}".format(self.isim,self.sanatci,self.albüm,self.sarkisüresi)
    
class sarki():
    def __init__(self):
       self.baglanti_olustur()
   
    
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Spotify.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kutu('sarkiadi TEXT','sanatci TEXT','albüm TEXT','sure FLOAT')"
        self.cursor.execute(sorgu)
        self.baglanti.commit()  
   
    def baglanti_kes(self):
        self.baglanti.close()
    def bilgi_ekle(self,müzik):
        sorgu = "INSERT INTO bilgiler VALUES(?,?,?,?)"
        self.cursor.execute(sorgu,(müzik.sarkiadi,müzik.sanatci,müzik.albüm, müzik.sure))   
        self.baglanti.commit()
    def bilgileri_göster(self):
        sorgu = "Select * FROM kutu"
        self.cursor.execute(sorgu)
        müzikler = self.cursor.fetchall()
        if len(müzikler) == 0:
            print("Herhangi bir şarkı bulunmuyor...")
        else:
            bilgi = müzik(müzikler[0][0],müzikler[0][1],müzikler[0][2],müzikler[0][3])

    def sanatci_sorgula(self,isim):
        sorgu = "Select * From kutu where sanatci = ?"    
        self.cursor.execute(sorgu,(isim,))
        cevap = self.cursor.fetchall()
        if len(cevap) == 0:
            print("Sanatcıya ait şarkı yok")
        else:
            göster = müzik(cevap[0][0],cevap[0][1],cevap[0][2],cevap[0][3])
            print(göster)
    
    def sarki_sorgula(self,sarki):
        sorgu = "Select * From kutu where sarkiadi = ?"
        self.cursor.execute(sorgu,(sarki,))
        cevap = self.cursor.fetchall()
        if len(cevap) == 0:
            print("Böyle bir şarkı bulunmuyor")
        else:
            göster = müzik(cevap[0][0],cevap[0][1],cevap[0][2],cevap[0][3])
            print(göster)
