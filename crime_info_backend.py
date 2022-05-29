import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("Create Table IF NOT EXISTS crime (id INTEGER PRIMARY KEY,Type text,Street text,Zipcode integer,Day integer,Month integer,Year integer)")
        self.conn.commit()

    def insert(self,Type,Street,Zipcode,Day,Month,Year):
        self.cur.execute("INSERT INTO crime VALUES (NULL,?,?,?,?,?,?)",(Type,Street,Zipcode,Day,Month,Year))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM crime")
        rows=self.cur.fetchall()
        return rows

    def search(self,Type="",Street="",Zipcode="",Day="",Month="",Year=""):
        self.cur.execute("SELECT * FROM crime WHERE Type=? OR Street=? OR Zipcode=? OR Day=? OR Month=? OR Year=?",(Type,Street,Zipcode,Day,Month,Year))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM crime WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,Type,Street,Zipcode,Day,Month,Year):
        self.cur.execute("UPDATE crime SET Type=?, Street=?, Zipcode=?, Day=?, Month=?, Year=? WHERE id=?",(Type,Street,Zipcode,Day,Month,Year,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close