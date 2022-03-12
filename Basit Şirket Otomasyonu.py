class Sirket:
    def __init__(self,ad):
        self.ad=ad
        self.calisma=True

    def program(self):
        secim= self.menuSecin()
        if secim ==1:
            self.calisanEkle()
        if secim ==2:
            self.calisanCikar()
        if secim ==3:
            self.verilecekMaasigöster()
        if secim ==4:
            self.maaslariVer()
        if secim ==5:
            self.masrafGir()
        if secim ==6:
            self.gelirGir()

    def menuSecin(self):
        secim=int(input("***{} otomasyonuna hoşgeldiniz *** \n 1-Çalışan Ekle \n 2-Çalışan Çıkart \n 3-Verilecek Maaş göster \n 4- Maaşları ver \n 5-Masraf Gir \n 6-Gelir Gir \n Seçiminizi giriniz: ".format(self.ad)))
        return secim

    def calisanEkle(self):
        ad=input("Çalışanın adını giriniz")
        soyad=input("Çalışanın soyadını giriniz")
        yas=input("Çalışanın yaşını giriniz")
        cinsiyet=input("Çalışanın cinsiyetini giriniz")
        maas=input("Çalışanın maaşını giriniz")

        with open("calisanlr.txt","r") as dosya:
             calisanListesi=dosya.readlines()
             
        
            
        if len(calisanListesi)==0:
            id =1
        else:
            with open("calisanlr.txt","r") as dosya:
                id=int(dosya.readlines()[-1].split(")")([0]) + 1
                       
                       
        with open("calisanlr.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))
            

            

        def calisanCikar(self):
        pass

    def verilecekMaasGoster(self,hesap="a"):
        
        pass

    def maaslariVer(self):
        pass

    def masrafGir(self):
        pass

    def gelirGir(self):
        pass

sirket=Sirket("EŞOBETSS")

