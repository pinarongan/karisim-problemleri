# Tuzlu su karışımlarını birleştirip, oluşan son karışımın tuz yüzdesini hesaplamak.



# -------------------------------------------------------------
print("\nAşağıdaki soru tiplerinden birini seçiniz. (Seçmek için 1 ya da  2 yazınız.) \n")
print("SORU TİPİ 1: Elinizde birkaç tane tuzlu su karışımı var ve her birinin kaçar gr tuz ve kaçar  gr su içerdiğini biliyorsunuz.\nElinizdeki tüm karışımları ortak bir kapta birleştirmek istediğinizde ortaya çıkacak olan karışım hakkında bilgi edinmek istiyorsunuz.\n")
print("SORU TİPİ 2: Elinizde birkaç tane tuzlu su karışımı var ve her birinin kaçar gr olduğunu ve yüzde kaçının tuz olduğunu biliyorsunuz.\nElinizdeki tüm karışımları ortak bir kapta birleştirmek istediğinizde ortaya çıkacak olan karışım hakkında bilgi edinmek istiyorsunuz.\n")
soru_tipi = int(input())

n = int(input("Kaç tane karışımı birleştirmeyi planlıyorsunuz?\n"))

def tuz_yuzdesi(tuz,su):
    toplam = tuz+su
    return (100*tuz)/toplam

Karisim = {
    "Tuz" : 0,
    "Su" : 0
}
# SORU TİPİ 1: Elinizde birkaç tane tuzlu su karışımı var ve
# her birinin kaçar gr tuz ve kaçar  gr su içerdiğini biliyorsunuz.
# Elinizdeki tüm karışımları ortak bir kapta birleştirmek istediğinizde
# ortaya çıkacak olan karışım hakkında bilgi edinmek istiyorsunuz.

if soru_tipi == 1:
    for i in range(n):
        Karisim["Tuz"] += int(input(f'{i+1}. karışımın tuz miktarı (gr): '))
        Karisim["Su"] += int(input(f'{i+1}. karışımın su miktarı (gr): '))
    print(f'Karışımlar birleştirilince elde edilen karışımın')
    print(f'Toplam ağırlığı: {Karisim["Tuz"]+Karisim["Su"]} gr')
    print(f'Tuz miktarı: {Karisim["Tuz"]} gr')
    print(f'Su miktarı: {Karisim["Su"]} gr')
    print(f'Tuz oranı: %{tuz_yuzdesi(Karisim["Tuz"],Karisim["Su"])}')

# -------------------------------------------------------------

# SORU TİPİ 2: Elinizde birkaç tane tuzlu su karışımı var ve
# her birinin kaçar gr olduğunu ve yüzde kaçının tuz olduğunu biliyorsunuz.
# Elinizdeki tüm karışımları ortak bir kapta birleştirmek istediğinizde
# ortaya çıkacak olan karışım hakkında bilgi edinmek istiyorsunuz.
elif soru_tipi == 2:
    hepsinin_toplami = 0
    for i in range(n):
        toplam =int(input(f'{i+1}. karışımın toplam ağırlığı (gr): '))
        hepsinin_toplami += toplam
        yuzde = int(input(f'{i+1}. karışımın tuz yüzdesi (%): '))
        Karisim["Tuz"] += yuzde*toplam/100
    Karisim["Su"] += hepsinin_toplami-Karisim["Tuz"]
    print(f'Karışımlar birleştirilince elde edilen karışımın')
    print(f'Toplam ağırlığı: {Karisim["Tuz"]+Karisim["Su"]} gr')
    print(f'Tuz miktarı: {Karisim["Tuz"]} gr')
    print(f'Su miktarı: {Karisim["Su"]} gr')
    print(f'Tuz oranı: %{tuz_yuzdesi(Karisim["Tuz"],Karisim["Su"])}')

else:
    print("Yukarıdaki soru tiplerinden birini seçmelisiniz.")