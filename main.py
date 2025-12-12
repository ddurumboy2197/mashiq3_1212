class Hayvon:
    def ovoz(self):
        pass

class Kuchuk(Hayvon):
    def ovoz(self):
        return "Vov-vov!"

class Mushuk(Hayvon):
    def ovoz(self):
        return "Miyov!"


hayvonlar = [Kuchuk(), Mushuk()]
for hayvon in hayvonlar:
    print(hayvon.ovoz())
