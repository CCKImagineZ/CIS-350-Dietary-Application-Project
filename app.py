import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect("Diet.db")
        self.cur = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("CREATE TABLE if not exists Diet(meal_name,Cal,Date,Type)")

    def insert_table(self,name,calcount,date,typem):
        self.cur.execute("INSERT INTO Diet (meal_name,Cal,Date,Type) VALUES (?,?,?,?)", (name,calcount,date,typem))
        self.connection.commit()

    def get_table(self):
        self.cur.execute("SELECT * FROM Diet")
        return self.cur.fetchall()

    def get_dailytotals(self):
        values = []
        values = self.get_table()
        final = [0, 0, 0, 0, 0, 0, 0]
        if values == []:
            return final
        else:
            for n in values:
                print(n[2])
                if n[2] == "Monday":
                    final[0] += int(n[1])
                if n[2] == "Tuesday":
                    final[1] += int(n[1])
                if n[2] == "Wednesday":
                    final[2] += int(n[1])
                if n[2] == "Thursday":
                    final[3] += int(n[1])
                if n[2] == "Friday":
                    final[4] += int(n[1])
                if n[2] == "Saturday":
                    final[5] += int(n[1])
                if n[2] == "Sunday":
                    final[6] += int(n[1])
        print(final)
        return final


