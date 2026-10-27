
dersler = ["Python", "Veri Tabanı", "Algoritma", "Matematik"]
durumlar = ("Başarısız", "Geçti", "Başarılı", "Yüksek Başarı")
teknik_bolumler = ["Yazılım Mühendisliği", "Bilgisayar Mühendisliği", "Elektrik Elektronik Mühendisliği"]


ad = input("Öğrenci Adı: ")
yas = int(input("Yaşı: "))
bolum = input("Bölümü: ")
devamsizlik = int(input("Devamsızlık: "))
aile_geliri = float(input("Aile Geliri: "))


notlar = {
    "vize": float(input("Vize: ")),
    "final": float(input("Final: ")),
    "proje": float(input("Proje: "))
}


ortalama = (
    notlar["vize"] * 0.30
    + notlar["final"] * 0.50
    + notlar["proje"] * 0.20
)


if devamsizlik > 5:
    print("Devamsızlıktan kaldınız.")
elif notlar["final"] < 50:
    print("Final barajını geçemediniz.")
elif ortalama < 50:
    print(f"Durum: {durumlar[0]}")
elif ortalama < 70:
    print(f"Durum: {durumlar[1]}")
elif ortalama < 85:
    print(f"Durum: {durumlar[2]}")
else:
    print(f"Durum: {durumlar[3]}")


if ortalama >= 80 and aile_geliri <= 40000:
    print("Başarı bursuna uygunsunuz.")


if ortalama >= 90 and notlar["final"] >= 90 and notlar["proje"] >= 85:
    print("Üstün Başarı Bursu Adayısınız.")


if ortalama < 55 or devamsizlik >= 4 or notlar["final"] < 55:
    print("Akademik risk grubundasınız.")
else:
    print("Akademik risk görünmüyor.")


if bolum in teknik_bolumler:
    print("Teknik bölüm öğrencisi.")
else:
    print("Diğer bölüm öğrencisi.")


if bolum in teknik_bolumler and ortalama >= 85:
    print("Etiket: Teknik Yüksek Başarı Öğrencisi")