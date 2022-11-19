""""
Liste=[]

eleman_sayısı = int(input("Eleman Sayısı Giriniz : "))

for i  in range(0,eleman_sayısı):
    eleman = int(input("Elamanı Giriniz : "))
    Liste.append(eleman)
print(Liste)

Liste=[]
toplam = 0
eleman_sayısı = int(input("Eleman Sayısı Giriniz : "))

for i  in range(0,eleman_sayısı+1):
    eleman = int(input("Elamanı Giriniz : "))
    Liste.append(eleman)
print(Liste)
boyut = len(Liste)
for i in range(0,boyut+1):
    toplam = toplam +Liste[i]

print(toplam)

Liste=[]

eleman_sayısı = int(input("Eleman Sayısı Giriniz : "))

for i  in range(0,eleman_sayısı):
    eleman = int(input("Elamanı Giriniz : "))
    Liste.append(eleman)
print(Liste)

Liste=[]
toplam = 0
eleman_sayısı = int(input("Eleman Sayısı Giriniz : "))

for i  in range(0,eleman_sayısı):
    eleman = int(input("Elamanı Giriniz : "))
    Liste.append(eleman)
print(Liste)
boyut = len(Liste)
for i in range(0,eleman_sayısı):
    toplam = toplam+Liste[i]

ortalama = toplam / (eleman_sayısı)
sayı = 0
for i in range(0,eleman_sayısı):
    if ortalama > Liste[i]:
        print(Liste[i])
        sayı = sayı + 1
print(sayı)
"""""
liste1=[]
liste2=[]

elaman_sayısı = int(input("Eleman Sayısı Giriniz : "))
for i  in range(0,elaman_sayısı):
    eleman = int(input("Elamanı Giriniz : "))
    liste1.append(eleman)
for i  in range(0,elaman_sayısı):
    eleman = int(input("Elamanı Giriniz : "))
    liste2.append(eleman)
durum = True
for i  in range(0,elaman_sayısı):
    if liste1[i] == liste2[i]:
        durum = False
print(durum)