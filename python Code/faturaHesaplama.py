from itertools import chain, combinations

# Kümeyi tanımlayın
kume_str = input("Faturaları '-' ile ayrılmış bir şekilde ve 2223.22 şeklinde girin: ")

kume = [float(x) for x in kume_str.replace(",",".").split("-")]

# Belirlenen sayıyı alın
belirlenen_sayi = float(input("Belirlenen en büyük sayıyı 2223.22 şeklinde girin: ").replace(",","."))

# Alt kümeleri oluşturun
alt_kumeler = []
for i in range(1, len(kume)+1):
    alt_kumeler.extend(list(combinations(kume, i)))

# Belirlenen sayıdan küçük veya eşit en büyük toplamı alan alt kümeyi bulun
en_buyuk_toplam = 0
en_buyuk_alt_kume = []
for alt_kume in alt_kumeler:
    toplam = sum(alt_kume)
    if toplam <= belirlenen_sayi and toplam >= en_buyuk_toplam:
        en_buyuk_toplam = toplam
        en_buyuk_alt_kume = alt_kume

# En büyük alt kümeyi yazdırın
print(f"Tutara en yakın ödenebilecek fatura listesi: {en_buyuk_alt_kume}")
print(f"Toplam Ödeme Tutarı: {en_buyuk_toplam}")
input("Çıkmak için bir tuşa basın...")