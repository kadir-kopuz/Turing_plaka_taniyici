class PlakaTuringMakinesi:
    def __init__(self, plaka): #uzunluk ve karakter kontrolü + girdiyi banda yerleştirme
        self.bant = list(plaka + "_")
        self.kafa = 0
        self.durum = "q0"
        self.gecisler = self._gecis_tablosunu_olustur()

    def _gecis_tablosunu_olustur(self): #geçiş kuralları 
        t = {}
        rakamlar = "0123456789"
        harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for r in rakamlar: t[("q0", r)] = ("q1", r, "R")
        
        for r in rakamlar: t[("q1", r)] = ("q2", r, "R")
        
        for h in harfler: t[("q2", h)] = ("q3", h, "R")
        
        for h in harfler: t[("q3", h)] = ("q4", h, "R")
        
        for r in rakamlar: t[("q4", r)] = ("q5", r, "R")
        
        for r in rakamlar: t[("q5", r)] = ("q6", r, "R")
        
        for r in rakamlar: t[("q6", r)] = ("q7", r, "R")
        
        t[("q7", "_")] = ("q_kabul", "_", "S")
        
        return t

    def calistir(self):
        adim = 1
        
        while self.durum != "q_kabul" and self.durum != "q_red":
            # hangi sembol
            okunan = self.bant[self.kafa] if self.kafa < len(self.bant) else "_"
            
            print(f" Adım {adim} ")
            print(f"Mevcut durum: {self.durum}")
            print(f"Okunan sembol: {okunan}")
            
            # işlemi alma
            islem = self.gecisler.get((self.durum, okunan))
            
            if islem is None:
                # direkt red durumu
                self.durum = "q_red"
                print("Kafa hareketi: Dur (S)")
            else:
                yeni_durum, yazilacak, hareket = islem
                self.bant[self.kafa] = yazilacak
                self.durum = yeni_durum
                
                if hareket == "R":
                    self.kafa += 1
                    print("Kafa hareketi: Sağ (R)")
                elif hareket == "L":
                    self.kafa -= 1
                    print("Kafa hareketi: Sol (L)")
                else:
                    print("Kafa hareketi: Dur (S)")
                    
            bant_metni = "".join(self.bant)
            kafa_isareti = " " * self.kafa + "↑"
            print("Bant içeriği:")
            print(bant_metni)
            print(kafa_isareti)
            print()
            
            adim += 1

        # son durum nihai
        if self.durum == "q_kabul":
            print("Sonuç: KABUL")
        else:
            print("Sonuç: RED")


if __name__ == "__main__":
    girdi = input("Lütfen plaka formatını giriniz: ")
    
    makine = PlakaTuringMakinesi(girdi)
    makine.calistir()