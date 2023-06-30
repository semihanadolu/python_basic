
print("sayıları BOŞLUK BIRAKARAK giriniz")

giris= input()
sayilar = giris.split(' ')
sayilar2 = [int(i) for i in sayilar]
yineleyen_elemanlar = {}

def elemanlariSay(liste):

  
  for eleman in liste:
    if eleman in yineleyen_elemanlar:
      yineleyen_elemanlar[eleman] += 1
    else:
      yineleyen_elemanlar[eleman] = 1

  for eleman, sayi in yineleyen_elemanlar.items():
      print(f"{eleman} : {sayi}")


elemanlariSay(sayilar2)