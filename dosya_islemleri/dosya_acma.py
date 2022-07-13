class dosya():
    def __init__(self) -> None:
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i.strip(",")
                i.strip(" ")
                i.strip(".")
                self.sade_kelimeler.append(i)
    

    def kelimeler(self):
        kelimler_kümesi = set()
        for i in self.sade_kelimeler:
            kelimler_kümesi.add(i)
        print("tüm kelimeler.....")
        for i in kelimler_kümesi:
            print(i)
            print("********************")
    def kelime_frekansı(self):
        kelime_sözlük = dict()
        for i in self.sade_kelimeler:
            if i in kelime_sözlük:
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1   
        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} kere geçiyor".format(kelime,sayı))
            print("****************************")        


doysa1 = dosya()
doysa1.kelime_frekansı()