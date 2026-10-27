

odalar = [
    {"no": 101, "tip": "Tek Kişilik", "fiyat": 1200, "dolu": False},
    {"no": 102, "tip": "Tek Kişilik", "fiyat": 1200, "dolu": False},
    {"no": 201, "tip": "Çift Kişilik", "fiyat": 1800, "dolu": False},
    {"no": 202, "tip": "Çift Kişilik", "fiyat": 1800, "dolu": False},
    {"no": 301, "tip": "Deluxe", "fiyat": 2800, "dolu": False},
    {"no": 302, "tip": "Deluxe", "fiyat": 2800, "dolu": False},
]


rezervasyonlar = []



def odalari_goster():
    print("")
    print("--- ODA LİSTESİ ---")
    for oda in odalar:
        if oda["dolu"] == True:
            durum = "DOLU"
        else:
            durum = "BOŞ"
        print(str(oda["no"]) + " - " + oda["tip"] + " - " + str(oda["fiyat"]) + " TL - " + durum)



def rezervasyon_yap():
    musteri = input("Müşteri adı: ")
    oda_no = int(input("Oda numarası: "))

   
    bulunan_oda = None
    for oda in odalar:
        if oda["no"] == oda_no:
            bulunan_oda = oda

   
    if bulunan_oda == None:
        print("Böyle bir oda bulunmamaktadır.")
        return

    
    if bulunan_oda["dolu"] == True:
        print("Bu oda şu anda dolu.")
        return

    gece = int(input("Kaç gece kalacak: "))

    
    normal_ucret = bulunan_oda["fiyat"] * gece

    
    if gece <= 2:
        indirim_orani = 0
    elif gece <= 6:
        indirim_orani = 0.10
    else:
        indirim_orani = 0.20

    indirim = normal_ucret * indirim_orani
    toplam = normal_ucret - indirim

   
    yeni_rezervasyon = {
        "musteri": musteri,
        "oda": oda_no,
        "gece": gece,
        "toplam": toplam
    }
    rezervasyonlar.append(yeni_rezervasyon)

    
    bulunan_oda["dolu"] = True

    print("")
    print("-------------------------")
    print("REZERVASYON OLUŞTURULDU")
    print("-------------------------")
    print("Müşteri: " + musteri)
    print("Oda: " + str(oda_no))
    print("Konaklama: " + str(gece) + " gece")
    print("Normal Ücret: " + str(normal_ucret) + " TL")
    print("İndirim: " + str(indirim) + " TL")
    print("Toplam: " + str(toplam) + " TL")



def rezervasyonlari_goster():
    if len(rezervasyonlar) == 0:
        print("Henüz rezervasyon bulunmamaktadır.")
        return

    print("")
    print("--- REZERVASYON LİSTESİ ---")
    sayac = 1
    for rez in rezervasyonlar:
        print("")
        print(str(sayac) + ". " + rez["musteri"])
        print("Oda: " + str(rez["oda"]))
        print("Gece: " + str(rez["gece"]))
        print("Toplam: " + str(rez["toplam"]) + " TL")
        sayac = sayac + 1



def rezervasyon_iptal_et():
    oda_no = int(input("İptal edilecek oda numarası: "))

    
    bulunan_rezervasyon = None
    for rez in rezervasyonlar:
        if rez["oda"] == oda_no:
            bulunan_rezervasyon = rez

    if bulunan_rezervasyon == None:
        print("Bu odaya ait aktif rezervasyon bulunamadı.")
        return

    
    rezervasyonlar.remove(bulunan_rezervasyon)

    
    for oda in odalar:
        if oda["no"] == oda_no:
            oda["dolu"] = False

    print(str(oda_no) + " numaralı odanın rezervasyonu iptal edildi.")



def gelir_hesapla():
    toplam_gelir = 0
    for rez in rezervasyonlar:
        toplam_gelir = toplam_gelir + rez["toplam"]
    print("")
    print("Toplam rezervasyon geliri: " + str(toplam_gelir) + " TL")



def doluluk_bilgisi():
    toplam_oda = len(odalar)
    dolu_oda = 0
    for oda in odalar:
        if oda["dolu"] == True:
            dolu_oda = dolu_oda + 1

    bos_oda = toplam_oda - dolu_oda
    doluluk_orani = (dolu_oda / toplam_oda) * 100

    print("")
    print("Toplam Oda : " + str(toplam_oda))
    print("Dolu Oda   : " + str(dolu_oda))
    print("Boş Oda    : " + str(bos_oda))
    print("Doluluk    : %" + str(doluluk_orani))




while True:
    print("")
    print("=========================")
    print("   OTEL YÖNETİM SİSTEMİ")
    print("=========================")
    print("")
    print("1 - Odaları Görüntüle")
    print("2 - Rezervasyon Yap")
    print("3 - Rezervasyonları Görüntüle")
    print("4 - Rezervasyon İptal Et")
    print("5 - Gelir Bilgisi")
    print("6 - Otel Doluluk Bilgisi")
    print("0 - Çıkış")
    print("")

    secim = input("Seçiminiz: ")

    if secim == "1":
        odalari_goster()
    elif secim == "2":
        rezervasyon_yap()
    elif secim == "3":
        rezervasyonlari_goster()
    elif secim == "4":
        rezervasyon_iptal_et()
    elif secim == "5":
        gelir_hesapla()
    elif secim == "6":
        doluluk_bilgisi()
    elif secim == "0":
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçim yaptınız.")