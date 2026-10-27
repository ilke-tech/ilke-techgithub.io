

import json
import os


DOSYA_ADI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "servisler.json")



def sayiya_cevir(metin):
    metin = metin.strip()
    metin = metin.upper().replace("TL", "")
    metin = metin.strip()
    metin = metin.replace(",", ".")
    return float(metin)




class ServisKaydi:

    def __init__(self, id, musteri, telefon, cihaz, ariza, ucret, durum="Bekliyor"):
        self.id = id
        self.musteri = musteri
        self.telefon = telefon
        self.cihaz = cihaz
        self.ariza = ariza
        self.ucret = ucret
        self.durum = durum

    def yazdir(self):
        print("----------------------------------------")
        print("Servis No:", self.id)
        print("Müşteri :", self.musteri)
        print("Telefon :", self.telefon)
        print("Cihaz   :", self.cihaz)
        print("Arıza   :", self.ariza)
        print("Ücret   :", self.ucret, "TL")
        print("Durum   :", self.durum)
        print("----------------------------------------")

    def dict_yap(self):
        return {
            "id": self.id,
            "musteri": self.musteri,
            "telefon": self.telefon,
            "cihaz": self.cihaz,
            "ariza": self.ariza,
            "ucret": self.ucret,
            "durum": self.durum
        }

    @staticmethod
    def dict_ten_olustur(veri):
        return ServisKaydi(
            veri["id"],
            veri["musteri"],
            veri["telefon"],
            veri["cihaz"],
            veri["ariza"],
            veri["ucret"],
            veri["durum"]
        )




def servisleri_yukle():
    servisler = []
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            veriler = json.load(dosya)
            for veri in veriler:
                servisler.append(ServisKaydi.dict_ten_olustur(veri))
    except FileNotFoundError:
        servisler = []
    except json.JSONDecodeError:
        servisler = []

    return servisler


def servisleri_kaydet(servisler):
    veriler = []
    for servis in servisler:
        veriler.append(servis.dict_yap())

    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(veriler, dosya, ensure_ascii=False, indent=4)




def yeni_kayit_olustur(servisler):
    print("\n--- Yeni Servis Kaydı ---")
    musteri = input("Müşteri adı: ")
    telefon = input("Telefon: ")
    cihaz = input("Cihaz: ")
    ariza = input("Arıza açıklaması: ")

    try:
        ucret = sayiya_cevir(input("Servis ücreti: "))
    except ValueError:
        print("Hatalı giriş. Lütfen sayısal bir değer giriniz. Örnek: 1500 veya 1500,50")
        return

    yeni_id = len(servisler) + 1

    yeni_servis = ServisKaydi(yeni_id, musteri, telefon, cihaz, ariza, ucret, "Bekliyor")
    servisler.append(yeni_servis)

    servisleri_kaydet(servisler)
    print("Servis kaydı oluşturuldu. Servis No:", yeni_id)


def tum_kayitlari_listele(servisler):
    print("\n--- Tüm Servis Kayıtları ---")
    if len(servisler) == 0:
        print("Henüz servis kaydı bulunmuyor.")
        return

    for servis in servisler:
        servis.yazdir()


def kayit_ara(servisler):
    print("\n--- Servis Kaydı Ara ---")
    print("1 - Servis numarasına göre")
    print("2 - Müşteri adına göre")

    try:
        secim = int(input("Seçiminiz: "))
    except ValueError:
        print("Hatalı giriş. Lütfen sayısal bir değer giriniz.")
        return

    if secim == 1:
        try:
            no = int(input("Servis numarası: "))
        except ValueError:
            print("Hatalı giriş. Lütfen sayısal bir değer giriniz.")
            return

        bulundu = False
        for servis in servisler:
            if servis.id == no:
                servis.yazdir()
                bulundu = True

        if not bulundu:
            print("Servis kaydı bulunamadı.")

    elif secim == 2:
        isim = input("Müşteri adı (veya bir kısmı): ")

        bulundu = False
        for servis in servisler:
            if isim.lower() in servis.musteri.lower():
                servis.yazdir()
                bulundu = True

        if not bulundu:
            print("Servis kaydı bulunamadı.")

    else:
        print("Geçersiz seçim.")


