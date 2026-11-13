TL_miktarı=int(input("Lütfen TL cinsinden miktarı giriniz: "))
USD_kuru=float(input("Lütfen USD kuru giriniz: "))
USD_miktarı=TL_miktarı/USD_kuru
print(f"{TL_miktarı} TL, {USD_miktarı} USD eder.")