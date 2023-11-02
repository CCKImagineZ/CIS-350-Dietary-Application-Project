class Data:
    def __init__(self, fname:str, calcount:int, typemeal:str, date:str):
        self.fname = fname
        self.calcount = calcount
        self.typemeal = typemeal
        self.date = date

    def get_data(self):
        return f"{self.fname}, {self.calcount}, {self.typemeal}, {self.date}"