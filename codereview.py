
# 🔐 SİBER GÜVENLİK SİSTEMİ

MAVI = "\033[94m"
YESIL = "\033[92m"
KIRMIZI = "\033[91m"
SIFIRLA = "\033[0m"

sistem_parolasi = "Fatih1453"
dogrulama_kodu = "5532"

print(MAVI + "\n===== GÜVENLİ GİRİŞ PANELİ =====" + SIFIRLA)

# 1. Aşama: Parola kontrolü
girilen_parola = input("\n[1/2] Sistem parolası: ")

if girilen_parola == sistem_parolasi:
    print(YESIL + "✔ Parola doğrulandı!" + SIFIRLA)

    # 2. Aşama: Kod kontrolü
    girilen_kod = input("\n[2/2] Doğrulama kodu: ")

    if girilen_kod == dogrulama_kodu:
        print(YESIL + "\n✔ ERİŞİM ONAYLANDI" + SIFIRLA)
        print("Sisteme hoş geldiniz.")
    else:
        print(KIRMIZI + "\n✘ Hatalı doğrulama kodu!" + SIFIRLA)
        print("Erişim reddedildi.")
else:
    print(KIRMIZI + "\n✘ Hatalı sistem parolası!" + SIFIRLA)
    print("Erişim reddedildi.")

print(MAVI + "\n===============================" + SIFIRLA)
