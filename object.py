class Kartya:
    def __init__(self, ID, Nev, szin, ertek, priority, kep):
        self.ID = int(ID)
        self.Nev = Nev
        self.szin = szin
        self.ertek = int(ertek)
        self.priority = int(priority)
        self.kep = kep

    def __repr__(self):
        return f'< object.kartya data: ID: {self.ID}, Nev: {self.Nev}, szin: {self.szin}, ertek: {self.ertek}, priority: {self.priority}, kep: {self.kep}'