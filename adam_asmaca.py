
class Hangman():




    def __init__(self):
        self.dogruKelime = self.dogruKelime()
        self.dogruKelime2 = self.dogruKelime.replace(" ", "")
        self.dogruKelime3 = [] # içinde farklı harfler bulundan doğru kelime
        for i in self.dogruKelime2: # doğru kelime 3 düzenleme
            if i not in self.dogruKelime3:
                self.dogruKelime3.append(i)
        self.dogruHarfler = []
        self.yanlisHarfler = []
        self.yanlisHarflerKucuk = []

        self.asama_1 = """
            +----------+
            |          |
            |          |
            |         
            |         
            |        
            |         
            |        
            |        
            |
        +------+------------------+
        |                         |
        |                         +----+
        |                              |
        +------------------------------+
        """

        self.asama_2 = """
            +----------+
            |          |
            |          |
            |         (.)
            |         
            |        
            |         
            |        
            |        
            |
        +------+------------------+
        |                         |
        |                         +----+
        |                              |
        +------------------------------+
        """

        self.asama_3 = """
            +----------+
            |          |
            |          |
            |         (.)
            |          |
            |          |
            |         
            |        
            |        
            |
        +------+------------------+
        |                         |
        |                         +----+
        |                              |
        +------------------------------+
        """

        self.asama_4 = """
            +----------+
            |          |
            |          |
            |         (.)
            |          |.
            |          | |
            |         
            |        
            |        
            |
        +------+------------------+
        |                         |
        |                         +----+
        |                              |
        +------------------------------+
        """

        self.asama_5 = """
            +----------+
            |          |
            |          |
            |         (.)
            |         .|.
            |        | | |
            |         
            |        
            |        
            |
        +------+------------------+
        |                         |
        |                         +----+
        |                              |
        +------------------------------+
        """

        self.asama_6 = """
            +----------+
            |          |
            |          |
            |         (.)
            |         .|.
            |        | | |
            |           .
            |            .
            |            
            |
        +------+------------------+
        |                         |
        |                         +----+
        |                              |
        +------------------------------+
        """

        self.asama_7 = """
            +----------+
            |          |
            |          |
            |         (.)
            |         .|.
            |        | | |
            |         . .
            |        .   .
            |        
            |
        +------+------------------+
        |                         |
        |                         +----+
        |                              |
        +------------------------------+
        """
        
        self.tur = 0

        self.asamaListesi = [self.asama_1, self.asama_2, self.asama_3, self.asama_4, self.asama_5, self.asama_6, self.asama_7]

        self.bosListe = [] # self.dogruKelime'nin bulundurduğu harf sayısı kadar " " bulunduran liste
        
        for i in self.dogruKelime: # bosListe düzenleme
            self.bosListe.append(" ")
            
        self.harfListe = [] # self.dogruKelime'nin liste hali

        for i in self.dogruKelime: # harfListe düzenleme
            self.harfListe.append(i)

        self.anaMenu()
        pass



    def anaMenu(self):
        while True:
            dogruMu = self.harfTahmin()
            if dogruMu == False:
                self.oyunTablosu()
            else:
                print(self.asamaListesi[self.tur])
            self.oyunBittiMi()



    def harfTahmin(self):

        
        tümHarfler = "qwertyuıopğüasdfghjklşizxcvbnmöç"

        while True:

            tahmin = input('Harf tahmininizi giriniz: ')
            print()
                
            if " " in tahmin:
                print("Tahmininiz boşluk içeremez.\n")
                continue


            elif len(tahmin) != 1:
                print("Tahmininiz 1 harften oluşmalı.\n")
                continue

            elif tahmin not in tümHarfler:
                print("Tahmininiz küçük harf olmalı.\n")
                continue

            elif len(tahmin) == 1 and tahmin != " ":
                if tahmin in self.dogruHarfler:
                    print("Bu harfi zaten bilmiştiniz.\n")


                elif tahmin in self.dogruKelime2:
                    self.dogruHarfler.append(tahmin)
                    if len(self.dogruHarfler) != len(self.dogruKelime3):
                        print("Tebrikler. Tahmininiz doğru. Kazanmanıza {} harf kaldı.".format(len(self.dogruKelime3) - len(self.dogruHarfler)))
                        for i in range(0, len(self.harfListe)):
                            if tahmin == self.harfListe[i]:
                                if tahmin != "i":
                                    self.bosListe[i] = tahmin.upper()
                                else:
                                    self.bosListe[i] = "İ"
                        return True
                    for i in range(0, len(self.harfListe)):
                            if tahmin == self.harfListe[i]:
                                if tahmin != "i":
                                    self.bosListe[i] = tahmin.upper()
                                else:
                                    self.bosListe[i] = "İ"
                    return True


                elif tahmin in self.yanlisHarflerKucuk:
                    print("Bu harfi zaten denemiştiniz.\n")


                else:
                    if tahmin != "i":
                        self.yanlisHarfler.append(tahmin.upper())
                    else:
                        self.yanlisHarfler.append("İ")
                    self.yanlisHarflerKucuk.append(tahmin)
                    if len(self.yanlisHarfler) != len(self.dogruKelime3):
                        print("Tahmininiz yanlış. {} hakkınız kaldı.".format(len(self.dogruKelime2) - len(self.yanlisHarfler)))
                        return False
                    return False




    def oyunBittiMi(self):

        if len(self.dogruHarfler) == len(self.dogruKelime3):
            self.oyunTablosu()
            self.harfTablosu()
            while True:
                secim = input("Tebrikler, {} kelimesini başarıyla tahmin ettiniz. Tekrar oynamak ister misiniz? E(evet), H(hayır): ".format(self.dogruKelime2))
                if secim == "E":
                    Hangman()
                elif secim == "H":
                    print("Oyun sonlanmıştır.")
                    exit()
                else:
                    print("Lütfen seçiminizi E veya H olarak yapınız.")
            

        elif len(self.yanlisHarfler) == len(self.dogruKelime3):
            
            print(self.asama_7)
            self.harfTablosu()

            while True:
                secim = input("Oyunu kaybettiniz. {} adlı kelimeyi bilemediniz. Tekrar oynamak ister misiniz? E(evet), H(hayır): ".format(self.dogruKelime2))
                if secim == "E":
                    Hangman()
                elif secim == "H":
                    print("Oyun sonlanmıştır.")
                    exit()
                else:
                    print("Lütfen seçiminizi E veya H olarak yapınız.")

        self.harfTablosu()



    def dogruKelime(self):

        tümHarfler = "qwertyuıopğüasdfghjklşizxcvbnmöç "

        while True:

            sembolVarMi = False
            ardArdaBoslukVarMi = False
            kelime = input("Tahmin edilmesini istediğiniz kelimeyi girin: ")
            kelimeKucuk = kelime.lower()
            print()

            for i in kelime: # sembolü kontrol eder
                if i not in tümHarfler:
                    sembolVarMi = True

            for i in range(0, len(kelime) - 1): # ard arda boşluk olup olmadığını kontrol eder
                if kelime[i] == kelime[i + 1] and kelime[i] == " ":
                    ardArdaBoslukVarMi = True

            if sembolVarMi == True:
                print("Kelimeniz sadece harf içerebilir, kelimenizde büyük harf bulunamaz.\n")
                continue

            elif kelime[0] == " ":
                print("Kelimeniz boşluk karakteriyle başlayamaz.\n")
                continue

            elif kelime[-1] == " ":
                print("Kelimeniz boşluk harfiyle bitemez.\n")
                continue

            elif ardArdaBoslukVarMi == True:
                print("Kelimenizde ard arda 2 tane boşluk bulunamaz.\n")
                continue

            elif len(kelime) < 5:
                print("Kelimeniz en az 5 harften oluşmalıdır\n")
                continue

            else:
                break

        
        return kelimeKucuk      



    def oyunTablosu(self):


        bolum = len(self.dogruKelime2) // 6
        kalan = len(self.dogruKelime2) % 6

        if len(self.yanlisHarfler) != 0:
            if len(self.yanlisHarfler) == len(self.dogruKelime3):
                self.tur = 6

            elif len(self.yanlisHarfler) % (bolum+1) == 0:
                self.tur += 1

        else:
            self.tur += 1

        if len(self.yanlisHarfler) != len(self.dogruKelime3):
            print(self.asamaListesi[self.tur])

        

    def harfTablosu(self):

        üstHarfler = ""
        ortaCizgi = ""
        altHarfler = ""
        harfListe = [] # self.dogruKelime'nin liste hali


        for i in self.dogruKelime: # harfListe düzenleme
            harfListe.append(i)


        for i in range(0, len(self.bosListe)): # üstHarfler düzenleme

            if self.dogruKelime[i] == " ":
                üstHarfler += "   "
            else:
                üstHarfler += "  {}  ".format(self.bosListe[i])


        for i in self.dogruKelime: # ortaCizgi düzenleme
            if i == " ":
                ortaCizgi += "   "

            else:
                ortaCizgi += " --- "


        for i in range(0, len(self.yanlisHarfler)):

            if self.dogruKelime[i] == " ":
                altHarfler += "     "

            else:
                altHarfler += "  {}  ".format(self.yanlisHarfler[i])


        print(üstHarfler)
        print(ortaCizgi)
        print(altHarfler)
        print()






calistir = Hangman()