def durum_guncelle(servisler):
    print("\n--- Servis Durumunu Güncelle ---")
    try:
        no = int(input("Servis numarası: "))
    except ValueError:
        print("Hatalı giriş. Lütfen sayısal bir değer giriniz.")
        return

    aranan_servis = None
    for servis in servisler:
        if servis.id == no:
            aranan_servis = servis

    if aranan_servis is None:
        print("Servis kaydı bulunamadı.")
        return

    print("1 - Bekliyor")
    print("2 - Tamir Ediliyor")
    print("3 - Tamamlandı")

    try:
        secim = int(input("Yeni durum: "))
    except ValueError:
        print("Hatalı giriş. Lütfen sayısal bir değer giriniz.")
        return

    if secim == 1:
        aranan_servis.durum = "Bekliyor"
    elif secim == 2:
        aranan_servis.durum = "Tamir Ediliyor"
    elif secim == 3:
        aranan_servis.durum = "Tamamlandı"
    else:
        print("Geçersiz servis durumu.")
        return

    servisleri_kaydet(servisler)
    print("Durum güncellendi.")


def ucret_guncelle(servisler):
    print("\n--- Servis Ücretini Güncelle ---")
    try:
        no = int(input("Servis numarası: "))
    except ValueError:
        print("Hatalı giriş. Lütfen sayısal bir değer giriniz.")
        return

    aranan_servis = None
    for servis in servisler:
        if servis.id == no:
            aranan_servis = servis

    if aranan_servis is None:
        print("Servis kaydı bulunamadı.")
        return

    try:
        yeni_ucret = sayiya_cevir(input("Yeni servis ücreti: "))
    except ValueError:
        print("Hatalı giriş. Lütfen sayısal bir değer giriniz. Örnek: 1500 veya 1500,50")
        return

    aranan_servis.ucret = yeni_ucret
    servisleri_kaydet(servisler)
    print("Ücret güncellendi.")


def tamamlananlari_listele(servisler):
    print("\n--- Tamamlanan Servisler ---")
    bulundu = False
    for servis in servisler:
        if servis.durum == "Tamamlandı":
            servis.yazdir()
            bulundu = True

    if not bulundu:
        print("Tamamlanmış servis kaydı bulunmuyor.")


def toplam_kazanc_goster(servisler):
    toplam = 0
    for servis in servisler:
        if servis.durum == "Tamamlandı":
            toplam = toplam + servis.ucret

    print("\nToplam Kazanç:", toplam, "TL")


def istatistikleri_goster(servisler):
    toplam_sayi = len(servisler)
    bekleyen = 0
    tamir_edilen = 0
    tamamlanan = 0
    toplam_kazanc = 0

    for servis in servisler:
        if servis.durum == "Bekliyor":
            bekleyen = bekleyen + 1
        elif servis.durum == "Tamir Ediliyor":
            tamir_edilen = tamir_edilen + 1
        elif servis.durum == "Tamamlandı":
            tamamlanan = tamamlanan + 1
            toplam_kazanc = toplam_kazanc + servis.ucret

    if tamamlanan > 0:
        ortalama = toplam_kazanc / tamamlanan
    else:
        ortalama = 0

    print("\n========= SERVİS İSTATİSTİKLERİ =========")
    print("Toplam Servis Sayısı :", toplam_sayi)
    print()
    print("Bekleyen             :", bekleyen)
    print("Tamir Edilen         :", tamir_edilen)
    print("Tamamlanan           :", tamamlanan)
    print()
    print("Toplam Kazanç        :", toplam_kazanc, "TL")
    print("Ortalama Servis      :", ortalama, "TL")




def menu_goster():
    print("\n========================================")
    print("       TEKNİK SERVİS TAKİP SİSTEMİ")
    print("========================================")
    print("1 - Yeni Servis Kaydı Oluştur")
    print("2 - Tüm Servis Kayıtlarını Listele")
    print("3 - Servis Kaydı Ara")
    print("4 - Servis Durumunu Güncelle")
    print("5 - Servis Ücretini Güncelle")
    print("6 - Tamamlanan Servisleri Listele")
    print("7 - Toplam Kazancı Göster")
    print("8 - Servis İstatistiklerini Göster")
    print("0 - Çıkış")


def main():
    servisler = servisleri_yukle()

    while True:
        menu_goster()

        try:
            secim = int(input("Seçiminiz: "))
        except ValueError:
            print("Hatalı giriş. Lütfen sayısal bir değer giriniz.")
            continue

        if secim == 1:
            yeni_kayit_olustur(servisler)
        elif secim == 2:
            tum_kayitlari_listele(servisler)
        elif secim == 3:
            kayit_ara(servisler)
        elif secim == 4:
            durum_guncelle(servisler)
        elif secim == 5:
            ucret_guncelle(servisler)
        elif secim == 6:
            tamamlananlari_listele(servisler)
        elif secim == 7:
            toplam_kazanc_goster(servisler)
        elif secim == 8:
            istatistikleri_goster(servisler)
        elif secim == 0:
            print("Program kapatılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()