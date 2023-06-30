

class Date:
  
    def __init__(self, gun, ay, yil):
   
        if yil < 2000:
            raise ValueError("yıl 2000'den sonra olmalı")

        if ay < 1 or ay > 12:
            raise ValueError("ay 1'le 12 arasında olmalı")

        if gun < 1 or gun > 31:
            raise ValueError("gün 1'le 21 arasında olmalı")

        self.yil = yil
        self.ay = ay
        self.gun = gun

    def tarih(self):
    
        return f"tarih geçerli: {self.gun}-{self.ay}-{self.yil}"

    def gecerliMi(self):
   
        if self.yil < 2000:
            return False

        if self.ay < 1 or self.ay > 12:
            return False

        if self.gun < 1 or self.gun > 31:
            return False
    
    
        return self.tarih()
    
       


 
    

    def haftaninGununuVer(self):

        gunler = [0, "pazartesi", 1, "salı", 2, "çarşamba", 3, "perşembe", 4, "cuma", 5, "cumartesi", 6, "pazar"]
  
        baslangictanBugune = (self.yil - 2000) * 365 + (self.yil - 2000) // 4 - (self.yil - 2000) // 100 + (self.yil - 2000) // 400 + (self.ay - 1) * 30 + self.gun

        haftaninGunu = baslangictanBugune % 7

  
        return gunler[haftaninGunu]

    
   



    

print("boşluk bırakarak gün ay yıl giriniz")
giris= input()
tarihler = giris.split(' ')
tarihler2 = [int(i) for i in tarihler]
date = Date(tarihler2[0], tarihler2[1],tarihler2[2])
print(date)
print(date.gecerliMi())
print(date.haftaninGununuVer())