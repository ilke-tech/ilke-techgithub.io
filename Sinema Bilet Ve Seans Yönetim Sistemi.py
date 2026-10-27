
class Film:
    def __init__(self, film_id, ad, tur, sure, yas_siniri):
        self.film_id = film_id
        self.ad = ad
        self.tur = tur
        self.sure = sure
        self.yas_siniri = yas_siniri

    def bilgi_goster(self):
        print("Film ID:", self.film_id)
        print("Film:", self.ad)
        print("Tur:", self.tur)
        print("Sure:", self.sure, "dakika")
        print("Yas Siniri:", self.yas_siniri)




class Seans:
    def __init__(self, seans_id, film, salon, saat, fiyat, koltuk_sayisi):
        self.seans_id = seans_id
        self.film = film
        self.salon = salon
        self.saat = saat
        self.fiyat = fiyat
        
        self.koltuklar = []
        for i in range(koltuk_sayisi):
            self.koltuklar.append("BOS")

    def koltuklari_goster(self):
        for i in range(len(self.koltuklar)):
            koltuk_no = i + 1
            durum = self.koltuklar[i]
            print(koltuk_no, "[", durum, "]")

    def koltuk_musait_mi(self, koltuk_no):
        
        index = koltuk_no - 1
        if index < 0 or index >= len(self.koltuklar):
            return False
        if self.koltuklar[index] == "BOS":
            return True
        else:
            return False

    def koltuk_doldur(self, koltuk_no):
        index = koltuk_no - 1
        self.koltuklar[index] = "DOLU"

    def koltuk_bosalt(self, koltuk_no):
        index = koltuk_no - 1
        self.koltuklar[index] = "BOS"

    def doluluk_bilgisi(self):
        toplam = len(self.koltuklar)
        dolu = 0
        for durum in self.koltuklar:
            if durum == "DOLU":
                dolu = dolu + 1
        bos = toplam - dolu
        yuzde = (dolu / toplam) * 100
        return toplam, dolu, bos, yuzde



class Bilet:
    def __init__(self, bilet_id, musteri_adi, film, seans, koltuk_no, tur, ucret):
        self.bilet_id = bilet_id
        self.musteri_adi = musteri_adi
        self.film = film
        self.seans = seans
        self.koltuk_no = koltuk_no
        self.tur = tur
        self.ucret = ucret

    def bilet_goster(self):
        print("========================")
        print("        BILET")
        print("========================")
        print("Bilet No:", self.bilet_id)
        print("Musteri:", self.musteri_adi)
        print("Film:", self.film.ad)
        print("Seans:", self.seans.saat)
        print("Salon:", self.seans.salon)
        print("Koltuk:", self.koltuk_no)
        print("Tur:", self.tur)
        print("Ucret:", self.ucret, "TL")
        print("========================")



def bilet_fiyati_hesapla(taban_fiyat, bilet_turu):
    if bilet_turu == "Ogrenci":
        indirim = taban_fiyat * 0.25
        fiyat = taban_fiyat - indirim
        return fiyat
    else:
        return taban_fiyat



