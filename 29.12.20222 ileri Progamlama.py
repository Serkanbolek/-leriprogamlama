"""metin = "Blogların içeriği geleneksel internet içeriğinden farklılık gösterdiği için sadece bloglar için kurulmuş özel indeksleme mekanizmaları ve arama motorları bulunmaktadır."
buyuk_harfler =[]
kucuk_harfler =[]
for i in metin:
    if i.isupper():
        buyuk_harfler.append(i)
    elif i.islower():
        kucuk_harfler.append(i)
    else:
        pass
print(buyuk_harfler)
print(kucuk_harfler)
metin = "SERKAN"
def ters(metin):
    x = ""
    index = len(metin)
    while index>0:
        x+=metin[index-1]
        index = index -1
    return x
print(ters(metin))
"listeyi tersten yazma"
sayi = int("6")
toplam = 0
for j in range(1,sayi):
     if sayi % j == 0:
         toplam += j
if toplam == sayi:
    print("Mükemel Sayıdır")
else:
    print("Mükümel Sayı Değildir.")

def us_al(taban,us):
    if taban == 1 :
        return 1;
    elif us == 0:
        return 1
    else:
       return taban * us_al(taban,us-1)
print(us_al(5,3))
"""""
def faktorliyel(sayı):
    if sayı == 1:
        return 1
    else:
      return  sayı * faktorliyel(sayı-1)
print(faktorliyel(5))