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

    