class Sinema:
    def __init__(self):
        self.filmler = []
        self.seanslar = []
        self.biletler = []
        self.film_sayac = 1
        self.seans_sayac = 1
        self.bilet_sayac = 1

    
    def film_ekle(self, ad, tur, sure, yas_siniri):
        yeni_film = Film(self.film_sayac, ad, tur, sure, yas_siniri)
        self.filmler.append(yeni_film)
        print("Film basariyla eklendi.")
        print("Film ID:", self.film_sayac)
        self.film_sayac = self.film_sayac + 1

    def filmleri_listele(self):
        if len(self.filmler) == 0:
            print("Sistemde kayitli film yok.")
            return
        for film in self.filmler:
            print("-----------------------------")
            film.bilgi_goster()

    def film_bul(self, film_id):
        for film in self.filmler:
            if film.film_id == film_id:
                return film
        return None

    def film_ara(self, aranan_isim):
        aranan_isim = aranan_isim.lower()
        bulunanlar = []
        for film in self.filmler:
            if aranan_isim in film.ad.lower():
                bulunanlar.append(film)

        if len(bulunanlar) == 0:
            print("Araniginiz film bulunamadi.")
        else:
            for film in bulunanlar:
                print("-----------------------------")
                film.bilgi_goster()

    
    def seans_ekle(self, film_id, salon, saat, fiyat, koltuk_sayisi):
        film = self.film_bul(film_id)
        if film is None:
            print("Boyle bir film bulunamadi. Seans olusturulamadi.")
            return

        yeni_seans = Seans(self.seans_sayac, film, salon, saat, fiyat, koltuk_sayisi)
        self.seanslar.append(yeni_seans)
        print("Seans basariyla eklendi.")
        print("Seans ID:", self.seans_sayac)
        self.seans_sayac = self.seans_sayac + 1

    def seanslari_listele(self):
        if len(self.seanslar) == 0:
            print("Sistemde kayitli seans yok.")
            return
        for seans in self.seanslar:
            print(seans.seans_id, "-", seans.film.ad, "|", seans.saat, "| Salon", seans.salon)

    def seans_bul(self, seans_id):
        for seans in self.seanslar:
            if seans.seans_id == seans_id:
                return seans
        return None


    def bilet_sat(self, seans, koltuk_no, musteri_adi, yas, bilet_turu):
        
        if not seans.koltuk_musait_mi(koltuk_no):
            print("Bu koltuk daha once satilmistir.")
            return None

        
        if yas < seans.film.yas_siniri:
            print("Bu film icin minimum yas siniri", seans.film.yas_siniri, "'dir.")
            print("Bilet satisi gerceklestirilemedi.")
            return None

        
        ucret = bilet_fiyati_hesapla(seans.fiyat, bilet_turu)

        
        yeni_bilet = Bilet(self.bilet_sayac, musteri_adi, seans.film, seans, koltuk_no, bilet_turu, ucret)

       
        seans.koltuk_doldur(koltuk_no)


        self.biletler.append(yeni_bilet)
        self.bilet_sayac = self.bilet_sayac + 1

        return yeni_bilet

    def bilet_iptal(self, bilet_id):
        bulunan_bilet = None
        for bilet in self.biletler:
            if bilet.bilet_id == bilet_id:
                bulunan_bilet = bilet
                break

        if bulunan_bilet is None:
            print("Bilet bulunamadi.")
            return

       
        bulunan_bilet.seans.koltuk_bosalt(bulunan_bilet.koltuk_no)

        
        self.biletler.remove(bulunan_bilet)

        print("Bilet iptal edildi. Koltuk tekrar bosaltildi.")

    
    def gun_sonu_raporu(self):
        toplam_film = len(self.filmler)
        toplam_seans = len(self.seanslar)
        toplam_bilet = len(self.biletler)

        tam_sayisi = 0
        ogrenci_sayisi = 0
        toplam_ciro = 0

        for bilet in self.biletler:
            if bilet.tur == "Tam":
                tam_sayisi = tam_sayisi + 1
            else:
                ogrenci_sayisi = ogrenci_sayisi + 1
            toplam_ciro = toplam_ciro + bilet.ucret

        
        en_cok_satan_seans = None
        en_yuksek_dolu = -1
        for seans in self.seanslar:
            toplam, dolu, bos, yuzde = seans.doluluk_bilgisi()
            if dolu > en_yuksek_dolu:
                en_yuksek_dolu = dolu
                en_cok_satan_seans = seans

        print("=================================")
        print("        GUN SONU RAPORU")
        print("=================================")
        print("Toplam Film     :", toplam_film)
        print("Toplam Seans    :", toplam_seans)
        print("Satilan Bilet   :", toplam_bilet)
        print()
        print("Tam Bilet       :", tam_sayisi)
        print("Ogrenci Bileti  :", ogrenci_sayisi)
        print()
        print("Toplam Ciro     :", toplam_ciro, "TL")
        print()

        if en_cok_satan_seans is not None and en_yuksek_dolu > 0:
            toplam, dolu, bos, yuzde = en_cok_satan_seans.doluluk_bilgisi()
            print("En Cok Satisli Seans:")
            print(en_cok_satan_seans.film.ad, "-", en_cok_satan_seans.saat)
            print(dolu, "/", toplam, "koltuk")
        else:
            print("Henuz bilet satilmadi.")

        print("=================================")



def ana_menu_goster():
    print()
    print("==================================")
    print("          CINEFLOW SINEMA")
    print("==================================")
    print("1 - Filmleri Listele")
    print("2 - Seanslari Listele")
    print("3 - Bilet Sat")
    print("4 - Bilet Iptal Et")
    print("5 - Koltuk Durumunu Goster")
    print("6 - Yeni Film Ekle")
    print("7 - Yeni Seans Ekle")
    print("8 - Gun Sonu Raporu")
    print("9 - Film Ara")
    print("0 - Cikis")
    print("==================================")


def film_ekleme_ekrani(sinema):
    print("--- YENI FILM EKLE ---")
    ad = input("Film adi: ")
    tur = input("Film turu: ")
    sure = int(input("Film suresi (dakika): "))
    yas_siniri = int(input("Yas siniri: "))
    sinema.film_ekle(ad, tur, sure, yas_siniri)


