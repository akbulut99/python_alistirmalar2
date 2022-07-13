isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
sonuc = list(zip(isim,soyisim))
for i,s in sonuc:
    print("isim:{} Soyisim: {}".format(i,s))
    print("**************")