def seans_ekleme_ekrani(sinema):
    print("--- YENI SEANS EKLE ---")
    if len(sinema.filmler) == 0:
        print("Once film eklemelisiniz.")
        return

    sinema.filmleri_listele()
    film_id = int(input("Film ID secin: "))

    film = sinema.film_bul(film_id)
    if film is None:
        print("Boyle bir film ID'si yok. Seans olusturulamadi.")
        return

    salon = input("Salon: ")
    saat = input("Saat: ")
    fiyat = float(input("Bilet fiyati (tam bilet, TL): "))
    koltuk_sayisi = int(input("Koltuk sayisi: "))

    sinema.seans_ekle(film_id, salon, saat, fiyat, koltuk_sayisi)


def koltuk_goster_ekrani(sinema):
    print("--- KOLTUK DURUMU ---")
    if len(sinema.seanslar) == 0:
        print("Sistemde kayitli seans yok.")
        return

    sinema.seanslari_listele()
    seans_id = int(input("Koltuklarini gormek istediginiz seans ID: "))
    seans = sinema.seans_bul(seans_id)

    if seans is None:
        print("Boyle bir seans bulunamadi.")
        return

    print(seans.film.ad, "-", seans.saat)
    seans.koltuklari_goster()

    toplam, dolu, bos, yuzde = seans.doluluk_bilgisi()
    print()
    print("Toplam Koltuk :", toplam)
    print("Satilan       :", dolu)
    print("Bos           :", bos)
    print("Doluluk       : %", round(yuzde, 1))


def bilet_satis_ekrani(sinema):
    print("--- BILET SAT ---")
    if len(sinema.seanslar) == 0:
        print("Sistemde kayitli seans yok.")
        return

    sinema.seanslari_listele()
    seans_id = int(input("Seans ID secin: "))
    seans = sinema.seans_bul(seans_id)

    if seans is None:
        print("Boyle bir seans bulunamadi.")
        return

    seans.koltuklari_goster()
    koltuk_no = int(input("Koltuk numarasi: "))

    if not seans.koltuk_musait_mi(koltuk_no):
        print("Bu koltuk daha once satilmistir.")
        return

    musteri_adi = input("Musteri adi: ")
    yas = int(input("Musteri yasi: "))

    print("1 - Tam")
    print("2 - Ogrenci")
    tur_secim = input("Bilet turu secin: ")

    if tur_secim == "2":
        bilet_turu = "Ogrenci"
    else:
        bilet_turu = "Tam"

    yeni_bilet = sinema.bilet_sat(seans, koltuk_no, musteri_adi, yas, bilet_turu)

    if yeni_bilet is not None:
        print()
        print("Bilet basariyla satildi.")
        yeni_bilet.bilet_goster()


def bilet_iptal_ekrani(sinema):
    print("--- BILET IPTAL ET ---")
    if len(sinema.biletler) == 0:
        print("Iptal edilecek bilet yok.")
        return

    bilet_id = int(input("Bilet numarasi: "))
    sinema.bilet_iptal(bilet_id)


def film_arama_ekrani(sinema):
    print("--- FILM ARA ---")
    aranan = input("Aranacak film: ")
    sinema.film_ara(aranan)



def ornek_veri_yukle(sinema):
    sinema.film_ekle("Red Notice", "Aksiyon", 118, 13)
    sinema.film_ekle("Spider-Man: Homecoming", "Aksiyon", 133, 10)
    sinema.film_ekle("Spider-Man: Far From Home", "Aksiyon", 129, 10)
    sinema.film_ekle("Harry Potter ve Felsefe Tasi", "Fantastik", 152, 7)

    sinema.seans_ekle(1, "1", "18:00", 200, 20)
    sinema.seans_ekle(2, "2", "21:00", 190, 20)
    sinema.seans_ekle(3, "3", "20:00", 190, 20)
    sinema.seans_ekle(4, "4", "17:30", 180, 20)


def main():
    sinema = Sinema()
    ornek_veri_yukle(sinema)

    while True:
        ana_menu_goster()
        secim = input("Seciminiz: ")

        if secim == "1":
            sinema.filmleri_listele()

        elif secim == "2":
            sinema.seanslari_listele()

        elif secim == "3":
            bilet_satis_ekrani(sinema)

        elif secim == "4":
            bilet_iptal_ekrani(sinema)

        elif secim == "5":
            koltuk_goster_ekrani(sinema)

        elif secim == "6":
            film_ekleme_ekrani(sinema)

        elif secim == "7":
            seans_ekleme_ekrani(sinema)

        elif secim == "8":
            sinema.gun_sonu_raporu()

        elif secim == "9":
            film_arama_ekrani(sinema)

        elif secim == "0":
            print("Programdan cikiliyor...")
            break

        else:
            print("Gecersiz secim, tekrar deneyin.")


if __name__ == "__main__":
    main()